# pip3 install aiogram
from aiogram import Bot,Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from aiogram.types import ContentTypes
from config import TOKEN
import logging
from pathlib import Path

BOT_DIR = Path(__file__).resolve().parent
STICKERS_DIR: Path = BOT_DIR / "stickers"
STICKERS_DIR.mkdir(exist_ok=True)

logging.basicConfig(level=logging.DEBUG)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

logging_middleware = LoggingMiddleware()
dp.middleware.setup(logging_middleware)

@dp.message_handler()
async def echo_message(message: types.Message):
    # await bot.send_message()
    return await message.answer(message.text)
    # return await message.answer(message.chat.id)
    # return await message.answer('Товарищ майор прочитал: '+(message.text))

@dp.message_handler(content_types=ContentTypes.PHOTO)
async def echo_foto(message: types.Message):
    return await message.answer_photo(
        message.photo[-1].file_id,
        caption=f"Вы написали: {message.caption!r}",

    )

@dp.message_handler(content_types=ContentTypes.STICKER | ContentTypes.ANIMATION)
async def forward_any_sticker(message: types.Message):
    file_id = message.sticker.file_id
    await bot.download_file_by_id(
        file_id = file_id,
        destination= STICKERS_DIR / f"sticker_{file_id}.{'TGS' if message.sticker.is_animated else 'webp'}",
    )
    return await message.forward(message.chat.id)




if __name__ == '__main__':
    print("Bot token:", TOKEN)
    executor.start_polling(dp)