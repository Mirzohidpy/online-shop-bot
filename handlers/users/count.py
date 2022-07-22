from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import product_btn
from loader import db, dp


@dp.callback_query_handler(text='plus')
async def increment(call: CallbackQuery):
    count = int(call.message.reply_markup.inline_keyboard[0][1].text)
    subcategory_id = call.message.reply_markup.inline_keyboard[2][0].callback_data.split('back_product_list_')[1]
    count += 1
    btn = await product_btn(subcategory_id, count)
    await call.message.edit_reply_markup(reply_markup=btn)
    await call.answer(cache_time=2)


@dp.callback_query_handler(text='minus')
async def decrement(call: CallbackQuery):
    count = int(call.message.reply_markup.inline_keyboard[0][1].text)
    subcategory_id = call.message.reply_markup.inline_keyboard[2][0].callback_data.split('back_product_list_')[1]
    if count > 1:
        count -= 1
        btn = await product_btn(subcategory_id, count)
        await call.message.edit_reply_markup(reply_markup=btn)
    await call.answer(cache_time=2)
