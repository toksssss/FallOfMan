import asyncio
import sys

from aiogram import Bot, Dispatcher
from aiogram.utils.token import TokenValidationError
from func import router as func_router
from func import con

async def main() -> None:
    dp = Dispatcher()
    dp.include_router(func_router)
    try:
        bot = Bot("7866181882:AAFs7qPHddmsRLCZEGWaKJ38VH5xYIBvZYQ")
    except TokenValidationError:
        print("Wrong Tokken")
        sys.exit()
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Программа завершила работу")
        con.close()

