from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

typ_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Serial")],
        [KeyboardButton(text="Kino")]
    ],
    resize_keyboard=True
)