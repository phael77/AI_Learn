from openai import OpenAI
import os

client = OpenAI(
    api_key="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"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user", "content": "Me fale sobre o seriado Apenas um Show"
    }],
)

print(response.choices[0].message.content)