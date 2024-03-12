import sqlite3


def add_dish(rank, title, recipe, price, quantity):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dishe (rank, title, recipe, price, quantity) VALUES (?, ?, ?, ?, ?)",
                       (rank, title, recipe, price, quantity))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error adding dish:", error)


def delete_dish(dish_id):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dishe WHERE dishe_id=?", (dish_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error deleting dish:", error)


def get_dishes():
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dishe")
        dishes = cursor.fetchall()
        conn.close()
        return dishes
    except sqlite3.Error as error:
        print("Error getting dishes:", error)


def update_dish(dish_id, rank, title, recipe, price, quantity):
    try:
        conn = sqlite3.connect('./database/sql.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE dishe SET rank=?, title=?, recipe=?, price=?, quantity=? WHERE dishe_id=?",
                       (rank, title, recipe, price, quantity, dish_id))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error updating dish:", error)
