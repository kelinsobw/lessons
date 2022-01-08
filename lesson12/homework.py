from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from my_base import *
from sqlalchemy.orm import sessionmaker
from datetime import datetime


DB_USER = "kelinso"
DB_PASSWORD = "kelinso"
DB_NAME = "kelinso"
DB_ECHO = True


def control():
    choise=None
    while choise != 0:
        print(f'Для продолжения работы выберите нужную опперацию:')
        print(f'1 -Добавить нового покупателя')
        print(f'2 -Добавить новый продукт')
        print(f'3 -опперация покупки')
        print(f'4 -отобразить все товары купленные пользователем')
        print(f'0 -выход из программы')
        print(f'')
        choise=int(input(f'Выберите необходимую опперацию...: '))


if __name__ == "__main__":
    engine = create_engine(
       f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)
    request = None
    control()

    Session = sessionmaker(bind=engine)
    session = Session()
    session.commit()
