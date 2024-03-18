from src.database.init import *


def user_add_service(first_name, last_name, phone_number, password):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users(first_name, last_name, phone_number, password) VALUES (?, ?, ?, ?)",
                   (first_name, last_name, phone_number, password))
    connection.commit()
    cursor.close()
    close_database(connection)


def user_get_service(first_name, last_name):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE first_name = ? AND last_name = ?",
                   (first_name, last_name))
    row = cursor.fetchall()
    cursor.close()
    close_database(connection)
    return row


def user_update_service(first_name, last_name, phone_number, user_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE users SET first_name = ?, last_name = ?, phone_number = ?"
        "WHERE click_and_collect_id = ?",
        (first_name, last_name, phone_number, user_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def user_delete_service(user_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM users WHERE user_id = ?", user_id)
    connection.commit()
    cursor.close()
    close_database(connection)


def user_get_all_service():
    connection = sqlite3.connect('../database/sql.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    cursor.close()
    close_database(connection)
    return rows
