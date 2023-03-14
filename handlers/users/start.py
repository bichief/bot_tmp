from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp
from utils.db_api.db_commands import select_client, create_client


@dp.message_handler(CommandStart())
async def bot_start_no_state(message: types.Message):
    await message.answer('Привет!')