from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot

@dp.callback_query_handler(lambda msg: msg.data.startswith('type_name'))
async def bot_test_or_learn(callback_query: types.CallbackQuery):
    test_or_learn_markup = types.InlineKeyboardMarkup()
    test_or_learn_markup.add(types.InlineKeyboardButton(text = 'Тест', callback_data = 'test'))
    test_or_learn_markup.add(types.InlineKeyboardButton(text = 'Обучение', callback_data = 'learning'))
    await bot.send_message(chat_id=callback_query.from_user.id, text=callback_query.data,
                           reply_markup=test_or_learn_markup)




