from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.data.loader import dp, bot
from bot.keyboards.inline import kb_edit_shedule

#Открытие меню редактирования расписания
@dp.callback_query_handler(text="edit_schedule", state="*")
async def func_edit_schedule(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"""
Выберите нужную функцию""", reply_markup=kb_edit_shedule())

#Заполнение расписания
@dp.callback_query_handler(text="edit_schedule", state="*")
async def func_edit_schedule(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"""
Выберите нужную функцию""", reply_markup=kb_edit_shedule())