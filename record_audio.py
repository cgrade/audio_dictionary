import pyaudio
import wave
import tempfile

def record_stream(duration=10, output_file=None):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print('Recording...')

    frames = []
    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Create a temporary WAV file
    if output_file is None:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
            output_file = tmpfile.name
            wf = wave.open(output_file, 'wb')
    else:
        wf = wave.open(output_file, 'wb')

    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return output_file

if __name__ == "___main___":
    wav = record_stream(5)