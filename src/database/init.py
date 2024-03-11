import sqlite3


def open_database():
    try:
        conn = sqlite3.connect('./database/sql.db')
        return conn
    except sqlite3.Error as error:
        print("Error opening database:", error)
        return None


def close_database(conn):
    try:
        if conn:
            conn.close()
    except sqlite3.Error as error:
        print("Error closing database:", error)


def create_tables():
    connection = open_database()
    if connection:
        try:
            cursor = connection.cursor()
            # creating tables
            users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                                        first_name VARCHAR(255) NOT NULL,
                                        last_Name VARCHAR(255) NOT NULL,
                                        phone_number INTEGER
                                    ); """

            orders_table = """ CREATE TABLE IF NOT EXISTS orders (
                                        order_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                                        user_id INTEGER NOT NULL,
                                        click_and_collect_id INTEGER,
                                        table_reservation_id INTEGER,
                                        FOREIGN KEY(user_id) REFERENCES users(user_id),
                                        FOREIGN KEY(click_and_collect_id) REFERENCES click_and_collects(click_and_collect_id),
                                        FOREIGN KEY(table_reservation_id) REFERENCES table_reservations(table_reservation_id)
                                    ); """

            click_and_collects_table = """ CREATE TABLE IF NOT EXISTS menu (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    rank INTEGER NOT NULL,
                                    title VARCHAR(255) NOT NULL,
                                    recipe VARCHAR(255) NOT NULL
                                ); """

            table_reservations_table = """ CREATE TABLE IF NOT EXISTS table_reservations (
                                table_reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INTEGER NOT NULL,
                                FOREIGN KEY(user_id) REFERENCES users(user_id)
                            ); """

            cursor.execute(users_table)
            cursor.execute(orders_table)
            cursor.execute(click_and_collects_table)
            cursor.execute(table_reservations_table)

            connection.commit()  # update database
            cursor.close()  # close cursor
            close_database(connection)  # close database
        except Exception as e:
            print("Error:", e)


def fill_tables():
    conn = sqlite3.connect('./database/sql.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO menu(title, recipe, rank) VALUES (?, ?, ?)",
                ('Burger', 'Bun, Meat, Tomato, Onion, Cheese', 1))
    cur.execute("INSERT INTO menu(title, recipe, rank) VALUES (?, ?, ?)",
                ('Fries', 'Potato, Salt, Oil', 2))
    cur.execute("INSERT INTO menu(title, recipe, rank) VALUES (?, ?, ?)",
                ('Soda', 'Soda, Ice', 3))

    conn.commit()
    conn.close()
    close_database(conn)  # close database

