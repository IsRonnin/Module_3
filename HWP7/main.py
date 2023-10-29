import tkinter as tk
from tkinter import ttk
import sqlite3

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg="#d7d8e0", bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        self.add_img = tk.PhotoImage(file='./HWP7/img/add.png')
        btn_open_dialog = tk.Button(toolbar, bg="#d7d8e0", bd=0, image=self.add_img, command=self.open_dialog)
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'name', 'tel', 'email'), height=45, show="headings")
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('name', width=300, anchor=tk.CENTER)
        self.tree.column('tel', width=150, anchor=tk.CENTER)
        self.tree.column('email', width=150, anchor=tk.CENTER)

        self.tree.heading("ID", text="ID")
        self.tree.heading("name", text="ФИО")
        self.tree.heading("tel", text="Телефон")
        self.tree.heading("email", text="E-Mail")

        self.tree.pack(side=tk.LEFT)

    def open_dialog(self):
        Child()
    
    def records(self, name, tel, email):
        self.db.insert_data(name, tel, email)
        self.view_records()

    def view_records(self):
        self.db.c.execute('SELECT * FROM db') 
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app
    
    def init_child(self):
        self.title('Добавить контакт')
        self.geometry('440x200')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        label_name = tk.Label(self, text="ФИО:")
        label_name.place(x=50, y=50)
        label_select = tk.Label(self, text="Телефон:")
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text="E-mail:")
        label_sum.place(x=50, y=110)

        entry_name = ttk.Entry(self)
        entry_name.place(x=200, y = 50)
        entry_email = ttk.Entry(self)
        entry_email.place(x=200, y = 80)
        entry_tel = ttk.Entry(self)
        entry_tel.place(x=200, y = 110)

        self.btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        self.btn_cancel.place(x=180, y=170)

        self.btn_ok = ttk.Button(self, text="Добавить")
        self.btn_ok.place(x=260, y=170)
        self.btn_ok.bind("<Button-1>", lambda event:
                         self.view.records(entry_name.get(),
                                           entry_email.get(),
                                           entry_tel.get()))
        self.btn_ok.bind('<Button-1>', lambda event: self.destroy, add="+")

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("db.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS db(
            id INTEGER PRIMARY KEY,
            name TEXT,
            tel TEXT,
            email TEXT
        );''')
        self.conn.commit()

    def insert_data(self, name, tel, email):
        self.c.execute('INSERT INTO db(name, tel, email) VALUES (?, ?, ?)', (name,tel,email))
        self.conn.commit()


if __name__ == '__main__':
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title('Телефонная Книга')
    root.geometry('665x450')
    root.resizable(False, False)
    root.mainloop()