from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command

from filters import IsPrivate
from keyboards.default.default_menu import phone_number_btn
from keyboards.inline.inline_menu import main_menu
from loader import dp, db
from states.register_state import RegisterState

@dp.message_handler(Command('registration'), IsPrivate(),state=None)
async def start_register(msg: Message):
    chat_id = msg.from_user.id
    user_status = await db.user_info(chat_id)
    if not user_status:
        await msg.answer("Ro'yxatdan o'tish uchun Ism va Familiyangizni kiriting: ")
        await RegisterState.full_name.set()

        

@dp.message_handler(state=RegisterState.full_name)
async def register_full_name(msg: Message, state: FSMContext):
    full_name = msg.text
    await state.update_data({'full_name': full_name})
    await msg.answer('Telefon raqamingizni kiriting: ', reply_markup=phone_number_btn)
    await RegisterState.phone_number.set()


@dp.message_handler(content_types='contact', state=RegisterState.phone_number)
async def register_phone_number(msg: Message, state: FSMContext):
    chat_id = msg.from_user.id
    data = await state.get_data()
    full_name = data['full_name']
    phone_number = msg.contact.phone_number
    await db.update_user(full_name, phone_number, chat_id)
    await state.finish()
    await msg.answer("Siz ro'yxatdan o'tdingiz 😊😊😊 ✅", reply_markup=ReplyKeyboardRemove())
    await msg.answer(f"Online Do'konga xush kelibsiz.", reply_markup=main_menu)