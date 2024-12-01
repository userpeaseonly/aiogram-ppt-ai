from openai import OpenAI

import openai
import os

# Option 1: Read from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Option 2: Set directly in the code
openai.api_key = 'your-api-key-here'

# Your existing code here


client = OpenAI()


completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "pythonni o'rganish uchun roadmap tuzib ber"}
    ]
)



print(completion.choices[0].message.content)