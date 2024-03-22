from src.backend.database.init import *


# CREATE
def user_add_service(first_name, last_name, phone_number, password):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users(first_name, last_name, phone_number, password) VALUES (?, ?, ?, ?)",
                   (first_name, last_name, phone_number, password))
    connection.commit()
    cursor.close()
    close_database(connection)


# READ
def user_get_by_username_service(first_name, last_name):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE first_name = ? AND last_name = ?",
                   (first_name, last_name))
    row = cursor.fetchall()
    cursor.close()
    close_database(connection)
    return row


def user_get_by_phone_number_service(phone_number):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE phone_number = ?", (phone_number,))
    row = cursor.fetchall()
    cursor.close()
    close_database(connection)
    return row


# UPDATE
def user_update_phone_number_service(phone_number, user_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE users SET phone_number = ?"
        "WHERE user_id = ?",
        (phone_number, user_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def user_update_password_service(password, user_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE users SET password = ?"
        "WHERE user_id = ?",
        (password, user_id))
    connection.commit()
    cursor.close()
    close_database(connection)


# DELETE
def user_delete_service(user_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM users WHERE user_id = ?", (user_id,))
    connection.commit()
    cursor.close()
    close_database(connection)


# GET ALL
def user_get_all_service():
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    cursor.close()
    close_database(connection)
    return rows
