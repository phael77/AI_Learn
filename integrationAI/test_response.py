from openai import OpenAI
import os

client = OpenAI(
    api_key="SUA_CHAVE_API"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user", "content": "Me fale sobre o seriado Apenas um Show"
    }],
)

print(response.choices[0].message.content)