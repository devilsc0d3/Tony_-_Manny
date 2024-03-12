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
                                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        first_name VARCHAR(255) NOT NULL,
                                        last_Name VARCHAR(255) NOT NULL,
                                        phone_number INTEGER
                                    ); """

            dishes_table = """ CREATE TABLE IF NOT EXISTS dishes (
                                    dishe_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    rank INTEGER NOT NULL,
                                    title VARCHAR(255) NOT NULL,
                                    recipe VARCHAR(255) NOT NULL,
                                    price FLOAT NOT NULL,
                                    quantity INTEGER NOT NULL
                                ); """

            tables_table = """ CREATE TABLE IF NOT EXISTS tables (
                                table_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                rank INTEGER NOT NULL,
                                place INTEGER NOT NULL
                            ); """
            drinks_table = """ CREATE TABLE IF NOT EXISTS drinks (
                        drink_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(255) NOT NULL,
                        recipe VARCHAR(255) NOT NULL,
                        quantity INTEGER NOT NULL,
                        price FLOAT NOT NULL
                    ); """

            reservations_table = """ CREATE TABLE IF NOT EXISTS reservations (
                        reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        table_id INTEGER,
                        date DATETIME,
                        FOREIGN KEY (user_id) REFERENCES users (user_id),
                        FOREIGN KEY (table_id) REFERENCES tables (table_id)
                    ); """

            click_and_collects_table = """ CREATE TABLE IF NOT EXISTS click_and_collects (
                        click_and_collect_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        dish_id INTEGER,
                        drink_id INTEGER,
                        date DATETIME,
                        FOREIGN KEY (user_id) REFERENCES users (user_id),
                        FOREIGN KEY (dish_id) REFERENCES dishes (dish_id),
                        FOREIGN KEY (drink_id) REFERENCES drinks (drink_id)
                    ); """

            cursor.execute(users_table)
            cursor.execute(dishes_table)
            cursor.execute(tables_table)
            cursor.execute(drinks_table)
            cursor.execute(reservations_table)
            cursor.execute(click_and_collects_table)

            connection.commit()  # update database
            cursor.close()  # close cursor
            close_database(connection)  # close database
        except Exception as e:
            print("Error:", e)


def fill_tables():
    conn = open_database()
    cur = conn.cursor()
    """
    cur.execute("INSERT INTO menu(title, recipe, rank) VALUES (?, ?, ?)",
                ('Burger', 'Bun, Meat, Tomato, Onion, Cheese', 1))
    cur.execute("INSERT INTO menu(title, recipe, rank) VALUES (?, ?, ?)",
                ('Fries', 'Potato, Salt, Oil', 2))
    cur.execute("INSERT INTO menu(title, recipe, rank) VALUES (?, ?, ?)",
                ('Soda', 'Soda, Ice', 3))
    """
    cur.execute("INSERT INTO users(first_name, last_name, phone_number) VALUES (?,?,?)",
                ('adan', 'laldy', '454545454545454545'))

    conn.commit()
    conn.close()
    close_database(conn)  # close database
