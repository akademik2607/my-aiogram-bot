from aiogram import types
from loader import dp, bot
from keyboards import create_type_of_question_markup


@dp.callback_query_handler(lambda msg: msg.data.startswith('sub_category_'))
async def bot_type_of_question(callback_query: types.CallbackQuery):
    sub_category_name = callback_query.data[len('sub_category')+1:]
    type_question_markup = create_type_of_question_markup('type_of_question', False)
    await bot.send_message(chat_id=callback_query.from_user.id, text=callback_query.data,
                           reply_markup=type_question_markup)
