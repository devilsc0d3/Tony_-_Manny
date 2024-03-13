from src.database.init import *
from src.front.login.login import pages


def main():
    create_tables()
    fill_tables()


if __name__ == '__main__':
    main()
    pages()
