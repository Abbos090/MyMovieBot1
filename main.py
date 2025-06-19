import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from config import TOKEN
from Handlers.admin import router as admin_router
from Handlers.users import router as user_router
from Handlers.admin_serial import router as serial_router
from Handlers.admin_kino import router as kino_router


dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(admin_router)
    dp.include_router(serial_router)
    dp.include_router(kino_router)
    dp.include_router(user_router)
    # init_data_file()

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())