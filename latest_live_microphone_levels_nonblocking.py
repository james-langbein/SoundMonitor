import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyaudio
import audioop
from collections import deque
# from multiprocessing import Process


CHUNK = 1024
WIDTH = 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
DEVICE_ID = 2


def run():

    graph_length = 1500

    # init list for data stream
    # fill with zeros so that graph x-axis is correct length when first shown
    rms_stream = [0 for i in range(graph_length)]
    session_max = [0 for i in range(graph_length)]
    # session_min = [0 for i in range(graph_length)]

    # init list for last 10 rms values, these will be used to get average of last 25 readings (250 ms)
    queue = deque()
    queue.append([0 for i in range(100)])

    # create figure and axes objects
    fig, ax = plt.subplots()
    ax.figure.set_size_inches(12, 4)
    ax.set_title("Volume Level")
    ax.set_ylabel("Stream Power Reading")

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=0)

    # animation function
    def animate(i, _rms_stream, _queue, _stream):
        """Animate the graph.
        _rms_stream: The values from the entire session
        _queue:
        _stream: PyAudio stream
        """
        try:
            data = _stream.read(CHUNK)
            rms = audioop.rms(data, WIDTH) / 32767
            _queue.popleft()
            _queue.append(rms)

            # at the beginning of the stream the rms is really high
            # the IF statement prevents it from appending the initial high values, until the rms goes below 0.1
            # after that, it will start increasing the length of _rms_stream, and after 50 loops this will always eval
            # to True regardless of volume
            # if rms < 0.8 or len(_rms_stream) > 1510:
            rms_stream.append(sum(_queue) / len(_queue))

            session_max_rms = max(data)
            session_max.pop(0)
            session_max.append(session_max_rms)

            # session_min_rms = min(_rms_values)
            # session_min.pop(0)
            # session_min.append(session_min_rms)
        except Exception as e:
            pass

        print(len(_rms_stream))

        # Limit the data list to X values (length of graph)
        data = _rms_stream[-graph_length:]

        # clear the last frame and draw the next frame
        ax.clear()
        ax.plot(data)
        # ax.plot(session_max[-graph_length:], color='red')
        # ax.plot(session_min[-graph_length:], color='green')

        # Format plot
        min_y, max_y = min(_rms_stream), max(_rms_stream)
        ax.set_ylim([min_y, 1])  # max_y*4])
        ax.set_xticklabels([])
        ax.set_xticks([])

    # run the animation and show the figure
    ani = animation.FuncAnimation(
        fig, animate, frames=30, fargs=[rms_stream, queue, stream], interval=50)

    plt.show()


if __name__ == '__main__':
    run()
    # proc = Process(target=run)
    # proc.start()
    # proc.join()
