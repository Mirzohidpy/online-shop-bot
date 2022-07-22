from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import product_btn
from loader import dp, db


@dp.callback_query_handler(text=[str(i) for i in range(1, 101)])
async def product_info(call: CallbackQuery):
    product_id = int(call.data)
    data = await db.get_product_by_id(product_id)
    product_name = data[1]
    product_photo = data[2]
    product_desc = data[3]
    subcategory_id = str(data[4])
    product_price = data[5]
    btn = await product_btn(subcategory_id)
    await call.message.edit_text(f'<a href="{product_photo}"> {product_name} </a>\n\n'
                                 f'{product_desc}\n\n'
                                 f'Narxi: {product_price}', reply_markup=btn)
