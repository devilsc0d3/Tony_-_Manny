from src.database.init import *


def click_and_collect_add_service(dishes_id, drinks_id, date_time, user_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO click_and_collects(dishes_id, drinks_id, date_time, user_id) VALUES (?, ?, ?, ?)",
                   (dishes_id, drinks_id, date_time, user_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def click_and_collect_get_all_service():
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM click_and_collects')
    rows = cursor.fetchall()
    connection.close()
    return rows


def click_and_collect_delete_service(click_and_collect_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM click_and_collects WHERE click_and_collect_id = ?", (click_and_collect_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def click_and_collect_update_service(dishes_id, drinks_id, date_time, user_id, click_and_collect_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE click_and_collects SET dishes_id = ?, drinks_id = ?, date_time = ?, user_id = ? WHERE click_and_collect_id = ?",
        (dishes_id, drinks_id, date_time, user_id, click_and_collect_id))
    connection.commit()
    connection.close()
    close_database(connection)
