import openai
import asyncio
from transcribe import record_stream1
from keys import (API_KEY, org_key, GPT_KEY)


prompts = asyncio.run(record_stream1())

openai.api_key = GPT_KEY
openai.organization = org_key

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

response = generate_response(prompts)
print(prompts)
print(response)
