from typing import Union

from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.private_chat import IsPrivate
from keyboards.inline.inline_menu import main_menu
from loader import dp, db


@dp.message_handler(IsPrivate(), CommandStart())
@dp.callback_query_handler(text='back_main')
async def bot_start(message: Union[Message, CallbackQuery]):
    chat_id = message.from_user.id
    await db.create_user(chat_id)
    user_status = await db.user_info(chat_id)
    if not user_status:
        await message.answer(f"Assalomu aleykum, Online Do'konga xush kelibsiz.\n\n"
                             f"Ro'yxatdan o'tish uchun /registration komandasini bosing.")
    else:
        if type(message) is Message:
            await message.answer(f"Online Do'konga xush kelibsiz.", reply_markup=main_menu)
        else:
            await message.answer()
            await message.message.edit_text(f"Online Do'konga xush kelibsiz.", reply_markup=main_menu)