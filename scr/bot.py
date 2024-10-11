import asyncio
import logging
from scr.handlers import states

from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from background import keep_alive

from aiogram_dialog import DialogManager, StartMode, ShowMode, setup_dialogs

from scr.handlers.start import main_dialog, help_dialog
from scr.handlers.commands import router as command_router
from scr.handlers.menu import router as menu_router

keep_alive()


async def start(message: Message, dialog_manager: DialogManager):
    # it is important to reset stack because user wants to restart everything
    await dialog_manager.start(
        states.Main.MAIN,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.SEND,
    )

dialog_router = Router()

dialog_router.include_routers(command_router, menu_router, main_dialog, help_dialog)


def setup_dp():
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.message.register(start, F.text == "/start", F.chat.type == "private")
    dp.business_message.register(start, F.text == "/start", F.chat.type == "private")
    dp.include_router(dialog_router)
    setup_dialogs(dp)
    return dp


async def main():
    # real main
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token="6723563813:AAFXjEuN6-a4GRutZpblbBZqCQGQCKaZ6gI")
    dp = setup_dp()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
