from src.database.init import *


def reservation_table_add_service(table_id, date_time, user_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO reservations_table(table_id, date, user_id) VALUES (?, ?, ?)",
                   (table_id, date_time, user_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def reservation_table_get_service(reservation_table_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM reservation_tables WHERE reservation_table_id = ?",
                   reservation_table_id)
    row = cursor.fetchone()
    cursor.close()
    close_database(connection)
    return row


def reservation_table_update_service(table_id, date_time, user_id, reservation_table_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE reservation_tables SET table_id = ?, date_time = ?, user_id = ?"
        "WHERE reservation_table_id = ?",
        (table_id, date_time, date_time, user_id, reservation_table_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def reservation_table_delete_service(reservation_table_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM reservations_table WHERE reservation_id = ?", (reservation_table_id,))
    connection.commit()
    cursor.close()
    close_database(connection)


def reservation_table_get_all_service():
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM reservations_table')
    rows = cursor.fetchall()
    cursor.close()
    close_database(connection)
    return rows
