import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_llm(messages, model="gpt-4o-mini"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"