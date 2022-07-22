from aiogram.types import CallbackQuery, InlineKeyboardButton
from loader import dp, db
from keyboards.inline.inline_menu import generate_menu


@dp.callback_query_handler(text=["tv", "audio", "photo_video",
                                 "noutbook", "monitor", "monoblok",
                                 "smartfon", "sm_gadjets", "washing_machine",
                                 "air_conditioner"])
async def products(call: CallbackQuery):
    await call.answer()
    subcategory_code = call.data
    product_list = await db.get_products(subcategory_code)
    back_subcategory_code = 'back_' + subcategory_code
    btn = await generate_menu(product_list)
    btn.insert(InlineKeyboardButton(text='🔙 Ortga', callback_data=back_subcategory_code))
    subcategory_name = await db.subcategory_name(subcategory_code)
    await call.message.edit_text(subcategory_name, reply_markup=btn)
