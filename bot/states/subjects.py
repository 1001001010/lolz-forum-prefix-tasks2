from aiogram.dispatcher.filters.state import State, StatesGroup


class New_subjects(StatesGroup): #State на добавление нового предмета
    name = State()
    
class Search_subjects(StatesGroup): #State на поиск нужного предмета
    name = State()
    