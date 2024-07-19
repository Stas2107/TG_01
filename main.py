import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random
import aiohttp

from config import TOKEN, WEATHER


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=['weather']))
async def weather(message: Message):
    weather_info = await get_weather()
    await message.answer(weather_info)

async def get_weather():
    City = 'Moscow'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid={WEATHER}&units=metric&lang=ru"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            description = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            return f"Погода в Москве: {description}\nТемпература: {temp}°C\nОщущается как: {feels_like}°C"





@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://balthazar.club/o/uploads/posts/2024-01/1705309704_balthazar-club-p-samii-krasivii-malenkii-kotenok-oboi-75.jpg',
            'https://www.zastavki.com/pictures/originals/2018Animals___Cats_Large_gray_cat_with_a_surprised_look_123712_.jpg']
    rand_photo = random.choice(list)
    await message.reply_photo(photo=rand_photo, caption='Это супер крутая картинка')

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это круто!')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды: \n /start \n /help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())