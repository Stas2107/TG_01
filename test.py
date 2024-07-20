import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
import random
import aiohttp
from gtts import gTTS
from googletrans import Translator
import os

from config import TOKEN, WEATHER


bot = Bot(token=TOKEN)
dp = Dispatcher()

translator = Translator()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветики, {message.from_user.first_name}!")



@dp.message()
async def translate_message(message: Message):
    translated_text = translator.translate(message.text, dest='en').text
    await message.answer(translated_text)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())