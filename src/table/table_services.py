from src.database.init import *


def table_add_service(rank, places):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tables(rank, places) VALUES (?, ?)",
                   (rank, places))
    connection.commit()
    cursor.close()
    close_database(connection)


def table_get_service(table_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tables WHERE table_id = ?",
                   table_id)
    row = cursor.fetchone()
    cursor.close()
    close_database(connection)
    return row


def table_update_service(rank, places, table_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE tables SET rank = ?, places = ?"
        "WHERE table_id = ?",
        (rank, places, table_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def table_delete_service(table_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM tables WHERE table_id = ?", table_id)
    connection.commit()
    cursor.close()
    close_database(connection)


def table_get_all_service():
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tables')
    rows = cursor.fetchall()
    cursor.close()
    close_database(connection)
    return rows
