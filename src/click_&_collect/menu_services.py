import sqlite3


def menu_add_service(title, recipe, rank):
    connection = sqlite3.connect('../sql.db')
    cur = connection.cursor()
    cur.execute(f"INSERT INTO Menu(title, recipe, rank) VALUES ('{title}', '{recipe}', '{rank}')")
    connection.commit()
    connection.close()


def menu_get_all_service():
    connection = sqlite3.connect('../sql.db')
    cur = connection.cursor()
    cur.execute('SELECT * FROM Menu')
    rows = cur.fetchall()
    connection.close()
    return rows


def menu_delete_service(title):
    connection = sqlite3.connect('../sql.db')
    cur = connection.cursor()
    cur.execute(f"DELETE FROM Menu WHERE name = '{title}'")
    connection.commit()
    connection.close()


def menu_update_service(name, recipe, rank):
    connection = sqlite3.connect('../sql.db')
    cur = connection.cursor()
    cur.execute(f"UPDATE Menu SET recipe = '{recipe}', rank = '{rank}' WHERE name = '{name}'")
    connection.commit()
    connection.close()
