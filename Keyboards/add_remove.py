from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

admin_key = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="add_movie")],
        [KeyboardButton(text="remove_movie")]
    ],
    resize_keyboard=True,
)