from openai import OpenAI
import os

client = OpenAI(
    api_key="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",
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um especialista em séries animados. Dê respostas de maneira bem animada sobre seriados."},
        {"role": "user", "content": "Me fale sobre o seriado Apenas um Show"}
        ],
)

print(f"\n{response.choices[0].message.content}")