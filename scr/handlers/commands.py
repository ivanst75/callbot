from aiogram import F, Router
from aiogram.types import Message
from scr.getter import get_chat_members
from aiogram.filters import Command

router = Router(name=__name__)


@router.message(F.text, Command("all"))
async def cmd_all(message: Message):
    members = await get_chat_members(chat_id=message.chat.id)

    # Идентификатор вызывающего пользователя
    caller_id = message.from_user.username

    # Идентификатор бота
    bot_id = (await message.bot.get_me()).username

    # Создаем список с именами пользователей, добавляя префикс @, исключая вызывающего и бота
    filtered_members = [
        f"@{member}" for member in members
        if member != caller_id and member != bot_id
    ]

    # Объединяем элементы списка в одну строку
    members_str = " ".join(filtered_members)

    # Отправляем сообщение со списком упомянутых участников
    await message.answer(members_str, parse_mode="HTML")
