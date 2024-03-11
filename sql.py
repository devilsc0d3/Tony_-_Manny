import sqlite3

def create_tables():
    try:
        connection = sqlite3.connect('sql.db')
        cur = connection.cursor()

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

        cur.execute(users_table)
        cur.execute(orders_table)
        connection.commit() # update database

    except sqlite3.Error as error:
        print("Error creating tables:", error)
    finally:
        if connection:
            connection.close()

def main():
    create_tables()

if __name__ == '__main__':
    main()
