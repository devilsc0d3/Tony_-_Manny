import sqlite3


def menu_service():
    print('Hello, World!')


def table_service():
    print('Hello, World!')


def main():
    conn = sqlite3.connect('sql.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE Menu(recipe, Name, score)")

    menu_service()
