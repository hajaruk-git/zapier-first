from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def my_gpt(user_mail):
    messages = [{
            "role": "user",
            "content": f"""Anwser the question delimited
            by triple brackets like you are a viking. Here is the email:
            [[[{user_mail}]]]"""
        }]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1
    )
    return response.choices[0].message.content