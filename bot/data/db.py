import aiosqlite
from async_class import AsyncClass

def dict_factory(cursor, row):
    save_dict = {}

    for idx, col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]

    return save_dict

#Путь до БД
path_db = 'bot/data/database.db'

#Проверка и создание бд
class DB(AsyncClass):
    async def __ainit__(self):
        self.con = await aiosqlite.connect(path_db)
        self.con.row_factory = dict_factory

    #Получение всех преподавателей
    async def get_all_teachers(self):
        row = await self.con.execute("SELECT * FROM teachers")
        return await row.fetchall()

    #Получение списка всех предметов
    async def get_all_subjects(self, page):
        offset = (page - 1) * 10
        row = await self.con.execute("SELECT * FROM subjects LIMIT 10 OFFSET ?", (offset,))
        return await row.fetchall()
    
    #Получение инфо о преподавателе
    async def get_teacher_info(self, id):
        row = await self.con.execute("SELECT * FROM teachers WHERE id = ?", (id,))
        return await row.fetchone()
    
    #Получение инфо о предмете
    async def get_subject_info(self, subj_id):
        row = await self.con.execute("SELECT name FROM subjects WHERE id = ?", (subj_id,))
        return await row.fetchone()
    
    #Получение расписания на n-число
    async def get_shedule(self, id):
        row = await self.con.execute("SELECT * FROM schedule WHERE date = ?", (id,))
        return await row.fetchall()
        
    # Добавление нового предмета
    async def new_genre(self, name):
        await self.con.execute(f"INSERT INTO subjects(name) VALUES (?)", (name,))
        await self.con.commit()
    
    #Увольнение/Принятие на работу преподавателя
    async def dismis_teacher(self, id, status):
        await self.con.execute("UPDATE teachers SET status = ? WHERE id = ?", (status, id))
        await self.con.commit()
    
    # Добавление нового преподавателя
    async def new_prepod(self, name, subject, status):
        await self.con.execute(f"INSERT INTO teachers(name, subject, status) VALUES (?, ?, ?)", (name, subject, status))
        await self.con.commit()
    
    # Поиск по ключевому слову
    async def search_by_word(self, table, word):
        search_word = f"%{word}%"
        row = await self.con.execute(f"SELECT * FROM {table} WHERE name LIKE ?", (search_word,))
        return await row.fetchall()
    
    #Проверка на существование бд и ее создание
    async def create_db(self):
        classrooms_info = await self.con.execute("PRAGMA table_info(classrooms)")
        if len(await classrooms_info.fetchall()) == 2:
            print("database was found (Classrooms | 1/4)")
        else:
            await self.con.execute("CREATE TABLE classrooms ("
                                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                   "number INTEGER)")
            data = [i for i in range(1, 151)]
            for number in data:
                await self.con.execute("INSERT INTO classrooms(number) VALUES (?)", (number,))
            print("database was not found (classrooms | 1/4), creating...")
    
        teachers_info = await self.con.execute("PRAGMA table_info(teachers)")
        if len(await teachers_info.fetchall()) == 4:
            print("database was found (Teachers | 2/4)")
        else:
            await self.con.execute("CREATE TABLE teachers("
                                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                   "name TEXT,"
                                   "subject TEXT,"
                                   "status BOOLEAN DEFAULT 1)")
            print("database was not found (Teachers | 2/4), creating...")
        
        subjects_info = await self.con.execute("PRAGMA table_info(subjects)")
        if len(await subjects_info.fetchall()) == 2:
            print("database was found (Subjects | 3/4)")
        else:
            await self.con.execute("CREATE TABLE subjects("
                                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                   "name TEXT)")
            print("database was not found (Subjects | 3/4), creating...")
            
        schedule_info = await self.con.execute("PRAGMA table_info(schedule)")
        if len(await schedule_info.fetchall()) == 6:
            print("database was found (Schedule | 4/4)")
        else:
            await self.con.execute("CREATE TABLE schedule("
                                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                   "subject_id INTEGER,"
                                   "classroom_id INTEGER,"
                                   "teacher_id INTEGER,"
                                   "lesson_num INTEGER,"
                                   "date TIMESTAMP)")
            print("database was not found (Schedule | 4/4), creating...")
            
        await self.con.commit()