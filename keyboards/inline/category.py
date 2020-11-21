from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import db_request

category_markup = InlineKeyboardMarkup()
categories = db_request('category')
for category in categories:
    category_markup.add(InlineKeyboardButton(category['category_name'],
                                 callback_data=category['category_name']))
