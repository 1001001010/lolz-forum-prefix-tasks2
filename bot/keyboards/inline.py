from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.data.config import db, get_date

# Кнопка возврата в главное меню
def kb_back_to_main_menu():
   keyboard = InlineKeyboardMarkup()
   kb = []
   kb.append(InlineKeyboardButton("🔙 В главное меню", callback_data="back_to_main_menu"))
   keyboard.add(kb[0])

   return keyboard

def kb_main_menu():
   keyboard = InlineKeyboardMarkup()
   kb = []
   kb.append(InlineKeyboardButton("📅 Просмотреть расписание", callback_data="check_schedule"))
   kb.append(InlineKeyboardButton("🆙 Обновить расписание", callback_data="edit_schedule"))
   keyboard.add(kb[0])
   keyboard.add(kb[1])

   return keyboard

def kb_edit_shedule():
   keyboard = InlineKeyboardMarkup()
   kb = []
   kb.append(InlineKeyboardButton("✏️ Изменить расписание", callback_data="change_schedule"))
   kb.append(InlineKeyboardButton("📅 Заполнить расписание", callback_data="fill_schedule"))
   kb.append(InlineKeyboardButton("💼 Предмемы", callback_data="subjects_menu"))
   kb.append(InlineKeyboardButton("👨‍🏫 Преподаватели", callback_data="teacher_menu"))
   kb.append(InlineKeyboardButton("🔙 Назад", callback_data="back_to_main_menu"))
   keyboard.add(kb[0])
   keyboard.add(kb[1])
   keyboard.add(kb[2], kb[3])
   keyboard.add(kb[4])
   
   return keyboard

async def kb_teacher():
   keyboard = InlineKeyboardMarkup()
   kb = []
   list = await db.get_all_teachers()
   for btn in list:
      keyboard.add(InlineKeyboardButton(btn['name'], callback_data=f"teacher_info:{btn['id']}"))
   kb.append(InlineKeyboardButton("➕ Добавить учителя", callback_data="add_teacher"))
   kb.append(InlineKeyboardButton("🔙 Назад", callback_data="back_to_main_menu"))
   keyboard.add(kb[1], kb[0])
   
   return keyboard

async def kb_subjects(page=1):
   keyboard = InlineKeyboardMarkup()
   kb = []
   list = await db.get_all_subjects(page)
   for btn in list:
      keyboard.add(InlineKeyboardButton(btn['name'], callback_data=f"teacher:{btn['id']}"))
   if page > 1:
      kb.append(InlineKeyboardButton("◀️ Предыдущая", callback_data=f"prev_page:{page - 1}"))
   if len(list) == 10:
      kb.append(InlineKeyboardButton("▶️ Следующая", callback_data=f"next_page:{page + 1}"))
   keyboard.add(*kb)
   list_kb = [
      InlineKeyboardButton("➕ Добавить предмет", callback_data=f"add_subjects"),
      InlineKeyboardButton("🔍 Поиск", callback_data=f"search_subject"),
      InlineKeyboardButton("🔙 Главное меню", callback_data="back_to_main_menu")
   ]
   keyboard.add(list_kb[0], list_kb[1])
   keyboard.add(list_kb[2])

   return keyboard
 
#Поиск
async def seach_list_kb(table, word):
   kb = InlineKeyboardMarkup()
   list = await db.search_by_word(table=table, word=word)
   for btn in list:
      kb.add(InlineKeyboardButton(f"{btn['name']}", callback_data=f"one_{table}:{btn['id']}"))
   kb.add(InlineKeyboardButton("Назад", callback_data=f"back_to_main_menu"))

   return kb

async def kb_subjects_for_prep(page=1):
   keyboard = InlineKeyboardMarkup()
   kb = []
   list = await db.get_all_subjects(page)
   for btn in list:
      keyboard.add(InlineKeyboardButton(btn['name'], callback_data=f"subj_for_prep:{btn['id']}"))
   if page > 1:
      kb.append(InlineKeyboardButton("◀️ Предыдущая", callback_data=f"prev_page:{page - 1}"))
   if len(list) == 10:
      kb.append(InlineKeyboardButton("▶️ Следующая", callback_data=f"next_page:{page + 1}"))
   keyboard.add(*kb)
   list_kb = [
      InlineKeyboardButton("➕ Добавить предмет", callback_data=f"add_subjects"),
      InlineKeyboardButton("🔍 Поиск", callback_data=f"search_subject"),
      InlineKeyboardButton("🔙 Главное меню", callback_data="back_to_main_menu")
   ]
   keyboard.add(list_kb[0], list_kb[1])
   keyboard.add(list_kb[2])

   return keyboard

def kb_date():
   kb = InlineKeyboardMarkup()
   kb.add(InlineKeyboardButton(f"{get_date('today')}", callback_data=f"date_{get_date('today')}"))
   kb.add(InlineKeyboardButton(f"{get_date('tomorrow')}", callback_data=f"date_{get_date('tomorrow')}"))
   kb.add(InlineKeyboardButton(f"{get_date('after_tomorrow')}", callback_data=f"date_{get_date('after_tomorrow')}"))
   kb.add(InlineKeyboardButton("Назад", callback_data=f"back_to_main_menu"))
   return kb

async def kb_shedule(date):
   keyboard = InlineKeyboardMarkup()
   kb = []
   list = await db.get_shedule(date)
   for btn in list:
      subj = await db.get_subject_info(btn['subject_id'])
      keyboard.add(InlineKeyboardButton(f"{subj['name']} | Каб. {btn['classroom_id']}", callback_data=f"shedule:{btn['id']}"))
   kb.append(InlineKeyboardButton("➕ Назначить урок", callback_data="add_shedule"))
   kb.append(InlineKeyboardButton("🔙 Назад", callback_data="back_to_main_menu"))
   keyboard.add(kb[1], kb[0])
   
   return keyboard