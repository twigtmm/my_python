from telethon.network.connection import ConnectionTcpMTProxyRandomizedIntermediate
from telethon import TelegramClient, events

from faces import detect_faces_and_predict_age_and_gender
from wide_resnet import WideResNet
from utils import *

import numpy as np
import dlib  # библиотека для поиска лиц
import cv2  # библиотека для работы с изображениями

import asyncio
import os

WEIGHTS_FILE = 'models/weights.hdf5'

# создаем детектор лиц и описываем модель
detector = dlib.get_frontal_face_detector()
model = WideResNet(64, depth=16, k=8)()
model.load_weights(WEIGHTS_FILE)


async def main():
    # создаем конфиг с параметрами
    config = Config('config.json')

    bot = TelegramClient(f'sessions/bot_{config.NAME}', config.api_id, config.api_hash,
                         connection=ConnectionTcpMTProxyRandomizedIntermediate,
                         proxy=config.proxy)

    # Встречаем пользователя с небольшой инструкцией по применению
    @bot.on(events.NewMessage(incoming=True, pattern='/start'))
    async def start_handler(event: events.NewMessage.Event):
        await event.respond(f'Привет! Пришли мне фотографию с людьми и я попробую предсказать их пол и возраст.\n'
                            f'Я не идеален, поэтому все совпадения случайны')
        raise events.StopPropagation()

    @bot.on(events.NewMessage(incoming=True))
    async def photo_handler(event: events.NewMessage.Event):
        # функция для предобработки фотографии такого же размера
        def preprocess_photo(photo):
            np_arr = np.frombuffer(photo, np.uint8)
            cv2_img = cv2.imdecode(np_arr, 1)
            h, w, _ = cv2_img.shape
            r = 640 / max(w, h)

            resized = cv2.resize(cv2_img, (int(w * r), int(h * r)))
            return resized

        # бот принимает только фотографии
        if event.message.photo:
            # скачиваем фото
            photo = await bot.download_file(event.message.photo)
            # предобрабатываем
            resized_photo = preprocess_photo(photo)
            # детектим лица, а затем нейронкой детектим пол и возраст
            result = detect_faces_and_predict_age_and_gender(resized_photo, detector, model)

            if not result:
                # нет лиц- просим другую фотографию
                await event.respond('Лица не найдены, попробуй другую фотографию')
            else:
                # нашли лица, задетектили пол и возраст, отправляем обратно
                await bot.send_file(event.chat, file=result)
                # удаляем распознанное фото
                os.remove(result)
        else:
            # если присланное сообщение- не фотография
            await event.respond('Мне нужна фотография')

    await bot.start(bot_token=config.TOKEN)

    # постоянная работа
    await bot.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
