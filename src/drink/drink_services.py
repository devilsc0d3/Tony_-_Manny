import sqlite3


def drink_add_service(name, recipe, quantity, price):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO drinks (name, recipe, quantity, price) VALUES (?, ?, ?, ?)",
                       (name, recipe, quantity, price))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error adding drink:", error)


def drink_delete_service(drink_id):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM drinks WHERE drink_id=?", (drink_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error deleting drink:", error)


def drink_get_all_service():
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM drinks")
        drinks = cursor.fetchall()
        conn.close()
        return drinks
    except sqlite3.Error as error:
        print("Error getting drinks:", error)


def drink_update_service(drink_id, name, recipe, quantity, price):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE drinks SET name=?, recipe=?, quantity=?, price=? WHERE drink_id=?",
                       (name, recipe, quantity, price, drink_id))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error updating drink:", error)
