import sqlite3
import os


def delete_id(id_delete):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            '''DELETE FROM user
            WHERE id=?;''',
            (id_delete))
    session.commit()
    return cursor.fetchone()

def update_tabble(id_update,cout_new):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            '''UPDATE user
            SET cout=?
            WHERE id=?;''',
            (cout_new,id_update))
    session.commit()
    return cursor.fetchone()

def show_all():
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            "SELECT * FROM user;")
    all_results = cursor.fetchall()
    for elements in all_results:
        print(elements)
    input("Нажмите любую клавишу для продолжения...")
    session.commit()
    return cursor.fetchone()

def input_add_product():
    name=input("Введите наименование товара:")
    price=input("Введите цену товара в формате ркк:")
    cout=int(input("Введите количество товара:"))
    comment=input("Введите комментарий к товару:")

    add_product([name,price,cout,comment])

def listen():
    while True:
        print(f'Выберите нужную опперацию:')
        print(f'1: Добавление нового продукта')
        print(f'2: Просмотр всех продуктов')
        print(f'3: Изменение количества продукта')
        print(f'4: Удаление продукта')
        print(f'5: Выход из программы')
        i=int(input('Ваш выбор?:'))
        if i==1:
            input_add_product()
        if i==2:
            show_all()
        if i==3:
            id_update=input("Введите id продукта для изменения его значения:")
            cout_new=input("Введите количество:")
            update_tabble(id_update,cout_new)
        if i==4:
            id_update=input("Введите id продукта для изменения его значения:")
            delete_id(id_update)
        if i==5:
            raise SystemExit

def create_tabble_products():
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            '''
        CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR UNIQUE,
            price INTEGER,
            cout INTREGER,
            comment VARCHAR
            );
            '''
        )
    session.commit()
    return cursor.fetchone()

def add_product(new_product):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            '''
        INSERT INTO user (name, price, cout, comment)
            VALUES (?,?,?,?);

            ''',
            (new_product),
        )

    session.commit()
    listen()

if __name__=='__main__':
    if os.path.isfile('products.sqlite3')==False:
        create_tabble_products()
    
    listen()



    
