from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🛍 Kataloglar', callback_data='categories'), ],
        [InlineKeyboardButton(text='🛒 Savat', callback_data='shopping_card'), ],
        [InlineKeyboardButton(text='👤 Mening profilim', callback_data='my_account'), ],
    ]
)


async def generate_menu(data_list, back_main=False, back_categories=False, back_subcategories=False,
                        subcategory_code=None):
    btn = InlineKeyboardMarkup(row_width=1)

    for inner_data in data_list:
        btn.insert(InlineKeyboardButton(text=inner_data[0], callback_data=str(inner_data[1])))

    if back_main:
        btn.insert(InlineKeyboardButton(text='🔙 Ortga', callback_data='back_main'))
    elif back_categories:
        btn.insert(InlineKeyboardButton(text='🔙 Ortga', callback_data='back_categories'))
    elif back_subcategories:
        btn.insert(InlineKeyboardButton(text='🔙 Ortga', callback_data='back_' + subcategory_code))

    return btn


async def product_btn(subcategory_id, count=None):
    button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='➖', callback_data='minus'),
                InlineKeyboardButton(text=count if count else '1', callback_data='count'),
                InlineKeyboardButton(text='➕', callback_data='plus'),
            ],
            [
                InlineKeyboardButton(text="Savatga qo'shish 🛍", callback_data='add_product'),
                InlineKeyboardButton(text="Savatni ko'rish 🛒", callback_data='show_card'),
            ],
            [
                InlineKeyboardButton(text='🔙 Ortga', callback_data='back_product_list_' + subcategory_id)
            ]
        ]
    )
    return button


async def show_card_btn(product_data):
    button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🛍 Buyurtma berish', callback_data='order'),
                InlineKeyboardButton(text='🔙 Bosh menu', callback_data='back_main')
            ],
            [
                InlineKeyboardButton(text=f"❌ {key}", callback_data=f'delete_{product_data[key]}') for key in product_data
            ],
            [
                InlineKeyboardButton(text='🛒 Savatni tozalash', callback_data='clear')
            ]
        ]
    )
    return button


async def delete_button(data):
    btn = InlineKeyboardMarkup(row_width=1)

    for product in data:
        btn.insert(InlineKeyboardButton(text=f"{product}", callback_data='delete_'+data[product]['id']))


    btn.insert(InlineKeyboardButton(text='Bosh sahifa', callback_data='back_main'))
    btn.insert(InlineKeyboardButton(text='🛍Buyurtma berish', callback_data='order'))
    btn.insert(InlineKeyboardButton(text='🔙 Ortga', callback_data='show_card'))

    return btn
