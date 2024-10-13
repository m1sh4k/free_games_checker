from steamchecker import *
from egs_checker import *

import asyncio
import json

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, html
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.formatting import Text
from aiogram.utils.formatting import Bold

config = json.load(open('config.json'))
bot_token = config['bot_token']

bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_steam(message: Message):
    await message.answer("Здарова, заебал!")

@dp.message(Command('check_steam'))
async def cmd_start(message: Message):
    await message.answer('development in progress...')

@dp.message(Command('check_egs'))
async def cmd_egs(message: Message):
    games = check_egs()
    msg = []
    for i in games:
        #msg.append([Bold(i[0]), '\n\n' + i[1] + '\n' + i[2]])
        
        await message.answer(text = f"<strong>{i[0]}</strong>\n\n{i[1]}\n{i[2]}", parse_mode=ParseMode.HTML)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

'''
try:
    print(check_steam())
except Exception as e:
    print(f'Unable to connect steam servers, exception: {e}')

try:
    print(check_egs())
except Exception as e:
    print(f'Unable to connect steam servers, exception: {e}')
'''


