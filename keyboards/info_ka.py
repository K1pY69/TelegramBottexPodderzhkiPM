from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b6 = KeyboardButton('/number')
b7 = KeyboardButton('/address')
b8 = KeyboardButton('/contacts')
b9 = KeyboardButton('/command')

ka_info = ReplyKeyboardMarkup(resize_keyboard=True)

ka_info.row(b7, b6, b8).add(b9)
