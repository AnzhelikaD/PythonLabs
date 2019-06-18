"""1. *Добавьте вывод данных о фильмах для заданного режиссера (режиссера спросить у пользователя). Сортировать фильмы
 при выводе по годам.
2. *Добавьте вывод данных о режиссерах. Сортировать по алфавиту."""
import os
import sqlite3


def connect(filename):
    # Проверяем, существует ли файл БД:
    create = not os.path.exists(filename)
    # Создаем объект соединения db:
    db = sqlite3.connect(filename)
    # Если нет, тогда создаем БД:
    if create:
        # Создаем объект курсор cursor:
        cursor = db.cursor()
        # Создаем таблицу «Режиссеры»:
        cursor.execute("""
            CREATE TABLE directors (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name TEXT UNIQUE NOT NULL)
            """)
        # Создаем таблицу «Фильмы»:
        cursor.execute("""
            CREATE TABLE dvds (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            duration INTEGER NOT NULL,
            director_id INTEGER NOT NULL,
            FOREIGN KEY (director_id) REFERENCES directors)
            """)
        # Подтверждение создания таблиц
        db.commit()
        # Возвращаем объект соединения с БД:
    return db


def get_and_set_director(db, director):
    cursor = db.cursor()
    cursor.execute("SELECT id FROM directors WHERE name=?", (director,))
    # Посмотреть результат выборки:
    fields = cursor.fetchone()
    if fields:
        return fields[0]
    # Добавить режиссера, если его нет в БД:
    cursor.execute(
        "INSERT INTO directors (name) VALUES (?)",
        (director,))
    db.commit()
    return get_and_set_director(db, director)


def add_dvd(db):
    # Ввод данных пользователем:
    title = input('title: ')
    director = input('director: ')
    year = int(input('year: '))
    duration = int(input('duration (min): '))
    # Получить id директора (если его нет, создать):
    director_id = get_and_set_director(db, director)
    # Запись строки в таблицу:
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO dvds
        (title, year, duration, director_id)
        VALUES (?, ?, ?, ?) """,
                   (title, year, duration, director_id))
    db.commit()


def edit_dvd(db):
    # Поиск фильма по названию:
    start = input('Введите начало названия фильма: ')
    cursor = db.cursor()
    cursor.execute("SELECT title, id FROM dvds "
                   "WHERE title LIKE ? ORDER BY title",
                   (start + "%",))
    records = cursor.fetchall()
    # Если ничего не нашли, то выходим:
    if len(records) == 0:
        print("Нет фильма: ", start)
        return
    title, identity = records[0]
    cursor.execute(
        "SELECT dvds.year, dvds.duration, directors.name"
        "FROM dvds, directors "
        "WHERE dvds.director_id = directors.id AND "
        "dvds.id=:id", {'id': identity})
    # Результат поиска:
    year, duration, director = cursor.fetchone()
    # Редактируем данные:
    line = input('title [' + title + ']:')
    if line: title = line
    line = input('director [' + director + ']:')
    if line: director = line
    line = input('duration [' + str(duration) + ']:')
    if line: duration = int(line)
    line = input('year [' + str(year) + ']:')
    if line: year = int(line)
    director_id = get_and_set_director(db, director)
    # Изменить значения в БД:
    cursor.execute(
        "UPDATE dvds SET title=:title, year=:year, "
        "duration=:duration, director_id=:director_id "
        "WHERE id=:identity", locals())
    db.commit()


def remove_dvd(db):
    # Поиск фильма по названию:
    start = input('Введите начало названия фильма: ')
    cursor = db.cursor()
    cursor.execute("SELECT title, id FROM dvds "
                   "WHERE title LIKE ? ORDER BY title",
                   (start + "%",))
    records = cursor.fetchall()
    # Если ничего не нашли, то выходим:
    if len(records) == 0:
        print("Нет фильма: ", start)
        return
    title, identity = records[0]
    # Удаление:
    cursor.execute("DELETE FROM dvds WHERE id=?",
                   (identity,))
    db.commit()


def list_dvds(db):
    cursor = db.cursor()
    # SQL – запрос:
    sql = """SELECT dvds.title, dvds.year, dvds.duration,
        directors.name
        FROM dvds, directors
        WHERE dvds.director_id = directors.id
        ORDER BY dvds.title"""
    cursor.execute(sql)
    print()
    # Построчный вывод:
    for record in cursor:
        print("{0[0]} ({0[1]} год) {0[2]} минут, режиссер: {0[3]}".format(record))
    print()


"""1. *Добавьте вывод данных о фильмах для заданного режиссера (режиссера спросить у пользователя). Сортировать фильмы
 при выводе по годам."""


def getDirectorFilms(db, director):
    cursor = db.cursor()
    cursor.execute("""SELECT dvds.title, dvds.year, dvds.duration
        FROM dvds JOIN directors
        ON dvds.director_id = directors.id
        WHERE directors.name=?
        ORDER BY dvds.year""", (director,))
    print()
    for record in cursor:
        print("{0[0]} ({0[1]} год) {0[2]} минут".format(record))
    print()


"""2. *Добавьте вывод данных о режиссерах. Сортировать по алфавиту."""


def list_directors(db):
    cursor = db.cursor()
    sql = """SELECT directors.name
            FROM directors
            ORDER BY directors.name"""
    cursor.execute(sql)
    print()
    # Построчный вывод:
    for record in cursor:
        print("{0[0]}".format(record))
    print()


def main():
    # Файл БД:
    filename = r"BD_dvds.sdb"
    print(filename)
    # Соединение/создание
    db = connect(filename)
    # Бесконечный цикл Меню
    while True:
        # Вывод меню:
        print('Меню'.center(50, '-'))
        print('| ' + '0 - Выход'.ljust(45) + ' |')
        print('| ' + '1 - Добавление '.ljust(45) + ' |')
        print('| ' + '2 - Вывести все фильмы режиссера '.ljust(45) + ' |')
        print('| ' + '3 - Вывести всех режиссеров '.ljust(45) + ' |')
        print('| ' + '4 - Вывести все '.ljust(45) + ' |')
        print(''.center(50, '-'))
        # Выбор пользователя:
        c = input('Выберите пункт меню (0-9): ')
        if c == '0':  # Выход
            break
        elif c == '1':
            add_dvd(db)
        elif c == '2':
            director = input("Режиссер: ")
            getDirectorFilms(db, director)
        elif c == '3':
            list_directors(db)
        elif c == '4':
            list_dvds(db)


# Точка входа в программу:
main()
