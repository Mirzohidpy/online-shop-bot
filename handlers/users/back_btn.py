from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import generate_menu
from loader import dp, db

subcategories = ["tv", "audio", "photo_video", "noutbook", "monitor", "monoblok", "smartfon", "sm_gadjets",
                 "washing_machine", "air_conditioner"]


@dp.callback_query_handler(text=['back_' + item for item in subcategories])
async def back_subcategories(call: CallbackQuery):
    subcategory_code = call.data.split('back_')[1]
    subcategory_list = await db.back_subcategories(subcategory_code)
    button = await generate_menu(subcategory_list, back_subcategories=True, subcategory_code=subcategory_code)
    await call.message.edit_text("Bo'limlardan birini tanlang: ", reply_markup=button)


@dp.callback_query_handler(text=['back_product_list_' + str(item) for item in range(1, 101)])
async def back_products(call: CallbackQuery):
    subcategory_code = int(call.data.split('back_product_list_')[1])
    subcategory_list = await db.back_product_list(subcategory_code)
    button = await generate_menu(subcategory_list, back_subcategories=True, subcategory_code=str(subcategory_code))
    await call.message.edit_text("Bo'limlardan birini tanlang: ", reply_markup=button)
