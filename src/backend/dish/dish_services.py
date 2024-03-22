from src.backend.database.init import *


def dish_add_service(name, recipe, price, quantity):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO dishes (name, recipe, price, quantity) VALUES (?, ?, ?, ?)",
                   (name, recipe, price, quantity))
    connection.commit()
    cursor.close()
    close_database(connection)


def dish_get_service(dish_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM dishes WHERE dish_id = ?",
                   dish_id)
    row = cursor.fetchone()
    cursor.close()
    close_database(connection)
    return row


def dish_update_service(name, recipe, price, quantity, dish_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE dishes SET name = ?, recipe = ?, price = ?, quantity = ?"
        "WHERE dish_id = ?",
        (name, recipe, price, quantity, dish_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def dish_delete_service(dish_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM dishes WHERE dish_id = ?", dish_id)
    connection.commit()
    cursor.close()
    close_database(connection)


def dish_get_all_service():
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM dishes')
    rows = cursor.fetchall()
    cursor.close()
    close_database(connection)
    return rows
