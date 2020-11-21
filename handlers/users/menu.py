from aiogram import types
from loader import dp
from keyboards import test_or_settings_markup

@dp.message_handler(text = "Меню")
async def bot_category(message: types.Message):
    await message.answer("Меню", reply_markup = test_or_settings_markup)