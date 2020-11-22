from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_requests import db_request

category_markup = InlineKeyboardMarkup()
categories = db_request('category', False)
for category in categories:
    category_markup.add(InlineKeyboardButton(category['category_name'],
                                 callback_data='category_'+category['category_name']))
