from dataclasses import dataclass

from dotenv import load_dotenv

from .base import getenv, ImproperlyConfigured


@dataclass
class TelegramBotConfig:
    token: str


@dataclass
class OpenAIConfig:
    api_key: str


@dataclass
class Config:
    tg_bot: TelegramBotConfig
    openai: OpenAIConfig


def load_config() -> Config:
    # Parse a `.env` file and load the variables into environment variables
    load_dotenv()

    return Config(
        tg_bot=TelegramBotConfig(token=getenv("BOT_TOKEN")),
        openai=OpenAIConfig(api_key=getenv("OPENAI_API_KEY"))
    )
