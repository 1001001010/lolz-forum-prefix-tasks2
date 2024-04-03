from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.data.config import db

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
      kb.add(InlineKeyboardButton(btn['name'], callback_data=f"teacher:{btn['id']}"))
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