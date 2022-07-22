from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.inline_menu import show_card_btn, main_menu
from loader import db, dp


@dp.callback_query_handler(text='add_product')
async def add_product(call: CallbackQuery, state: FSMContext):
    product = call.message.text.split('\n')[0].strip()
    count = int(call.message.reply_markup.inline_keyboard[0][1].text)
    data = await db.get_price_by_id(product)
    price, product_id = data[0][0], data[0][1]
    await state.update_data({
        product: {
            'price': price,
            'count': count,
            'total': int(float(price)) * count,
            'product_id': product_id
        }
    })
    await call.answer("Mahsulot savatga qo'shildi!")


@dp.callback_query_handler(text=['show_card', 'shopping_card'])
async def show_products(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data:
        send_mess = ''
        product_data = {}
        n = 1
        for product in data:
            send_mess += f'{n}) {product}\n' \
                         f'{data[product]["price"]} * {data[product]["count"]} = {data[product]["total"]}\n\n' \
                         f'{"--" * 30}\n\n'
            product_data[product] = data[product]["product_id"]
            n += 1

        btn = await show_card_btn(product_data)

        await call.message.edit_text(send_mess, reply_markup=btn)
        await call.answer()
    else:
        await call.answer("Savat bo'sh❗")


@dp.callback_query_handler(text=['delete_' + str(i) for i in range(1,101)])
async def remove_product(call: CallbackQuery, state: FSMContext):
    product_id = int(call.data.split('delete_')[1])
    product_data = await db.get_product_by_id(product_id)
    product_name = product_data[1]
    data = await state.get_data()
    await state.finish()
    del data[product_name]
    if data:
        await state.update_data(data)
        send_mess = ''
        product_data = {}
        n = 1
        for product in data:
            send_mess += f'{n}) {product}\n' \
                         f'{data[product]["price"]} * {data[product]["count"]} = {data[product]["total"]}\n\n' \
                         f'{"--" * 30}\n\n'
            product_data[product] = data[product]["product_id"]
            n += 1

        btn = await show_card_btn(product_data)

        await call.message.edit_text(send_mess, reply_markup=btn)
        await call.answer()
    else:
        await call.answer("Savat tozalandi. Savat bo'sh❗")
        await state.finish()
        await call.message.edit_text("Bo'limlardan birini tanlang:", reply_markup=main_menu)

@dp.callback_query_handler(text='clear')
async def clear_card(call: CallbackQuery, state: FSMContext):
    await call.answer("Savat tozalandi. Savat bo'sh❗")
    await state.finish()
    await call.message.edit_text("Bo'limlardan birini tanlang:", reply_markup=main_menu)
