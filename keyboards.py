from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def create_main_keyboard(user_first_name: str) -> ReplyKeyboardMarkup:
    main = ReplyKeyboardMarkup(keyboard=[
       [KeyboardButton(text=f"Привет {user_first_name}")],
       [KeyboardButton(text=f"Пока {user_first_name}")]
    ], resize_keyboard=True)
    return main

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
   [InlineKeyboardButton(text="Новости", callback_data='news')],
   [InlineKeyboardButton(text="Профиль", callback_data='person')]
])

test = ["кнопка 1", "кнопка 2", "кнопка 3", "кнопка 4"]

async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key, url='https://www.youtube.com'))
    return keyboard.adjust(2).as_markup()