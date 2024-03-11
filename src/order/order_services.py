from src.database.init import *


def order_add_service(user_id, click_and_collect_id, table_reservation_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO orders(user_id, click_and_collect_id, table_reservation_id) VALUES (?, ?, ?)",
                   (user_id, click_and_collect_id, table_reservation_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def order_get_all_service():
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


def order_delete_service(order_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM orders WHERE order_id = ?", (order_id))
    connection.commit()
    cursor.close()
    close_database(connection)


def order_update_service(click_and_collect_id, table_reservation_id, order_id):
    connection = open_database()
    cursor = connection.cursor()
    cursor.execute("UPDATE orders SET click_and_collect_id = ?, table_reservation_id = ? WHERE order_id = ?",
                   (click_and_collect_id, table_reservation_id, order_id))
    connection.commit()
    connection.close()
    close_database(connection)
