from src.database.init import *
from src.front.home.home_page import home_page


def main():
    create_tables()
    fill_tables()
    home_page()


if __name__ == '__main__':
    main()
