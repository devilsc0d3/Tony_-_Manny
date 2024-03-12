import sqlite3


def table_add_service(rank, place):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tables (rank, place) VALUES (?, ?)", (rank, place))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error adding table:", error)


def table_get_all_service():
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tables")
        tables = cursor.fetchall()
        conn.close()
        return tables
    except sqlite3.Error as error:
        print("Error getting tables:", error)


def table_delete_service(table_id):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tables WHERE table_id=?", (table_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error deleting table:", error)


def table_update_service(table_id, rank, place):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE tables SET rank=?, place=? WHERE table_id=?", (rank, place, table_id))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error updating table:", error)
