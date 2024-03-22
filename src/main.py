from src.backend.database.init import *
from src.frontend.pages import pages


def main():
    create_tables()
    fill_tables()
    pages()


if __name__ == '__main__':
    main()
