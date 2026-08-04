import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
TOKEN = "8887727104:AAF-WkVY-WdMglICBKftM5TtnmDCCgu0xK8

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    # Текст сообщения (использует HTML-разметку или Markdown)
    text = (
        "✈️ <b>Добро пожаловать на борт</b> — №1 лицензированная платформа с 15 000+ играми и спортом прямо в мессенджере!\n\n"
        "Забирай:\n"
        "🎁 <b>До 425%+250FS</b> в играх или до $1600 фрибетами в спорте.\n"
        "🎁 <b>Бездепозитный бонус</b> в Турбине.\n"
        "Удачи новым игрокам.\n"
        "💸 <b>Cashback до 10%</b> без вейджера.\n"
        "💸 <b>Депозитный бонус +5%</b> ежедневно.\n\n"
        "Всегда актуальное зеркало 👉 @your_channel"
    )

    # Создание кнопок под сообщением
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                # Кнопка, открывающая Web App (мини-приложение внутри телеграма)
                InlineKeyboardButton(
                    text="Играть в боте", 
                    web_app=WebAppInfo(url="https://your-website.com") 
                )
            ],
            [
                # Обычная кнопка-ссылка на сайт
                InlineKeyboardButton(
                    text="Играть на сайте", 
                    url="https://your-website.com" 
                )
            ],
            [
                # Кнопка-ссылка на сообщество/канал
                InlineKeyboardButton(
                    text="Сообщество", 
                    url="https://t.me/your_channel" 
                )
            ]
        ]
    )

    # Ссылка на картинку (можно заменить на прямую ссылку в интернете)
    photo_url = "https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=1000&auto=format&fit=crop"
    
    # Отправка фото с текстом и кнопками
    await message.answer_photo(
        photo=photo_url,
        caption=text,
        parse_mode="HTML", # Режим разметки (вместо Markdown лучше использовать HTML для надежности)
        reply_markup=keyboard
    )

# Главная функция для запуска бота
async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запущен и ожидает сообщения...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен.")
