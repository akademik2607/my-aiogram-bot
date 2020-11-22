from aiogram import types
from loader import dp, bot
from keyboards import create_sub_category_markup


@dp.callback_query_handler(lambda msg: msg.data.startswith('category_'))
async def bot_sub_category(callback_query: types.CallbackQuery):
    category_name = callback_query.data[len('category')+1:]
    sub_category_markup = create_sub_category_markup('sub_category', category_name)
    await bot.send_message(chat_id=callback_query.from_user.id, text=callback_query.data,
                           reply_markup=sub_category_markup)