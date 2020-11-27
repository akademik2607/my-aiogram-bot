from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_requests import db_request

def create_type_of_question_markup(vale_name, false):
    type_of_question_markup = InlineKeyboardMarkup()
    types = db_request(vale_name, False)
    for typeQ in types:
        type_of_question_markup.add(InlineKeyboardButton(typeQ['type_name'],
                                 callback_data='type_name_'+typeQ['type_name']))
    return type_of_question_markup
