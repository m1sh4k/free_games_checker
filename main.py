from checker import *

import asyncio
import json

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

config = json.load(open('config.json'))
bot_token = config['bot_token']

bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Здарова, заебал!")

@dp.message(Command("goida!"))
async def cmd_goida(message: Message):
    await message.reply('💤')

@dp.message(Command('steam'))
async def cmd_steam(message: Message):
    games = parse_steam()
    if games:
        for i in games:
            await message.answer(text=i.build_message(), parse_mode=ParseMode.HTML)
    else:
        await message.answer('Пароварка пуста 😒💨')
    #await message.answer('фича пока в разработке!')

@dp.message(Command('gog'))
async def cmd_gog(message: Message):
    games = parse_gog()
    if games:
        for i in games:
            await message.answer(text=i.build_message(), parse_mode=ParseMode.HTML)
    else:
        await message.answer('GOG — жмот! 💔')

@dp.message(Command('egs'))
async def cmd_egs(message: Message):
    games = parse_egs()
    if games:
        for i in games:
            #await message.answer(text = f"<strong>{i[0]}</strong>\n\n{i[1]}\n{i[2]}", parse_mode=ParseMode.HTML)
            await message.answer(text=i.build_message(), parse_mode=ParseMode.HTML)
    else:
        await message.answer('В Epic Games Store ничего не раздают 🙁')

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


