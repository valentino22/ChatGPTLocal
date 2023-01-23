from sys import argv
import os
import openai  # pip install openai
# get API key from https://beta.openai.com/account/api-keys
openai.api_key = ""

print(argv[1:])
if (argv[1]):
    prompt = argv[1:]
else:
    prompt = "Tell me something positive about the world."

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    frequency_penalty=0,
    presence_penalty=0,
    max_tokens=3200
)

print(response.choices[0].text)
