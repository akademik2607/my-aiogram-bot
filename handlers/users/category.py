from aiogram import types
from loader import dp

@dp.message_handler(text = "Категория")
async def bot_category(message: types.Message):
    await message.answer("Категория")
