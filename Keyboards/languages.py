from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

languages = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="O'zbek")],
        [KeyboardButton(text="Ingliz")],
        [KeyboardButton(text="Rus")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)