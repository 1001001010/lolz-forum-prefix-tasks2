import aiosqlite
from async_class import AsyncClass

#Путь до БД
path_db = 'bot/data/database.db'

#Проверка и создание бд
class DB(AsyncClass):
    async def __ainit__(self):
        self.con = await aiosqlite.connect(path_db)
        self.con.row_factory = aiosqlite.Row

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
        if len(await teachers_info.fetchall()) == 3:
            print("database was found (Teachers | 2/4)")
        else:
            await self.con.execute("CREATE TABLE teachers("
                                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                   "name TEXT,"
                                   "subject TEXT)")
            print("database was not found (Teachers | 2/4), creating...")
        
        subjects_info = await self.con.execute("PRAGMA table_info(subjects)")
        if len(await subjects_info.fetchall()) == 3:
            print("database was found (Subjects | 3/4)")
        else:
            await self.con.execute("CREATE TABLE subjects("
                                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                   "name TEXT,"
                                   "link TEXT)")
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