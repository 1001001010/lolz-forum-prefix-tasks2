from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.data.config import db
from bot.keyboards.inline import kb_date, kb_shedule

#Выбор даты
@dp.callback_query_handler(text="fill_schedule", state="*")
async def func_list_teachers(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"Выберите дату", reply_markup=kb_date())
    
@dp.callback_query_handler(text_startswith="date", state="*")
async def func_new_book_to_db(call: CallbackQuery, state: FSMContext):
    await state.finish()
    data = call.data.split("_")[1]
    await call.message.edit_text(f"Расписание на {data}:", reply_markup=await kb_shedule(date=data))