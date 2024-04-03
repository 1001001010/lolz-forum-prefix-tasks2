# - *- coding: utf- 8 - *-
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update
from loguru import logger

class ExistsUserMiddleware(BaseMiddleware):

    def __init__(self):
        super(ExistsUserMiddleware, self).__init__()

    async def on_process_update(self, update: Update, data: dict):
        user = update
        if "message" in update:
            user = update.message.from_user
            logger.info(f"{user.full_name} - {update.message.text}")
        elif "callback_query" in update:
            user = update.callback_query.from_user
            logger.info(f"{user.full_name} - {update.callback_query.data} (Callback)")