from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import generate_menu
from loader import dp, db


@dp.callback_query_handler(text=["tvtexno", "comp", "phone", "homeAppliances"])
async def categories(call: CallbackQuery):
    await call.answer()
    category_code = call.data
    subcategory_list = await db.get_subcategories(category_code)
    button = await generate_menu(subcategory_list, back_categories=True)
    category_name = await db.category_name(category_code)
    await call.message.edit_text(category_name, reply_markup=button)
