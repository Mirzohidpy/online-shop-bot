from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from filters import IsPrivate
from loader import dp, db


@dp.message_handler(Command('update'), IsPrivate())
async def bot_start(message: types.Message):
    await message.answer('Uy ishi')