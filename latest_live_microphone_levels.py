import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyaudio
import audioop
from collections import deque


CHUNK = 1024
WIDTH = 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
DEVICE_ID = 1


def run():

    graph_length = 1500

    # animation function
    def animate(i, _rms_values, _queue, _stream):
        try:
            data = _stream.read(CHUNK)
            rms = audioop.rms(data, WIDTH) / 32767
            _queue.popleft()
            _queue.append(rms)
            rms_stream.append(sum(_queue)/len(_queue))
            # session_min_rms = min(_rms_values)
            session_max_rms = max(data)
            session_max.pop(0)
            session_max.append(session_max_rms)
            # session_min.pop(0)
            # session_min.append(session_min_rms)
        except Exception as e:
            pass

        # Limit the data list to X values
        data = _rms_values[-graph_length:]
        # clear the last frame and draw the next frame
        ax.clear()
        ax.plot(data)
        ax.plot(session_max[-graph_length:], color='red')
        # ax.plot(session_min[-graph_length:], color='green')
        # Format plot
        min_y, max_y = min(_rms_values), max(_rms_values)
        ax.set_ylim([min_y, 0.25])  # max_y*4])
        ax.set_title("Volume Level")
        # ax.set_ylabel("Stream Power Reading")
        ax.figure.set_size_inches(15, 4)
        ax.set_xticklabels([])
        ax.set_xticks([])

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

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=0)

    # run the animation and show the figure
    ani = animation.FuncAnimation(
        fig, animate, frames=50, fargs=[rms_stream, queue, stream], interval=20)

    plt.show()


if __name__ == '__main__':
    run()
