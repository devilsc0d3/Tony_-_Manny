import sqlite3


def add_table(rank, place):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tables (rank, place) VALUES (?, ?)", (rank, place))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error adding table:", error)


def get_tables():
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tables")
        tables = cursor.fetchall()
        conn.close()
        return tables
    except sqlite3.Error as error:
        print("Error getting tables:", error)


def delete_table(table_id):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tables WHERE table_id=?", (table_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error deleting table:", error)

def update_table(table_id, rank, place):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE tables SET rank=?, place=? WHERE table_id=?", (rank, place, table_id))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error updating table:", error)
