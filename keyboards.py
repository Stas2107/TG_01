from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_main_keyboard(user_first_name: str) -> ReplyKeyboardMarkup:
    main = ReplyKeyboardMarkup(keyboard=[
       [KeyboardButton(text=f"Привет {user_first_name}")],
       [KeyboardButton(text=f"Пока {user_first_name}")]
    ], resize_keyboard=True)
    return main

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", callback_data='news')],
   [InlineKeyboardButton(text="Музыка", callback_data='music')],
   [InlineKeyboardButton(text="Видео", callback_data='video')]
])

def inline_dynamic_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data='show_more')]
    ])

test = ["Опция 1", "Опция 2"]

async def dinamic_keyboard():
    keyboard = InlineKeyboardBuilder()
    for i, key in enumerate(test, start=1):
        keyboard.add(InlineKeyboardButton(text=key, callback_data=f'option_{i}'))
    return keyboard.adjust(2).as_markup()
