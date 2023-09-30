from matplotlib import pyplot as plt
import matplotlib.animation as animation
import pyaudio
import audioop
import time

CHUNK = 1024
WIDTH = 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
DEVICE_ID = 1


def record():

    def animate(i, _data):
        _data = _data[-300:]
        ax.clear()
        ax.plot(_data)
        ax.set_ylim([0, 20000])
        ax.set_title('Live Sound Level')

    rms_stream = []
    fig, ax = plt.subplots()

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=0)

    print("Opening stream...")

    try:
        while True:
            data = stream.read(CHUNK)
            rms_value = audioop.rms(data, WIDTH)
            rms_stream.append(rms_value)
            print(rms_value)
            # anim = animation.FuncAnimation(fig, animate, frames=100, fargs=[rms_stream], interval=10)

            plt.show()
            time.sleep(0.2)
    except KeyboardInterrupt:
        print('Stopping stream...')
    except Exception as e:
        print(str(e))

    sample_width = p.get_sample_size(FORMAT)

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Closed stream.")

    # print(len(frames))

    # return sample_width#, frames


if __name__ == '__main__':
    record()
