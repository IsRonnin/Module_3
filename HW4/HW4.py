import sqlite3

conn = sqlite3.connect("MyContacts.db")
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS Contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE ON CONFLICT IGNORE,
        phone_num TEXT,
        email TEXT
        )
    ''')

class Table:
    def add_new(name:str, phone:str, email:str)->None:
        cur.execute('''
        INSERT OR IGNORE INTO Contacts(name, phone_num, email) VALUES (?,?,?)
        ''', (name, phone, email))
        conn.commit()
    def select_all()->list:
        cur.execute('''SELECT * FROM Contacts''')
        rows = cur.fetchall()
        return rows
    def like_Search(column:str, query:str, answ:tuple)->list:
        cur.execute(f'''
        SELECT {"".join([str(i)+', ' for i in answ])[:-2]}
        FROM Contacts
        WHERE {column} LIKE '%{query}%'
        ''')
        rows = cur.fetchall()
        return rows
    def update_by_id(id:int, new_name:str, new_phone:str)->None:
        cur.execute(f'''
        UPDATE Contacts SET name = ? WHERE id = ?
        ''', (new_name, id))
        conn.commit()
        cur.execute(f'''
        UPDATE Contacts SET phone_num = ? WHERE id = ?
        ''', (new_phone, id))
        conn.commit()
    def delete_by_id(id:int):
        cur.execute(f'''
        DELETE FROM Contacts WHERE id={id}
        ''')
t = Table

t.add_new("Anders", "+1(9735)999-81-42352", "Anders@gmail.com")
t.add_new("Nessy", "+1(6890)908-55-55801", "Nessy@yahhoo.com")
t.add_new("Marty", "+193(2759)945-07-51403", "Marty@mail.ru")
t.add_new("Merry", "+79(8095)889-47-97916", "Merry_B@bk.ru")
t.add_new("Monk", "+935(7950)284-23-18677", "MonkWork@ya.ru")

print("\nВывод всех\n _________ \n")
[print(i) for i in t.select_all()] # Все

print("\nВывод только по +1 - имя и номер\n _________ \n")
[print(i) for i in t.like_Search("phone_num", "+1", ("name", "phone_num"))]

print("\nВывод только по gmail\n _________ \n")
[print(i) for i in t.like_Search("email", "gmail", ("name", "phone_num", "email"))]

print("\nОбновление по Id -> Пример id-4, Merry\n _________ \n")
[print(i) for i in t.like_Search("id", "4", ("name", "phone_num", "email"))]
t.update_by_id(4,"Ms.Merry", "+1(76)838-38-11")
[print(i) for i in t.like_Search("id", "4", ("name", "phone_num", "email"))]

print("\nУдаление по ID\n _________ \n")
[print(i) for i in t.like_Search("id", "4", ("name", "phone_num", "email"))]
t.delete_by_id(4)
[print(i) for i in t.select_all()]