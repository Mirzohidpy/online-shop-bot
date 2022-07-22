from aiogram.dispatcher import FSMContext
from aiogram.types import ShippingQuery, PreCheckoutQuery
from loader import dp, bot
from shopping_config.product_invoice import *


@dp.shipping_query_handler()
async def choose_shipping(query: ShippingQuery):
    if query.shipping_address.country_code != 'UZ':
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=True, error_message="Yetkazib berish xizmati faqat O'zbekiston bo'ylab.")

    elif query.shipping_address.city.lower() in ['toshkent', 'tashkent', 'тошкент', 'ташкент']:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[EXPRESS_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    elif query.shipping_address.city.lower() not in ['toshkent', 'tashkent', 'тошкент', 'ташкент']:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGIONS_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def checkout(pre_checkout_query: PreCheckoutQuery, state: FSMContext):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True, error_message='Test')
    await bot.send_message(chat_id=pre_checkout_query.from_user.id, text='Xaridingiz uchun rahmat 😊.')
    data = await state.get_data()
    chat_id = pre_checkout_query.from_user.id
    customer_full_name = await db.user_info(chat_id=chat_id)
    created_order = await db.create_order(customer_full_name)
    order_id = created_order[0]
    data_order_item = [(product, data[product]['count'], int(float(data[product]['price'])), data[product]['total'], order_id)
                       for product in data]
    await db.create_order_item(data_order_item)
    await state.finish()

