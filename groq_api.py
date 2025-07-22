
import os
import openai
from dotenv import load_dotenv

load_dotenv() 

openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"  

def get_groq_response(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="llama3-8b-8192",  # You can also try: "mixtral-8x7b-32
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
