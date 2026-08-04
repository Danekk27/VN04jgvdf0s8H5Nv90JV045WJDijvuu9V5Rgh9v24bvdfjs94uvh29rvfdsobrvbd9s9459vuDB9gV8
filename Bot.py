import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)

TOKEN = "8887727104:AAF-WkVY-WdMglICBKftM5TtnmDCCgu0xK8"

SITE_URL = "https://danekk27.github.io/VN04jgvdf0s8H5Nv90JV045WJDijvuu9V5Rgh9v24bvdfjs94uvh29rvfdsobrvbd9s9459vuDB9gV8/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    text = (
        "🎰 <b>Лицензированная платформа с 15 000+ играми и спортом прямо в мессенджере!</b>\n\n"
        "Забирай:\n"
        "🎁 <b>До 425%+250FS</b> в играх или до $1600 фрибетами в спорте.\n"
        "🎁 <b>Бездепозитный бонус</b> в Турбине Удачи новым игрокам.\n"
        "💸 <b>Cashback до 10%</b> без вейджера.\n"
        "💸 <b>Депозитный бонус +5%</b> ежедневно.\n\n"
        "Всегда актуальное зеркало 👉 @jetton"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎮 Играть в боте",
                    web_app=WebAppInfo(url=SITE_URL)
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌐 Играть на сайте",
                    url=SITE_URL
                )
            ],
            [
                InlineKeyboardButton(
                    text="👥 Сообщество",
                    url=SITE_URL
                )
            ]
        ]
    )

    # Замени на ссылку своей картинки после загрузки в репозиторий
    photo_url = "https://danekk27.github.io/VN04jgvdf0s8H5Nv90JV045WJDijvuu9V5Rgh9v24bvdfjs94uvh29rvfdsobrvbd9s9459vuDB9gV8/banner.jpg"

    await message.answer_photo(
        photo=photo_url,
        caption=text,
        parse_mode="HTML",
        reply_markup=keyboard
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен.")
