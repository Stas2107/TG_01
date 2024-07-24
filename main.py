import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import TOKEN
import keyboards as kb


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text.startswith("Links"))
async def greet_button(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}!')

@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
    await callback.answer("Новости подгружаются", show_alert=True)
    await callback.message.edit_text('Вот свежие новости!', reply_markup=await kb.test_keyboard())

@dp.message(F.text.startswith("Привет"))
async def greet_button(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}!')

@dp.message(CommandStart())
async def start(message: Message):
    reply_markup = kb.create_main_keyboard(message.from_user.first_name)
    await message.answer(f"Приветики, {message.from_user.first_name}!", reply_markup=reply_markup)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())