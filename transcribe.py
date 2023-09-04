#!/usr/bin/env python3
""" A module that receives an audio file/stream 
    and transcribe to text (speech to text) using Deepgram API
"""


# importing the required dependencies
from deepgram import Deepgram
import asyncio
from record_audio import record_stream
from key import API_KEY


# initializing Api key and Mimetype
API_KEY = API_KEY
MIMETYPE = 'audio/wav'


async def record_stream1(duration: int=5) -> str:
    """ An Async func that transcribe audio/speech to text
        using deepgram api and returns string
            Param:
                duration: an int that represnts the timeframe
                          for the stream
    """


    # taking the voice/speech from the user
    FILE = record_stream(duration)


    # instantiating the Deepgram Class
    dg = Deepgram(API_KEY)

    # getting the audio/speech into the audio variable
    audio = open(FILE, 'rb')

    # configuring the source(the audio/speech data) attribute 
    source = {
        'buffer': audio,
        'mimetype': MIMETYPE
    }

    # awaiting for the deepgram to transcribe the audio/speech stream
    response = await asyncio.create_task(
        dg.transcription.prerecorded(
            source,
            {
                'smart_format': True,
                'model': "nova",
            }
        )
    )

    # extracting the transcribed text from the response
    transcripts = response['results']['channels'][0]['alternatives'][0]['transcript']
    return transcripts


if __name__ == "__main__":
    duration = 5  # Specify the recording duration in seconds
    transcripts = asyncio.run(record_stream1(duration))
    print(transcripts)
