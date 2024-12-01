import openai
from config.config import load_config

config = load_config()

# Initialize OpenAI client
openai.api_key = config.openai.api_key

async def generate_presentation_text(topic: str, description: str, slide_count: int, language: str) -> str:
    """
    Generate presentation text using OpenAI.

    :param topic: Topic of the presentation
    :param description: Description of the presentation
    :param slide_count: Number of slides
    :param language: Language for the response
    :return: Generated presentation text
    """
    prompt = (
        f"You are an expert presentation creator. Create a presentation in {language} based on the following details:\n\n"
        f"Topic: {topic}\n"
        f"Description: {description}\n"
        f"Number of slides: {slide_count}\n\n"
        f"For each slide, provide the title and the content. Use concise language and structure the text clearly. "
        f"Ensure the response matches the specified language ({language})."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1500,
    )

    return response["choices"][0]["message"]["content"]
