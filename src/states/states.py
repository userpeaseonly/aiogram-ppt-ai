from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Create your states here.

class PresentationCreation(StatesGroup):
    topic = State()
    description = State()
    slide_count = State()