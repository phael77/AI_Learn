from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.tools import tool
import os

os.environ['OPENAI_API_KEY'] = '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'

model = ChatOpenAI(
    model='gpt-4o-mini',
)

messages = [
    {'role': 'system', 'content': 'Você é um assistente especialista em IOT, e que sabe integrar IoT com inteligência artificial.'},
    {'role': 'user', 'content': 'Me diga qual é uma maneira eficiente de integração de IA com ESP-32 node mcu'},
]

response = model.invoke(messages)

print(response)
print(response.content)