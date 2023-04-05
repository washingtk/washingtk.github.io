import os
import openai
from dotenv import load_dotenv
load_dotenv()

#load OpenAI API Key
# OPENAI_API_KEY = os.getenv('OpenAI_API')
OPENAI_API_KEY = os.getenv('API')
# print(OPENAI_API_KEY)

#load user prompt
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'spell.txt')
with open(file_path, 'r') as file:
    spell = file.read()

openai.api_key = OPENAI_API_KEY
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content":  "Hello!"},
    ]
)

print(response['choices'][0]['message']['content'])