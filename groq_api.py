import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"  # ✅ Correct this line

def get_groq_response(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print("Groq API Error:", e)
        return "Error fetching response."
