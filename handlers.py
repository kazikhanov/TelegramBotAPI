from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import keyboards as kb
from aiogram import Router
import CommandsText as text
router = Router()
import asyncio
from weather_api import main, temp




@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer(f'{text.weather_start_text}', parse_mode='Markdown', reply_markup=kb.main)

    @router.message(~Command(commands=["start", "help"]))
    async def cmd_city(message:Message):

        res = await main(message.text)
        await message.answer(res)


@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer(f'{text.weather_help_text}', parse_mode='Markdown')

@router.message(Command('temp'))
async def cmd_temp(message: Message):
    try:
        if message.text.split()[1]:

            res = await temp(message.text.split()[1])
            await message.answer(res)
    except IndexError:
        print(True)

@router.message(Command('news'))
async def cmd_news(message:Message):
    await message.answer(f'Новости')


@router.message(Command("now"))
async def cmd_now(message:Message):
    try:
        if message.text.split()[1]:
            res = await main(message.text.split()[1])
            await message.answer(res)
    except IndexError:
        print(
            True
        )