from aiogram import types
from loader import dp
from keyboards import category_markup
from loader import bot
from states import TestStates

@dp.callback_query_handler(lambda ans: ans.data == "Тесты")
async def bot_category(callback_query: types.CallbackQuery):


    await bot.send_message(chat_id=callback_query.from_user.id, text=callback_query.data,
                           reply_markup=category_markup)

