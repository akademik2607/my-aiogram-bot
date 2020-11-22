from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_requests import db_request

def create_sub_category_markup(vale_name, parent_val_name):
    sub_category_markup = InlineKeyboardMarkup()
    categories = db_request(vale_name, parent_val_name)
    for category in categories:
        sub_category_markup.add(InlineKeyboardButton(category['sub_category_name'],
                                 callback_data='sub_category_'+category['sub_category_name']))
    return sub_category_markup