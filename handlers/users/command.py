from aiogram import types, Dispatcher
from loader import dp, bot
from keyboards.client_ka import ka_client
from keyboards.info_ka import ka_info

# from data_base import sqlite_db


# заполнение ответов на вопросы


# пользовательские фишки

#@dp.message_handler(commands=['start'])
#async def command_start(message: types.Message):
   # try:
     #   await bot.send_message(message.from_user.id,
        #                       'Здравствуйте!Я являюсь ботом тех-поддержки компании ООО МТК "ТЕХНОСОФТ", чтобы начать пользоваться напишите команду /command.')
   # except:
     #   await message.reply('Общение с ботом через личные сообшения, напишити ему - https://t.me/Techno_Soft_SuppBot')


# commadi
@dp.message_handler(commands=['command'])
async def CommandB(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Список комманд, которыми Вы можете пользоваться:\n/сommand - позволяет увидеть основные команды.\n/info - позволяет узнать, контактную информацию о нас.\n/support - комманда позволяет написать 1 сообщение специалисту и получить ответ.\n/support_call - команда позволяет пообщаться со специалистом. ',
                           reply_markup=ka_client)


# iNFO
@dp.message_handler(commands=['info'])
async def Information(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберет команду, чтобы узнать информацию', reply_markup=ka_info)


# @dp.message_handler()
# async def echo_send(message: types.Message):
#   if message.text =='/info':
#      await message.answer('Выберете интересующую вас информацию')
# adress
@dp.message_handler(commands=['address'])
async def AdressMTK(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Наш адресс:\n129626, г. Москва,ВН.ТЕР.Г. МУНИЦИПАЛЬНЫЙ ОКРУГ АЛЕКСЕЕВСКИЙ, ПР-КТ МИРА, Д. 102, К. 1,ПОМЕЩ. 3/7, ОФИС 59')


# contakti
@dp.message_handler(commands=['contacts'])
async def ContactsMTK(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Контакты:\nМы в телеграмме: \n@Cokol888 и https://t.me/TexhnoSoft. \nНаша почта для обратной связи и предложений:\ngleb.kak2@yandex.ru.\nМы в вк:\n@g.cheprasov. ')


# telefon
@dp.message_handler(commands=['number'])
async def NumberMTK(message: types.Message):
    await bot.send_message(message.from_user.id, 'Наш номер: +79646345553')


# @dp.message_handler(commands=['qa'])
# async def sQl(message: types.Message):
# await sqlite_db.sql_read(message)


# echo
#@dp.message_handler()
#async def echo_send(message: types.Message):
    #await message.answer('Я еще не знаю как ответить на эту команду')


def register_baza_client(dp: Dispatcher):
    dp.register_message_handler(CommandB, commands=['command'])
    dp.register_message_handler(Information, commands=['info'])
    dp.register_message_handler(AdressMTK, commands=['address'])
    dp.register_message_handler(ContactsMTK, commands=['contacts'])
    dp.register_message_handler(NumberMTK, commands=['number'])