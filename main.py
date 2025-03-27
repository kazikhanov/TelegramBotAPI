from aiogram import Bot, Dispatcher
import asyncio
from config import TOKEN
from handlers import router

bot = Bot(token=TOKEN)
db = Dispatcher()

async def main():
    db.include_router(router)
    await db.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())