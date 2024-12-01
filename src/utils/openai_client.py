from openai import OpenAI
import openai
from config import load_config
import logging

# Initialize the logger
logging.basicConfig(level=logging.INFO)

# Load the configuration
config = load_config()

# Set OpenAI API key
openai.api_key = config.openai.api_key

# Initialize the OpenAI client
client = OpenAI()


async def generate_presentation_text(topic: str, description: str, slide_count: int, language: str) -> str:
    prompt = (
        f"Create a detailed presentation outline in {language}. "
        f"The topic is '{topic}', it should include {slide_count} slides, "
        f"and it is described as: {description}."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in creating presentation outlines."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        # Extract the assistant's reply using object attributes
        message_content = response.choices[0].message.content.strip()
        logging.info("--- Response: %s ---", message_content)
        return message_content
    except openai.OpenAIError as e:
        logging.error("OpenAI API Error: %s", e)
        return f"An error occurred: {e}"
