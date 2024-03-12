import sqlite3


def reservation_add_service(user_id, table_id, date):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reservations_table (user_id, table_id, date) VALUES (?, ?, ?)",
                       (user_id, table_id, date))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error adding reservation:", error)


def reservation_delete_service(reservation_id):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reservations_table WHERE reservation_id=?", (reservation_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error deleting reservation:", error)


def reservation_get_service():
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservations_table")
        reservations = cursor.fetchall()
        conn.close()
        return reservations
    except sqlite3.Error as error:
        print("Error getting reservations:", error)


def reservation_update_service(reservation_id, user_id, table_id, date):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE reservations_table SET user_id=?, table_id=?, date=? WHERE reservation_id=?",
                       (user_id, table_id, date, reservation_id))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error updating reservation:", error)