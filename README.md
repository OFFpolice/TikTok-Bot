# TikTok Bot

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://t.me/OFFpoliceChannel) [![aiogram 2](https://img.shields.io/badge/aiogram-2-%234FC3F7)](https://docs.aiogram.dev/en/v2.25.1/) [![yt-dlp](https://img.shields.io/badge/yt--dlp-2024.5.27-%230077B5)](https://github.com/yt-dlp/yt-dlp)

## Обзор:
Этот Python-скрипт реализует телеграм-бота с использованием фреймворка [aiogram 2.25.1](https://docs.aiogram.dev/en/v2.25.1/) и библиотеки [yt-dlp](https://pypi.org/project/yt-dlp/) для загрузки видео с TikTok без водяных знаков. Бот предоставляет пользовательский интерфейс для взаимодействия со ссылками на видео TikTok в Telegram.

## Возможности:
- Команда `/start` для запуска бота и получения инструкций.
- Получить дополнительную помощь, используя инлайн-кнопку "🆘 Помощь".
- Загрузка видео после проверки подписки на Telegram канал.
- Загрузка видео TikTok без водяных знаков.
- Рандомные стикеры.

## Инструкция по использованию бота:
1. Запустите бот, используя команду `/start`.
2. Отправьте ссылку на видео из TikTok.
3. Получите дополнительную помощь, используя инлайн-кнопку "🆘 Помощь".

## Установка:
1. Установите необходимые зависимости: `aiogram`, `python-dotenv`, `yt-dlp`.
2. Настройте переменное окружения в файле `.env` с `channel_link`, `channel_id`, `bot_token`, `photo_link`, `video_link`.
3. Замените идентификаторы стикеров в файле random_id.py
4. **Обязательно добавьте бота в администраторы телеграм канала.**
5. Запустите скрипт 🤗🤗🤗🤗

- Перед тем, как начать работать с кодом бота убедитесь, что у вас установлена актуальная версия [yt-dlp](https://pypi.org/project/yt-dlp/), так как TikTok часто вносит изменения в API.
- Если видео не загружается попробуйте другую версию [бота](https://github.com/OFFpolice/TikTok-Bot-Local)!

## Отказ от ответственности:
- Соблюдайте авторские права и убедитесь, что у вас есть право загружать и распространять контент.
- Незаконная загрузка контента с нарушением авторских прав запрещена.

## Скриншоты:
- **Start**
![Alt text](https://github.com/OFFpolice/TikTok-Bot/blob/main/photo/start.jpg)

- **Help**
![Alt text](https://github.com/OFFpolice/TikTok-Bot/blob/main/photo/help.jpg)

- **Subscription**
![Alt text](https://github.com/OFFpolice/TikTok-Bot/blob/main/photo/subscription.jpg)

- **Subscription no**
![Alt text](https://github.com/OFFpolice/TikTok-Bot/blob/main/photo/subscription_no.jpg)

- **Subscription yes**
![Alt text](https://github.com/OFFpolice/TikTok-Bot/blob/main/photo/subscription_yes.jpg)

- **Downloads**
![Alt text](https://github.com/OFFpolice/TikTok-Bot/blob/main/photo/downloads.jpg)

- **Video**
![Alt text](https://github.com/OFFpolice/TikTok-Bot/blob/main/photo/downloads_video.jpg)

## Как связаться со мной:
- [![Telegram Badge](https://img.shields.io/badge/Telegram-blue?style=flat&logo=telegram&logoColor=white)](https://t.me/OFFpolice)
- [![Twitter Badge](https://img.shields.io/twitter/follow/:OFFpolice2077)](https://x.com/OFFpolice2077)

## Лицензия:
Этот проект лицензируется по лицензии GNU - более подробную информацию смотрите в файле [LICENSE](LICENSE).