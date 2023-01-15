from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b2 = KeyboardButton('/info')
#b4 = KeyboardButton('/command')
b5 = KeyboardButton('/support')
b6 = KeyboardButton('/support_call')
ka_client = ReplyKeyboardMarkup(resize_keyboard=True)

ka_client.add(b2).row(b5, b6)
