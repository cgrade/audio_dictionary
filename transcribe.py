from deepgram import Deepgram
import asyncio
from record_audio import record_stream  # Assuming you have a func.py module with the record_audio function
from keys import API_KEY

API_KEY = API_KEY
MIMETYPE = 'audio/wav'


async def record_stream1(duration=5):
    # Record audio for the specified duration
    FILE = record_stream(duration)

    dg = Deepgram(API_KEY)
    audio = open(FILE, 'rb')

    source = {
        'buffer': audio,
        'mimetype': MIMETYPE
    }
    response = await asyncio.create_task(
        dg.transcription.prerecorded(
            source,
            {
                'smart_format': True,
                'model': "nova",
            }
        )
    )

    transcripts = response['results']['channels'][0]['alternatives'][0]['transcript']
    return transcripts


if __name__ == "__main__":
    duration = 5  # Specify the recording duration in seconds
    transcripts = asyncio.run(record_stream1(duration))
    print(transcripts)