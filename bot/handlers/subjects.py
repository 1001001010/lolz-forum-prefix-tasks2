from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp
from bot.data.config import db
from bot.keyboards.inline import kb_subjects, kb_back_to_main_menu
from bot.states.subjects import New_subjects


#Открытие списка предметов
@dp.callback_query_handler(text="subjects_menu", state="*")
async def func_list_subj(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"Список предметов: ", reply_markup=await kb_subjects())
    await New_subjects.name.set()

#Добавление предметов
@dp.callback_query_handler(text="add_subjects", state="*")
async def func_list_teachers(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"Укажите название предмета: ", reply_markup=kb_back_to_main_menu())
    await New_subjects.name.set()

#Получение название предмета
@dp.message_handler(state=New_subjects.name)
async def func_name_subj(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await db.new_genre(name = data['name'])
    await message.answer("Предмет успешно добавлен", reply_markup=kb_back_to_main_menu())

#Смена стреницы
@dp.callback_query_handler(text_startswith=['next_page', 'prev_page'], state="*")
async def func_change_page(call: CallbackQuery, state: FSMContext):
    data = call.data.split(':')
    if data[0] == 'next_page':
        page = int(data[1])
        await call.message.edit_reply_markup(reply_markup=await kb_subjects(page))
    elif data[0] == 'prev_page':
        page = int(data[1])
        await call.message.edit_reply_markup(reply_markup=await kb_subjects(page))
        
# Поиск предмета по ключевому слову или фразе
@dp.callback_query_handler(text="search_subject", state="*")
async def func_subj_search(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f"Введите ключевое слово или фразу для поиска\n<b>Обратите внимание, что на поиск влияет регистр!</b>")
    await Search.word.set()

@dp.message_handler(state=Search.word)
async def func_zapros_poiska(message: Message, state: FSMContext):
    """
    Результы поиска по ключевому слову или фразе

    Args:
        message (Message)
        state (FSMContext)
    """
    await state.update_data(word=message.text)
    data = await state.get_data()
    result = await db.search_by_word(data['word'])
    if len(result) == 0:
        await message.answer('По вашему запросу ничего не найдено', reply_markup=back_to_main_menu())
    else:
        await message.answer(f"Список книг по запросу - {data['word']}", reply_markup=await seach_list_kb(data['word']))
    await state.finish()