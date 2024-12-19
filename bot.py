import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from service.spam import classify_message
from service.mwt import MWT

from config import BOT_TOKEN

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.chat_member
async def new_chat_member(message: types.Message):
    for member in message.new_chat_members:
        await message.answer(f'Добро пожаловать @{member.username}, веди себя прилично, не спамь и не флуди')

@MWT(timeout=60*60)
async def get_admin_ids(chat_id):
    """ Returns a list of admin IDs for a given chat. Results are cached for 1 hour. """
    return [admin.user.id for admin in await bot.get_chat_administrators(chat_id)]

@dp.message()
async def normal_message(message: types.Message):
    admin_ids = await get_admin_ids(message.chat.id)
    is_privileged = message.from_user.id in admin_ids or message.from_user.is_bot
    if is_privileged:
        print("🛑 Privileged user skipped")
        return
    result = await classify_message(message.text)
    if result:
        print(f"❌ Spam recognized: {message.text}")
        await message.delete()
        await kick_chat_member(message.chat.id, message.from_user.id)
        print(f"UID {message.from_user.id} kicked")


async def kick_chat_member(chat_id, user_id):
    await bot.ban_chat_member(chat_id, user_id)
    await bot.unban_chat_member(chat_id, user_id)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
