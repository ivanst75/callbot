from telethon import TelegramClient
from config import api_id, api_hash, BOT_TOKEN

# Создание клиента
client = TelegramClient('session_name', api_id, api_hash)


async def get_chat_members(chat_id):
    # Старт клиента с использованием bot_token
    await client.start(bot_token=BOT_TOKEN)

    # Получение участников чата
    chat_members = []
    async for member in client.iter_participants(chat_id):
        chat_members.append(member.username)

    # Отключение клиента после завершения работы
    await client.disconnect()
    return chat_members
