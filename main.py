# Made by: @OFFpolice
import re
import os
import logging
import random
import asyncio
from dotenv import load_dotenv
from os.path import join, dirname
from random_id import sticker_id
from download import download_video
from aiogram import Bot, Dispatcher, executor, types

# Настройки логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="a",
    filename="run.log"
)

# Загрузка переменных из файла .env
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Получение значений переменных
channel_link = os.environ.get("channel_link")
channel_id = os.environ.get("channel_id")
photo_link = os.environ.get("photo_link")
video_link = os.environ.get("video_link")
bot_token = os.environ.get("bot_token")

# Инициализация бота и диспетчера
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
loop = asyncio.get_event_loop()

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    # Создание кнопки помощи
    markup = types.InlineKeyboardMarkup(row_width=1)
    help_button = types.InlineKeyboardButton("🆘 Помощь", callback_data="help")
    markup.add(help_button)
    # Отправка видео сообщения с кнопкой помощи
    await bot.send_video(
        chat_id=message.chat.id,
        video=video_link,
        caption = f"<b>Здравствуйте, {message.chat.first_name}!</b>\n\n<i>С помощью этого бота вы сможете скачивать видео с</i> <b>«TikTok»</b> <i>без водяного знака!</i>\n\n<i>Скопируйте ссылку на видео</i> <b>«TikTok»</b> <i>и пришлите мне!</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    # Удаление команды /start из чата
    await message.delete()

# Обработчик нажатия на кнопку помощи
@dp.callback_query_handler(lambda c: c.data == "help")
async def process_help_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # Создание кнопки "Назад"
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("🔙 Назад", callback_data="back")
    markup.add(back_button)
    # Редактирование сообщения с инструкциями по использованию бота
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption="<b>⁉️ Если вы хотите скачать видео с платформы «TikTok» без водяного знака, вам нужно будет следовать этой инструкции:</b>\n\n<b>1. Для этого откройте приложение «TikTok» найдите интересующее вас видео и нажмите кнопку «Поделиться».</b>\n<i>Затем выберите опцию «Копировать ссылку».</i>\n<b>2. Отправьте скопированную ссылку чат-боту.</b>\n<i>Вставьте ссылку в поле сообщения и отправьте боту.</i>\n<b>3. Бот обработает предоставленную ссылку и предоставит вам видео без водяного знака.</b>\n<b><i>Размер видео будет ограничен (20Мб)</i></b>.\n\n<b>Пример ссылки:</b>\n<code>https://vm.tiktok.com/ZM6LSsUHv/</code>\n\n<b>‼️ Обратите внимание, что загрузка контента, защищенного авторским правом, без разрешения является уголовным преступлением.\n‼️ Убедитесь, что вы загружаете только свой собственный контент или контент, на загрузку которого у вас есть разрешение.</b>\n\n<b>По всем вопросам:</b> <i>OFFpolice.t.me</i>",
        parse_mode="HTML",
        reply_markup=markup
    )

# Обработчик нажатия на кнопку "Назад"
@dp.callback_query_handler(lambda c: c.data == "back")
async def process_back_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # Создание кнопки помощи
    markup = types.InlineKeyboardMarkup(row_width=1)
    help_button = types.InlineKeyboardButton("🆘 Помощь", callback_data="help")
    markup.add(help_button)
    # Редактирование сообщения с приветствием
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=f"<b>Здравствуйте, {callback_query.from_user.first_name}!</b>\n\n<i>С помощью этого бота вы сможете скачивать видео с</i> <b>«TikTok»</b> <i>без водяного знака!</i>\n\n<i>Скопируйте ссылку на видео</i> <b>«TikTok»</b> <i>и пришлите мне!</i>",
        parse_mode="HTML",
        reply_markup=markup
    )

# Обработчик текстовых сообщений для скачивания видео
@dp.message_handler(content_types=["text"])
async def content_download(message: types.Message):
    # Проверка, что сообщение содержит ссылку на TikTok видео
    if re.compile("https://[a-zA-Z]+.tiktok.com/").match(message.text):
        # Проверка, что пользователь подписан на канал
        channel_member = await bot.get_chat_member(channel_id, message.chat.id)
        if channel_member.status == "left":
            # Если пользователь не подписан, отправка сообщения с предложением подписаться
            status_button = types.InlineKeyboardMarkup()
            status_button.add(
                types.InlineKeyboardButton(
                    text="Подписаться",
                    url=channel_link
                )
            )
            status_button.row(
                types.InlineKeyboardButton(
                    text="Проверка",
                    callback_data="check_subscription"
                )
            )
            # Отправка фото сообщения с предложением подписаться
            await bot.send_photo(
                chat_id=message.chat.id,
                photo=photo_link,
                caption="<b>🔒 Для доступа к функциям бота, подпишитесь на наш канал!\n\nПосле подписки вернитесь в диалог с ботом и нажмите кнопку «Проверка».\nЗатем повторите свой запрос!</b>",
                parse_mode="HTML",
                reply_markup=status_button
            )
            # Удаление сообщения с ссылкой на видео TikTok
            await message.delete()
            return
        try:
            # Отправка случайного стикера
            random_sticker = random.choice(sticker_id)
            message_sticker = await bot.send_sticker(
                chat_id=message.chat.id,
                sticker=random_sticker
            )
            # Отправка сообщения о начале загрузки видео
            processing = await bot.send_message(
                chat_id=message.chat.id,
                text=f"<b>Пожалуйста, подождите!\n<a href='{message.text}'>Видеоролик</a> загружается... ⌛️⏳⌛️⏳</b>",
                parse_mode="HTML"
            )
            # Загрузка видео и получение информации о нем
            video_url, likes, comments, repost, views, description, channel_url, channel_name, post_link = await download_video(message.text)
            # Создание URL кнопки с рекламной ссылкой которая будет отправлена вместе с видео
            url_button = types.InlineKeyboardMarkup()
            url_button.add(
                types.InlineKeyboardButton(
                    text="🌀 Shazam Bot",
                    url="https://telegram.me/OFFpoliceShazamBot?start=TikTokBot"
                )
            )
            # chat_action "отправляет видео"
            await bot.send_chat_action(
                message.chat.id,
                "upload_video"
            )
            # Отправка видео пользователю
            await bot.send_video(
                chat_id=message.chat.id,
                video=video_url,
                caption=f"{description}\n\n<b>👤 Автор:</b> <a href='{channel_url}'>{channel_name}</a>\n<b>👁 Просмотров:</b> <code>{views}</code>\n<b>❤️ Лайков:</b> <code>{likes}</code>\n<b>💬 Комментариев:</b> <code>{comments}</code>\n<b>🔁 Поделились:</b> <code>{repost}</code>\n<b>📹 Открыть в</b> <a href='{post_link}'>TikTok</a>\n\n<b>🆔: @SaveTikTokVideoBot</b>",
                parse_mode="HTML",
                reply_markup=url_button
            )
            # Удаление исходного сообщения и сообщений стикера и прогресса
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=message.message_id
            )
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=message_sticker.message_id
            )
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=processing.message_id
            )
        except Exception as e:
            # Обработка исключений и отправка сообщения об ошибке
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"<b>🛑 Ошибка скачивания!</b>\n\n<a href='{message.text}'>Этот видеоролик</a> недоступен. Попробуйте повторить запрос позже!\n\n<b>😵 Ошибка:</b> {e}\n\n<b>🔗 Ссылка на видео:</b>\n<code>{message.text}</code>",
                parse_mode="HTML"
            )
            # Логирование ошибки
            logging.error("Ошибка скачивания: %s", e)
            print(f"Ошибка скачивания: {e}")
            # Удаление исходного сообщения и сообщений стикера и прогресса
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=message.message_id
            )
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=message_sticker.message_id
            )
            await bot.delete_message(
                chat_id=message.chat.id,
                message_id=processing.message_id
            )
    else:
        # Если сообщение не содержит ссылку на TikTok, отправка сообщения с просьбой прислать ссылку
        message_tiktok = await bot.send_message(
            chat_id=message.chat.id,
            text="<b>Я вас не понимаю, пришлите мне 🔗ссылку на видео «TikTok»!</b>",
            parse_mode="HTML"
        )
        await message.delete()
        await asyncio.sleep(5)
        # Удаление сообщения с просьбой прислать ссылку через 5 секунд
        await bot.delete_message(
            chat_id=message.chat.id,
            message_id=message_tiktok.message_id
        )

# Обработчик нажатия на кнопку "Проверка" для проверки подписки
@dp.callback_query_handler(lambda query: query.data == "check_subscription")
async def check_subscription(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    try:
        # Проверка статуса подписки пользователя
        channel_member = await bot.get_chat_member(channel_id, user_id)
        if channel_member.status == "member":
            # Если пользователь подписан, отправка уведомления об успешной проверке
            await bot.answer_callback_query(
                callback_query.id,
                text="🟢 Теперь вы можете использовать бот!\n🥰 Спасибо что выбрали нас!\n\n😇 Пожалуйста повторите свой запрос:)",
                show_alert=True
            )
            # Удаление сообщения с предложением подписаться
            await bot.delete_message(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id
            )
        else:
            # Если пользователь не подписан, отправка уведомления о необходимости подписки
            await bot.answer_callback_query(
               callback_query.id,
               text="🔴 Вы не подписаны на телеграм канал!",
               show_alert=True
           )
    except Exception as e:
        # Обработка исключений и логирование ошибки
        logging.error(e)
        print(e)

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен!!!!")
    asyncio.run(executor.start_polling(dp, skip_updates=True))
