# - *- coding: utf- 8 - *-
from aiogram import Dispatcher

from bot.middlewares.exists_user import ExistsUserMiddleware


# Подключение милдварей
def setup_middlewares(dp: Dispatcher):
    dp.middleware.setup(ExistsUserMiddleware())