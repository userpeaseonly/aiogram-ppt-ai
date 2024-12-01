import logging
import openai
import json
from openai import OpenAI
from config import load_config

# Initialize the logger
logging.basicConfig(level=logging.INFO)

# Load the configuration
config = load_config()

# Set OpenAI API key
openai.api_key = config.openai.api_key

# Initialize the OpenAI client
client = OpenAI()



async def generate_presentation_text(topic: str, description: str, slide_count: int, language: str):
    prompt = (
        f"Create a detailed presentation outline in {language}. "
        f"The topic is '{topic}', it should include {slide_count} slides, "
        f"and it is described as: {description}."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in creating presentation outlines. Here is some paraments that you need to follow: every slide should be id based (ex: slide-1, slide-2, etc.), every slide should have a title and a description, and every slide should have a clear and concise content. and your response type should be in JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        # Extract the assistant's reply using object attributes
        response_json = json.loads(response.choices[0].message.content)
        return response_json
    except openai.OpenAIError as e:
        logging.error("OpenAI API Error: %s", e)
        return f"An error occurred: {e}"
