import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
import random

logger = logging.getLogger(__name__)


async def main():

    logging.basicConfig(
        level = logging.INFO,
        format = u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    
    
    logger.info("Starting bot")

    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    with open("Compliment_Bot\complimets.txt", "r", encoding="utf-8") as f:
        compliments = f.readlines()

    @dp.message_handler(content_types=(types.ContentTypes.PHOTO | types.ContentTypes.VIDEO | types.ContentTypes.VIDEO_NOTE))
    async def compliment(message: types.Message):
        await bot.send_message(
            message.from_user.id,
            text=random.choice(compliments),
        )
        

    try: 
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

