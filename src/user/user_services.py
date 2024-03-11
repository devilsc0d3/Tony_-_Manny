from src.database.init import *


def user_add_service(first_name, last_name, phone_number):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users(first_name, last_name, phone_number) VALUES (?, ?, ?)",
                   (first_name, last_name, phone_number))
    connection.commit()
    cursor.close()
    close_database(connection)


def user_delete_service(user_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM users WHERE user_id = ?", (user_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def user_update_service(first_name, last_name, phone_number, user_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET first_name = ?, last_name = ?, phone_number = ? WHERE user_id = ?",
                   (first_name, last_name, phone_number, user_id))
    connection.commit()
    connection.close()
    close_database(connection)
