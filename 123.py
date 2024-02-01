import tkinter as tk
from tkinter import ttk
import sqlite3
import os

class Database:
    def __init__(self, db_file="people.db"):
        # Инициализация объекта базы данных
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
         # Создание таблицы при необходимости
        self.create_table()

    def create_table(self):
        # Создание таблицы "people" с полями id, first_name, last_name, age
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS people
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           first_name TEXT NOT NULL,
                           last_name TEXT NOT NULL,
                           age INTEGER NOT NULL)''')
        # Сохранение изменений
        self.conn.commit()

    def is_database_empty(self):
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM people")
        return cursor.fetchone()[0] == 0

    def insert_data(self, data):
         # Вставка данных в таблицу "people"
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO people (first_name, last_name, age) VALUES (?, ?, ?)", data)
        # Сохранение изменений
        self.conn.commit()

    def fetch_data(self):
        # Получение данных из таблицы "people"
        cursor = self.conn.cursor()
        cursor.execute("SELECT first_name, last_name, age FROM people")
        # Возвращение всех строк результата
        return cursor.fetchall()

class App:
    def __init__(self, root, database):
        # Инициализация графического интерфейса
        self.root = root
        self.root.title("People Database")

        # Инициализация базы данных
        self.database = database


        # Создание Treeview для отображения данных
        self.tree = ttk.Treeview(root, columns=("First Name", "Last Name", "Age"), show="headings")
        self.tree.heading("First Name", text="First Name")
        self.tree.heading("Last Name", text="Last Name")
        self.tree.heading("Age", text="Age")
        self.tree.pack(padx=10, pady=10)
        # Заполнение Treeview данными из базы данных
        self.populate_tree()

    def populate_tree(self):
        # Получение данных из базы данных
        data = self.database.fetch_data()
        # Вставка данных в Treeview
        for row in data:
            self.tree.insert("", "end", values=row)

def main():
    # Заполнение базы данных в первый раз из словаря
    initial_data = [
        ("Ivan", "Ivanov", 25),
        ("Marco", "Roise", 30),
        ("Bob", "Dilan", 22)
    ]
    # Инициализация базы данных
    db = Database()

    # Проверка, является ли база данных пустой или отсутствующей
    if db.is_database_empty():
        # Вставка начальных данных
        for person in initial_data:
            db.insert_data(person)
    # Создание главного окна Tkinter
    root = tk.Tk()
    # Инициализация приложения с графическим интерфейсом
    app = App(root, db)
    # Запуск главного цикла событий
    root.mainloop()

if __name__ == "__main__":
    main()
