from aiogram import types
from create_bot import bot, Dispatcher
from settings.consts import USER_START_TEXT, USER_WAIT_TEXT
from parser.qiwi_parser import get_name
from database.database import insert


async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=USER_START_TEXT)
    

async def phone_number_message(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=USER_WAIT_TEXT)
    
    only_num_mess = ''.join(filter(lambda x: x.isdigit(), message.text))
    
    # получение имени пользователя
    owner = get_name(only_num_mess)
    
    await bot.send_message(chat_id=message.from_user.id, text=owner)
    
    await bot.send_message(chat_id=message.from_user.id, text=USER_START_TEXT)
    
    # запись данных в базу
    insert(only_num_mess, owner)
    
    
def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(phone_number_message, content_types=['text'])