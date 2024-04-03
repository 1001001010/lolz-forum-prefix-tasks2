from aiogram.dispatcher.filters.state import State, StatesGroup


class New_teacher(StatesGroup): #State на добавление нового преподавателя
    full_name = State()
    