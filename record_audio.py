#!/usr/bin/env python3
""" A module that uses pyaudio to capture voice from the microphone
    the module contain a function `record_stream()` that returns
    the recoreded voice in a `.wav` file format
"""


# importing the required dependencies
import pyaudio
import wave
import tempfile
import typing


def record_stream(duration: int=10, output_file: typing.Any=None) -> typing.Any:
    """ A func that records voice from the microphone of the pc using pyaudio package
        Params:
            duration: this is the max time for streaming
            outpufile: This is the `.wav file` that contains the recoreded audio
    """
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    
    # instantiating the PyAudio instance
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # printing to the console
    print('Recording...')

    # initializing a list of frames to store chunck of audio bits data
    frames = []

    # looping through the voice streams and appending to the frame
    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    # stoping and terminating the stream
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

    # configuring the wafe file.
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return output_file

if __name__ == "___main___":
    wav = record_stream(5)