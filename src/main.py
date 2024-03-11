import sqlite3

def create_tables():
    try:
        connection = sqlite3.connect('sql.db')
        cur = connection.cursor()

        # creating tables
        users_table = """ CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name VARCHAR(255) NOT NULL,
                            last_Name VARCHAR(255) NOT NULL,
                            phone_number INTEGER
                        ); """

        orders_table = """ CREATE TABLE IF NOT EXISTS orders (
                            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
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

        cur.execute(users_table)
        cur.execute(orders_table)
        cur.execute(click_and_collects_table)
        cur.execute(table_reservations_table)
        connection.commit()  # update database
        connection.close()

    except sqlite3.Error as error:
        print("Error creating tables:", error)


def fill_table():
    conn = sqlite3.connect('sql.db')
    cur = conn.cursor()



    cur.execute("INSERT INTO menu(title, recipe, rank) VALUES (?, ?, ?)",
                ('Burger', 'Bun, Meat, Tomato, Onion, Cheese', 1))
    cur.execute("INSERT INTO menu(title, recipe, rank) VALUES (?, ?, ?)",
                ('Fries', 'Potato, Salt, Oil', 2))
    cur.execute("INSERT INTO menu(title, recipe, rank) VALUES (?, ?, ?)",
                ('Soda', 'Soda, Ice', 3))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_tables()
    fill_table()
