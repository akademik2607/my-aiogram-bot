from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_markup = ReplyKeyboardMarkup([
    [
        KeyboardButton(text = "Меню")
    ]
], resize_keyboard=True)