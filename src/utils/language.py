import json
import os
from aiogram.fsm.context import FSMContext

DEFAULT_LANGUAGE = "uz"

LOCALES_DIR = os.path.join(os.path.dirname(__file__), "../locales")
translations = {}

def load_translations():
    global translations
    for filename in os.listdir(LOCALES_DIR):
        if filename.endswith(".json"):
            lang_code = filename.split(".")[0]
            with open(os.path.join(LOCALES_DIR, filename), "r", encoding="utf-8") as f:
                translations[lang_code] = json.load(f)

def get_translation(key: str, language: str = DEFAULT_LANGUAGE) -> str:
    return translations.get(language, {}).get(key, f"_{key}_")

async def set_language(state: FSMContext, language: str):
    await state.update_data(language=language)

async def get_language(state: FSMContext) -> str:
    data = await state.get_data()
    return data.get("language", DEFAULT_LANGUAGE)
