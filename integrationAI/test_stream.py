from openai import OpenAI

client = OpenAI(
    api_key="SUA_CHAVE_API"
)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user", "content": "Me conte sobre o seriado Todo Mundo Odeia o Chris"
    },],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end='')