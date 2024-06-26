import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
import commands


load_dotenv()
# session = AiohttpSession()
bot = Bot(os.getenv("BOT_TOKEN"))
storage = MemoryStorage()
dispatcher = Dispatcher(storage=storage)
dispatcher.callback_query.middleware(CallbackAnswerMiddleware())

async def main():
    dispatcher.include_router(router=commands.router)
    # dispatcher.include_router(router=callbacks.router)
    await bot.set_my_commands(commands.commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())