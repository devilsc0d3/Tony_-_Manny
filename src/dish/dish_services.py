import sqlite3


def dish_add_service(rank, title, recipe, price, quantity):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dishes (rank, title, recipe, price, quantity) VALUES (?, ?, ?, ?, ?)",
                       (rank, title, recipe, price, quantity))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error adding dish:", error)


def dish_delete_service(dish_id):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dishes WHERE dishe_id=?", (dish_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error deleting dish:", error)


def dish_get_all_service():
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dishes")
        dishes = cursor.fetchall()
        conn.close()
        return dishes
    except sqlite3.Error as error:
        print("Error getting dishes:", error)


def dish_update_service(dish_id, rank, title, recipe, price, quantity):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE dishes SET rank=?, title=?, recipe=?, price=?, quantity=? WHERE dishe_id=?",
                       (rank, title, recipe, price, quantity, dish_id))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error updating dish:", error)
