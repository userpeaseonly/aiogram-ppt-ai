from openai import OpenAI


client = OpenAI()


completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "pythonni o'rganish uchun roadmap tuzib ber"}
    ]
)



print(completion.choices[0].message.content)