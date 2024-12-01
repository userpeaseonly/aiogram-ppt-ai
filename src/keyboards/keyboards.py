from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_selection_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿 Uzbek", callback_data="lang_uz"),
                InlineKeyboardButton(text="🇷🇺 Russian", callback_data="lang_ru"),
                InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
            ]
        ]
    )
    return keyboard
