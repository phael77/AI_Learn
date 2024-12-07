from openai import OpenAI

client = OpenAI(
    api_key="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"
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