# - *- coding: utf- 8 - *-
import configparser
import asyncio
from datetime import datetime, timedelta

from bot.data.db import DB

# Создание экземпляра бд 
async def main_db():
    db = await DB()

    return db


loop = asyncio.get_event_loop()
task = loop.create_task(main_db())
db = loop.run_until_complete(task)

# Чтение конфига
read_config = configparser.ConfigParser()
read_config.read("settings.ini")

bot_token = read_config['settings']['token'].strip().replace(" ", "")  # Токен бота
path_database = "tgbot/data/database.db"  # Путь к Базе Данных

# Получение текущей даты
def get_date(date_type):
    if date_type == 'today':
        this_date = datetime.today().replace(microsecond=0)
    elif date_type == 'tomorrow':
        this_date = datetime.today() + timedelta(days=1)
        this_date = this_date.replace(microsecond=0)
    elif date_type == 'after_tomorrow':
        this_date = datetime.today() + timedelta(days=2)
        this_date = this_date.replace(microsecond=0)
    else:
        raise ValueError("Invalid date type")

    this_date = this_date.strftime("%d.%m.%Y")

    return this_date