from aiogram.dispatcher.filters.state import StatesGroup, State

class TestStates(StatesGroup):
    CATEGORY = State()
    SUB_CATEGORY = State()