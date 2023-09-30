import pyaudio
import wave
import audioop

CHUNK = 1024
WIDTH = 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
DEVICE_ID = 1


def record():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=0)

    print("Start recording")

    frames = []

    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
            rms = audioop.rms(data, WIDTH)
            print(rms)
    except KeyboardInterrupt:
        print("Done recording")
    except Exception as e:
        print(str(e))

    sample_width = p.get_sample_size(FORMAT)

    stream.stop_stream()
    stream.close()
    p.terminate()

    return sample_width, frames


def record_to_file(file_path):
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    sample_width, frames = record()
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == '__main__':
    print('#' * 80)
    print("Please provide input to the microphone, hit Stop when done.")
    print('Press Ctrl+C to stop the recording')

    record_to_file('output.wav')

    print("Result written to output.wav")
    print('#' * 80)
