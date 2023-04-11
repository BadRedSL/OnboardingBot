import os

import dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import BotCommand

dotenv.load_dotenv(dotenv.find_dotenv())


class OnboardBot:
    __bot: Bot = Bot(token=os.getenv('TOKEN'))
    __storage: MemoryStorage = MemoryStorage()
    __dp: Dispatcher = Dispatcher(__bot, storage=__storage)

    @classmethod
    def get_dp(cls) -> Dispatcher:
        return cls.__dp
