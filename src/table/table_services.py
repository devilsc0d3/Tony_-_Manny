import sqlite3


def table_add_service(number_table, user_name, phone_number):
    connection = sqlite3.connect('../database/sql.db')
    cur = connection.cursor()
    cur.execute(
        f"INSERT INTO TABLES(number_table, user_name, phone_number) VALUES ('{number_table}', '{user_name}', '{phone_number}')")
    connection.commit()
    connection.close()


def table_get_all_service():
    connection = sqlite3.connect('../database/sql.db')
    cur = connection.cursor()
    cur.execute('SELECT * FROM TABLES')
    rows = cur.fetchall()
    connection.close()
    return rows


def table_delete_service(number_table):
    connection = sqlite3.connect('../database/sql.db')
    cur = connection.cursor()
    cur.execute(f"DELETE FROM TABLES WHERE number_table = '{number_table}'")
    connection.commit()
    connection.close()


def table_update_service(number_table, user_name, phone_number):
    connection = sqlite3.connect('../database/sql.db')
    cur = connection.cursor()
    cur.execute(
        f"UPDATE TABLES SET user_name = '{user_name}', phone_number = '{phone_number}' WHERE number_table = '{number_table}'")
    connection.commit()
    connection.close()
