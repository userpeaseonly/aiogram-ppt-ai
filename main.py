from openai import OpenAI
from pprint import pprint
import openai
import os
import json

# Option 1: Read from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Option 2: Set directly in the code
openai.api_key = 'your-api-key-here'

# Your existing code here


client = OpenAI()


language = "Uzbek"
topic = "Havo Ifloslanishi va uning ta'siri"
description = "Havo ifloslanishi va uning ta'siri haqida tafsilotli prezentatsiya chiqaring."
slide_count = 10

# prompt = (
#     f"Create a detailed presentation outline in {language}. "
#     f"The topic is '{topic}', it should include {slide_count} slides, "
#     f"and it is described as: {description}."
# )

# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant specialized in creating presentation outlines. Here is some paraments that you need to follow: every slide should be id based (ex: slide-1, slide-2, etc.), every slide should have a title and a description, and every slide should have a clear and concise content. and your response type should be in JSON format."},
#         {"role": "user", "content": prompt}
#     ],
#     temperature=0.7,
# )

# response_json = json.loads(response.choices[0].message.content)
# pprint(response_json)

response_json = {'slide-1': {'title': 'Kirish', 'description': 'Maqola: Suvning isrof qilinishi'}, 'slide-2': {'title': 'Suvning isrof qilinishi', 'description': 'Suvning qanday shakllanishi va yuzaga kelishi'}, 'slide-3': {'title': 'Suvning isrof qilishining sababi', 'description': "Suvni qanday isrof qilish bilan bog'liq qoidalarni tushuntirish"}, 'slide-4': {'title': 'Suvni qanday isrof qilmaslik kerak', 'description': 'Suvni samarali isrof qilmaslik uchun tavsiyalar'}, 'slide-5': {'title': 'Suvni isrof qilmaslikning foydalari', 'description': 'Suvni isrof qilmaslik bilan qanaqa foydalar olish mumkin'}, 'slide-6': {'title': "O'zgarishlar", 'description': "Suvni isrof qilmaslik natijasida qanday pozitiv o'zgarishlar kelayotgan"}, 'slide-7': {'title': 'Suvning samarali ishlatilishi', 'description': 'Suvning samarali ishlatilishi va isrof qilinmagan suvning ahamiyati'}, 'slide-8': {'title': 'Suvni samarali ishlatish strategiyalari', 'description': 'Suvni samarali ishlatish uchun qanday strategiyalar amalga oshirish mumkin'}, 'slide-9': {'title': "Suvni isrof qilishning o'qitilishi", 'description': "Suvni isrof qilishning katta tartibi va o'qitilishi"}, 'slide-10': {'title': 'Xulosa', 'description': 'Suvning isrof qilinishi haqida jamiy natijalar va takliflar'}}



