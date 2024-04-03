from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.data.loader import dp, bot
from bot.keyboards.inline import kb_main_menu

#Обработка команды /start
@dp.message_handler(commands=['start'], state="*")
@dp.callback_query_handler(text="back_to_main_menu", state="*")
async def func_main_start(message: Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id, 
"""
<b>Добро пожаловать в электронное расписание</b>
Здесь вы можете просмотреть расписание и составлять его
""", reply_markup=kb_main_menu())