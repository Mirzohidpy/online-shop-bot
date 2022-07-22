from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

phone_number_btn = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Raqam bilan ulashish 📱", request_contact=True)],
    ]
)