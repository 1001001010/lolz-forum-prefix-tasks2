from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.keyboards.inline import kb_teacher
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
    await call.message.edit_text(f"Укажите ФИО преподавателя: ", reply_markup=await kb_teacher())
    await New_teacher.full_name.set()

#Получение ФИО преподавателя
# @dp.message_handler(state=New_teacher.full_name)
# async def func_new_book_new_genre(message: Message, state: FSMContext):
    