from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_load = KeyboardButton('/загрузить')

button_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)

