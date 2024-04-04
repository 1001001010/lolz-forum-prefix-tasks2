from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.data.config import db
from bot.keyboards.inline import kb_teacher, kb_subjects_for_prep, kb_back_to_main_menu
from bot.states.teachers import New_teacher

#открытие списка учителей
@dp.callback_query_handler(text="teacher_menu", state="*")
async def func_list_teachers(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"Выберите нужную функцию", reply_markup=await kb_teacher())
    
#Добавление учителя
@dp.callback_query_handler(text="add_teacher", state="*")
async def func_list_teachers(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"Укажите ФИО преподавателя:", reply_markup=kb_back_to_main_menu())
    await New_teacher.full_name.set()

#Получение ФИО преподавателя
@dp.message_handler(state=New_teacher.full_name)
async def func_new_book_new_genre(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await bot.send_message(message.from_user.id, "Выберите предмет, который преподаватель будет вести", reply_markup=await kb_subjects_for_prep())
    await New_teacher.subject.set()
    
#Добавление преподавателя в бд
@dp.callback_query_handler(text_startswith="subj_for_prep", state=New_teacher.subject)
async def func_new_book_to_db(call: CallbackQuery, state: FSMContext):
    subj_id = call.data.split(":")[1]
    await state.update_data(subject=subj_id)
    await call.message.delete()
    data = await state.get_data()
    await db.new_prepod(name = data['full_name'], subject = data['subject'], status = True)
    await call.message.answer("Преподаватель успешно добавлен", reply_markup=kb_back_to_main_menu())
    await state.finish()
    
@dp.callback_query_handler(text_startswith="teacher_info")
async def func_new_book_to_db(call: CallbackQuery, state: FSMContext):
    teacher_id = call.data.split(":")[1]
    await call.message.delete()
    data = await state.get_data()
    info = await db.get_teacher_info(id=teacher_id)
    subject = await db.get_subject_info(subj_id=info['subject'])
    if info['status'] == True:
        status = 'Работает'
    elif info['status'] == False:
        status = 'Уволен'
    await call.message.answer(f"""
ФИО: <b>{info['name']}</b>
Предмет: {subject['name']}

Статус: <b>{status}</b>
""", reply_markup=kb_back_to_main_menu())
    await state.finish()