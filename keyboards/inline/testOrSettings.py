from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# test_or_settings_markup = InlineKeyboardMarkup([
#     [
#         InlineKeyboardButton(text = "Тесты", callback_data = "1")
#         InlineKeyboardButton(text = "Настройки", callback_data = "2")
#     ]
# ])
test_or_settings_markup = InlineKeyboardMarkup(2)
test_or_settings_markup.add(InlineKeyboardButton(text = "Тесты", callback_data = "1"),
                     InlineKeyboardButton(text = "Настройки", callback_data = "2"))