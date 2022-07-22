from aiogram.types import CallbackQuery
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from shopping_config.product_invoice import generate_product_invoice


@dp.callback_query_handler(text='order')
async def order_invoice(call: CallbackQuery, state: FSMContext):
    product_data = await state.get_data()
    chat_id = call.from_user.id
    await bot.send_invoice(chat_id=chat_id, **generate_product_invoice(product_data).generate_invoice(), payload='shop_bot')
    await call.answer()
