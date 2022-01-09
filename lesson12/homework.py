'''Я не совсем понял как правильно нужно связывать таблицы в запросах, так что чуть-чуть нагавнокодил'''

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
    choise = None
    while choise != 0:
        print(f'Для продолжения работы выберите нужную опперацию:')
        print(f'1 -Добавить нового покупателя')
        print(f'2 -Добавить новый продукт')
        print(f'3 -опперация покупки')
        print(f'4 -отобразить все товары купленные пользователем')
        print(f'0 -выход из программы')
        print(f'')
        choise = int(input(f'Выберите необходимую опперацию...: '))

        if choise == 1:     # новый покупатель
            Session = sessionmaker(bind=engine)
            session = Session()
            new_name = input(f'Введите Email: ')
            customer = Customer(email=new_name)
            session.add(customer)
            session.commit()

        if choise == 2:  # новый товар
            Session = sessionmaker(bind=engine)
            session = Session()
            new_name = input(f'Введите название продукта: ')
            new_price = input(f'Введите цену: ')
            product = Product(name=new_name, price=new_price)
            session.add(product)
            session.commit()

        if choise == 3:  # новая покупка
            Session = sessionmaker(bind=engine)
            session = Session()
            email = input("Введите email пользователя")
            human = session.query(Customer).filter(Customer.email == email).first()
            product = input("Введите название продукта")
            product = session.query(Product).filter(Product.name == product).first()
            cout_x = int(input("Введите количесво продукта"))
            purchare = Purchase(id_pr=product.id_product, id_cu=human.id_customer, cout=cout_x,
                                receipt=cout_x*product.price, date=datetime.now())
            session.add(purchare)
            session.commit()

        if choise == 4:  # просмотр покупок определенного покупателя
            Session = sessionmaker(bind=engine)
            session = Session()
            email = input("Введите email пользователя")
            user = session.query(Customer).filter(Customer.email == email).first()
            user = user.id_customer
            purchares = session.query(Purchase).filter(Purchase.id_cu == user).all()
            for i in purchares:
                name_product = session.query(Product).filter(Product.id_product == Purchase.id_pr).first()
                name_product = name_product.name
                print(f'Купил товар {name_product} на сумму {i.receipt} в количестве {i.cout} шт. {i.date}')

        if choise == 0:     # выход
            break


if __name__ == "__main__":
    engine = create_engine(
       f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)
    control()
