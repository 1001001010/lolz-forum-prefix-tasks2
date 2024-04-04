from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.data.config import db
from bot.keyboards.inline import kb_date
from bot.states.teachers import New_teacher

#Выбор даты
@dp.callback_query_handler(text="fill_schedule", state="*")
async def func_list_teachers(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"Выберите дату", reply_markup=kb_date())
    await New_teacher.full_name.set()