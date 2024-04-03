from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.data.config import db

# Кнопка возврата в главное меню
def back_to_main_menu():
   keyboard = InlineKeyboardMarkup()
   kb = []
   kb.append(InlineKeyboardButton("В главное меню", callback_data="back_to_main_menu"))
   keyboard.add(kb[0])

   return keyboard

def main_menu():
   keyboard = InlineKeyboardMarkup()
   kb = []
   kb.append(InlineKeyboardButton("📅 Просмотреть Расписание", callback_data="check_schedule"))
   kb.append(InlineKeyboardButton("🆙 Обновить Расписание", callback_data="edit_schedule"))
   keyboard.add(kb[0])
   keyboard.add(kb[1])

   return keyboard