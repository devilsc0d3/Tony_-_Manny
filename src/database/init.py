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


def create_users_table():
    return """ CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(255) NOT NULL,
        last_Name VARCHAR(255) NOT NULL,
        phone_number INTEGER,
        password VARCHAR(255) NOT NULL
    ); """


def create_dishes_table():
    return """ CREATE TABLE IF NOT EXISTS dishes (
        dish_id INTEGER PRIMARY KEY AUTOINCREMENT,
        rank INTEGER NOT NULL,
        title VARCHAR(255) NOT NULL,
        recipe VARCHAR(255) NOT NULL,
        price FLOAT NOT NULL,
        quantity INTEGER NOT NULL
    ); """


def create_tables_table():
    return """ CREATE TABLE IF NOT EXISTS tables (
        table_id INTEGER PRIMARY KEY AUTOINCREMENT,
        rank INTEGER NOT NULL,
        place INTEGER NOT NULL
    ); """


def create_drinks_table():
    return """ CREATE TABLE IF NOT EXISTS drinks (
        drink_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        recipe VARCHAR(255) NOT NULL,
        quantity INTEGER NOT NULL,
        price FLOAT NOT NULL
    ); """


def create_reservations_table_table():
    return """ CREATE TABLE IF NOT EXISTS reservations_table (
        reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        table_id INTEGER,
        date DATETIME,
        FOREIGN KEY (user_id) REFERENCES users (user_id),
        FOREIGN KEY (table_id) REFERENCES tables (table_id)
    ); """


def create_click_and_collects_table_table():
    return """ CREATE TABLE IF NOT EXISTS click_and_collects (
        click_and_collect_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        dish_id INTEGER,
        drink_id INTEGER,
        date DATETIME,
        FOREIGN KEY (user_id) REFERENCES users (user_id),
        FOREIGN KEY (dish_id) REFERENCES dishe (dish_id),
        FOREIGN KEY (drink_id) REFERENCES drinks (drink_id)
    ); """


def create_tables():
    connection = open_database()
    if connection:
        try:
            cursor = connection.cursor()

            # creating tables
            users_table = create_users_table()
            dishes_table = create_dishes_table()
            tables_table = create_tables_table()
            drinks_table = create_drinks_table()
            reservations_table = create_reservations_table_table()
            click_and_collects_table = create_click_and_collects_table_table()

            # execute requests
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
    cur.execute("INSERT INTO users(first_name, last_name, phone_number) VALUES (?,?,?)",
                ('adan', 'Laldy', '454545454545454545'))
    """
    cur.execute("INSERT INTO tables(rank, place) VALUES (?,?)",
                (1, 1))
    cur.execute("INSERT INTO dishes(rank, title, recipe, price, quantity) VALUES (?,?,?,?,?)",
                (1, 'Poulet au curry', 'Poulet, curry', 10, 100))
    cur.execute("Insert INTO dishes(rank, title, recipe, price, quantity) VALUES (?,?,?,?,?)",
                (2, 'puree douce', 'pomme de terre, poivre', 10, 100))
    cur.execute("INSERT INTO dishes(rank, title, recipe, price, quantity) VALUES (?,?,?,?,?)",
                (3, 'poulet frit', 'poulet, frit', 10, 100))
    cur.execute("INSERT INTO drinks(name, recipe, quantity, price) VALUES (?,?,?,?)",
                ('drink1', 'recipe1', 100, 5))
    cur.execute("INSERT INTO reservations_table(user_id, table_id, date) VALUES (?,?,?)",
                (1, 1, '2021-01-01 12:00:00'))
    cur.execute("INSERT INTO click_and_collects(user_id, dish_id, drink_id, date) VALUES (?,?,?,?)",
                (1, 1, 1, '2021-01-01 12:00:00'))

    conn.commit()
    conn.close()
    close_database(conn)  # close database
