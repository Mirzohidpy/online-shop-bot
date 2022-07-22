from aiogram.types import ShippingOption, LabeledPrice
from loader import db
from shopping_config.product_class import Product


def generate_product_invoice(product_data):
    query = Product(
        title='Shop Bot',
        description='\n'.join([title for title in product_data]),
        currency='UZS',
        prices=[
            LabeledPrice(
                label=f'{product_data[title]["count"]} ta {title}',
                amount=int(product_data[title]["count"]) * int(float(product_data[title]["price"])) * 100)
            for title in product_data
        ],
        start_parameter='create_invoice_products',
        need_name=True,
        need_phone_number=True,
        is_flexible=True
    )
    return query

EXPRESS_SHIPPING = ShippingOption(
    id='post_express',
    title='3 soat ichida',
    prices=[
        LabeledPrice('3 soat ichida', 2500000) # => 25 000.00 == 25000
    ]
)

REGULAR_SHIPPING = ShippingOption(
    id='post_regular',
    title='1 kunda yetazish',
    prices=[
        LabeledPrice('1 kunda yetazish', 1000000)
    ]
)

PICKUP_SHIPPING = ShippingOption(
    id='post_pickup',
    title="Do'kondan olib ketish",
    prices=[
        LabeledPrice("'Do'kondan olib ketish'", 0)
    ]
)

REGIONS_SHIPPING = ShippingOption(
    id='post_regions',
    title="O'zbekiston bo'ylab yetkazish",
    prices=[
        LabeledPrice("O'zbekiston bo'ylab yetkazish", 4000000)
    ]
)
