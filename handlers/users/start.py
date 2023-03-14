import os

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from api_wb import get_keys_from_api
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start_no_state(message: types.Message):
    await message.answer('Привет!\n'
                         'Отправь мне артикул, а я тебе все запросы по ключевым')


@dp.message_handler()
async def get_keys(message: types.Message):
    if message.text.isdigit():
        await get_keys_from_api(message.text, message.from_user.id)
        file = open(f'key_data_{message.from_user.id}.txt', 'rb')
        await message.reply_document(file, caption='Собрал все ключевые слова по данному артикулу!')
        os.remove(f'key_data_{message.from_user.id}.txt')

    else:
        await message.answer('Кажется, это не артикул..')
