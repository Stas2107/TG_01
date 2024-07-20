import random
import os
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

# Инициализация бота
bot = Bot(token='YOUR_TOKEN_HERE')
dp = Dispatcher(bot)

@dp.message_handler(Command('training'))
async def training(message: Message):
    training_list = [
        "\nТренировка 1:\n1. Скручивания: 3 подхода по 15 повторений\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n3. Планка: 3 подхода по 30 секунд",
        "\nТренировка 2:\n1. Подъемы ног: 3 подхода по 15 повторений\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
        "\nТренировка 3:\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
    ]
    rand_tr = random.choice(training_list)
    await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")

    # Инициализация pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Установка скорости, 150 - обычная, можно менять

    # Выбор голоса (зависит от установленных голосов на вашей системе)
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'Russian' in voice.name:
            engine.setProperty('voice', voice.id)
            break

    # Сохранение аудио в файл
    engine.save_to_file(rand_tr, 'training.wav')
    engine.runAndWait()

    # Изменение скорости с помощью pydub
    audio = AudioSegment.from_wav('training.wav')
    audio = audio.speedup(playback_speed=1.5)  # Увеличение скорости на 1.5x
    audio.export('training_fast.mp3', format='mp3')

    # Отправка аудио в чат
    audio_file = FSInputFile('training_fast.mp3')
    await bot.send_audio(message.chat.id, audio_file)

    # Удаление временных файлов
    os.remove('training.wav')
    os.remove('training_fast.mp3')