from src.database.init import *


def drink_add_service(name, recipe, price, quantity):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO drinks(name, recipe, price, quantity) VALUES (?, ?, ?, ?)",
                   (name, recipe, price, quantity))
    connection.commit()
    cursor.close()
    close_database(connection)


def drink_get_service(drink_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM drinks WHERE drink_id = ?",
                   drink_id)
    row = cursor.fetchone()
    cursor.close()
    close_database(connection)
    return row


def drink_update_service(name, recipe, price, quantity, drink_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE drinks SET name = ?, recipe = ?, price = ?, quantity = ?"
        "WHERE drink_id = ?",
        (name, recipe, price, quantity, drink_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def drink_delete_service(drink_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM drinks WHERE drink_id = ?", drink_id)
    connection.commit()
    cursor.close()
    close_database(connection)


def drink_get_all_service():
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM drinks')
    rows = cursor.fetchall()
    cursor.close()
    close_database(connection)
    return rows
