from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from src.states.states import PresentationCreation
from src.keyboards.keyboards import language_selection_keyboard
from src.utils.language import set_language, get_translation, get_language
from src.utils.openai_client import generate_presentation_text



router: Router = Router()

# /start command
class LanguageCallbackData(CallbackData, prefix="lang"):
    language: str

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.reply(
        get_translation("start"),
        reply_markup=language_selection_keyboard()
    )

@router.callback_query()
async def handle_language_selection(callback: CallbackQuery, state: FSMContext):
    lang_mapping = {"lang_uz": "uz", "lang_ru": "ru", "lang_en": "en"}
    selected_language = lang_mapping.get(callback.data)
    if not selected_language:
        return await callback.answer("Invalid selection")

    await set_language(state, selected_language)
    await callback.message.edit_text(get_translation("start", selected_language))

# /help command
@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.reply("Available commands:\n/start - Start the bot\n/help - Show this help message\n/new - Create a new presentation")


# /new command - Start presentation creation
@router.message(Command("new"))
async def cmd_new(message: Message, state: FSMContext):
    language = await get_language(state)
    await message.reply(get_translation("new_presentation_topic", language))
    await state.set_state(PresentationCreation.topic)

# Step 1: Get Topic
@router.message(PresentationCreation.topic)
async def get_topic(message: Message, state: FSMContext):
    language = await get_language(state)
    await state.update_data(topic=message.text)
    await message.reply(get_translation("new_presentation_description", language))
    await state.set_state(PresentationCreation.description)

# Step 2: Get Description
@router.message(PresentationCreation.description)
async def get_description(message: Message, state: FSMContext):
    language = await get_language(state)
    await state.update_data(description=message.text)
    await message.reply(get_translation("new_presentation_slide_count", language))
    await state.set_state(PresentationCreation.slide_count)


# Step 3: Get Slide Count and Generate Presentation
@router.message(PresentationCreation.slide_count)
async def get_slide_count(message: Message, state: FSMContext):
    language = await get_language(state)
    try:
        slide_count = int(message.text)
        if slide_count <= 0:
            raise ValueError
        await state.update_data(slide_count=slide_count)
        data = await state.get_data()
        topic = data['topic']
        description = data['description']

        # Notify user that the presentation is being generated
        await message.reply(get_translation("presentation_creating", language).format(
            topic=topic, description=description, slide_count=slide_count
        ))

        # Generate presentation text using OpenAI
        presentation_text = await generate_presentation_text(
            topic=topic,
            description=description,
            slide_count=slide_count,
            language=language,
        )

        # Send the generated presentation text to the user
        await message.reply(presentation_text)
        await state.clear()  # Clear the FSM state

    except ValueError:
        await message.reply(get_translation("invalid_slide_count", language))
    except Exception as e:
        # Handle OpenAI or other errors
        await message.reply(get_translation("generation_error", language).format(error=str(e)))