import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
import random
import aiohttp
from gtts import gTTS


import os

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




@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile("TG02.pdf")
    await bot.send_document(message.chat.id, doc)


@dp.message(Command('training'))
async def training(message: Message):
   training_list = [
       "\nТренировка 1:\n1. Скручивания: 3 подхода по 15 повторений\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n3. Планка: 3 подхода по 30 секунд",
       "\nТренировка 2:\n1. Подъемы ног: 3 подхода по 15 повторений\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
       "\nТренировка 3:\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
   ]
   rand_tr = random.choice(training_list)
   await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")

   tts = gTTS(text=rand_tr, lang='ru')
   tts.save("training.ogg")
   audio = FSInputFile('training.ogg')
   await bot.send_voice(message.chat.id, audio)
   os.remove("training.ogg")



@dp.message(Command('video'))
async def video(message: Message):
    await bot.send.chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('video.mp4')
    await bot.send_video(message.chat.id, video)


@dp.message(Command('voice'))
async def voice(message: Message):
    await bot.send.chat_action(message.chat.id, 'record_voice')
    voice = FSInputFile("sample.ogg")
    await message.answer_voice(voice)


@dp.message(Command('audio'))
async def audio(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n /start\n /help\n /minitraining")
    audio = FSInputFile('sound2.mp3')
    await bot.send_audio(message.chat.id, audio)


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
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')

@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это круто!')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды: \n /start \n /help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветики, {message.from_user.first_name}!")



@dp.message()
async def start(message: Message):
    await message.send_copy(chat_id=message.chat.id)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())