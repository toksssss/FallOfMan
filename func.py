from aiogram import Router, F, types, Bot
from aiogram.filters.command import Command
import sqlite3

router = Router()

bot = Bot("7866181882:AAFs7qPHddmsRLCZEGWaKJ38VH5xYIBvZYQ")

con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, username TEXT,"
            " points INTEGER DEFAULT 0)")

@router.message(Command("start"))
async def cmd_start_command(message: types.Message):
    await message.answer("Добро пожаловать, юный ситх")

    res = cur.execute(f"SELECT NOT EXISTS (SELECT id FROM Users WHERE user_id='{message.from_user.id}')").fetchone()[0]
    if res:
        cur.execute(f"INSERT INTO Users (user_id, username) VALUES "
                    f"('{message.from_user.id}', "
                    f"'{message.from_user.username}')")
        con.commit()

@router.message(Command("add"))
async def cmd_add(message: types.Message):
    await message.answer("+1")

    cur.execute(f"UPDATE Users SET points = points + 1 WHERE user_id ='{message.from_user.id}'")
    con.commit()
    count = cur.execute(f"SELECT points FROM Users WHERE user_id = '{message.from_user.id}'").fetchone()[0]
    await telegram_noti(count, message.from_user.full_name)

async def telegram_noti(_count : int, _username : str) -> None:
    group_id = ""
    text = f"БУМ! {_username} имеет на счету {_count} очков! "
    await bot.send_message(chat_id=group_id, text=text)

async def discord_noti(_count : int, _username : str) -> None:
    return

async def send_noti(_count : int, _username : str) -> None:
    return

@router.message(Command("reset"))
async def cmd_reset(message: types.Message):
    cur.execute(f"UPDATE Users SET points = 0 WHERE user_id ='{message.from_user.id}'")
    con.commit()
    await message.answer("Поинты сброшены")
