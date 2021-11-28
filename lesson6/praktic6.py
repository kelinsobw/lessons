import random
import csv

#  Дан словарь, где в качестве ключей английские слова, 
# а значений - их перевод на русский язык. Написать две 
# функции, одна переводит слово с английского на русский, 
# где слово - это входной параметр, вторая функция - с русского 
# на английский.



def en_ru_csv(word):
    file = "traslate.csv"
    with open(file,"r",newline="") as file:
        reader=csv.reader(file)
        for row in reader:
            if row[0]==word:
                return(row[1])


def ru_en_csv(word):
    file = "traslate.csv"
    with open(file,"r",newline="") as file:
        reader=csv.reader(file)
        for row in reader:
            if row[1]==word:
                return(row[0])


def ru_en(slovo):
    for en,ru in slov.items():
        if slovo==en:
            return ru

def en_ru(slovo):
    for en,ru in slov.items():
        if slovo==ru:
            return en


slov={
    "cat":"кот",
    "apple":"яблоко",
}
print(en_ru("яблоко"))
print(ru_en("cat"))
print(en_ru_csv("cat"))
print(ru_en_csv("кот"))


"""#Доработать первое задание так, чтобы словарь читался из текстового 
# CSV файла, где на каждой строке пары слов вида: apple,яблоко.

смотреть выше
"""

#Написать функцию которая возвращают случайным образом одну карту из 
# стандартной колоды в 36 карт, где на первом месте номинал карты номинал 
# (6 - 10, J, D, K, A), а на втором название масти (Hearts, Diamonds, Clubs, Spades).

#ищем номинальное значение карты для подсчета очков
"""def translate_name(kart):
    try:
        return(int(kart))
    except:
        if kart=="J":
            return(2)
        if kart=="D":
            return(3)
        if kart=="K":
            return(4)
        if kart=="A":
            return(11)

#проверяем вытягивали ли мы данную карту раньше
def cheсk(kart,temp):
    for i in range(0,len(temp)):
        if kart==temp[i]:
            return(False)
    return True

#выбираем случайную карту
def random_cart(name,suit,carts_gamer_1,carts_gamer_2): 
    for i in range(0,56):
        r_name,r_cart=random.choice(name),random.choice(suit)
        temp=carts_gamer_1+carts_gamer_2
        if cheсk((r_name,r_cart),temp)==True:
            return((r_name,r_cart))


name_carts=("6","7","8","9","10","J","D","K","A")
suit_carts=("Hearts","Diamonds","Clubs","Spades")

#очки
gamer_1=0
gamer_2=0

#игроки берут по две карты
carts_gamer_1=[]
carts_gamer_2=[]
carts_gamer_1.append(random_cart(name_carts,suit_carts, carts_gamer_1, carts_gamer_2))
gamer_1+=translate_name(carts_gamer_1[-1][0])
carts_gamer_2.append(random_cart(name_carts,suit_carts, carts_gamer_1, carts_gamer_2))
gamer_2+=translate_name(carts_gamer_2[-1][0])
carts_gamer_1.append(random_cart(name_carts,suit_carts, carts_gamer_1, carts_gamer_2))
gamer_1+=translate_name(carts_gamer_1[-1][0])
carts_gamer_2.append(random_cart(name_carts,suit_carts, carts_gamer_1, carts_gamer_2))
gamer_2+=translate_name(carts_gamer_2[-1][0])
print("Игрок 1, ваши карты:", carts_gamer_1, ", у вас", gamer_1, "очков.")
print("Игрок 2, ваши карты:", carts_gamer_2, ", у вас", gamer_2, "очков.")

#предложение поочередно добрать карты
gamer_1_game=True
gamer_2_game=True
while True:
    if gamer_1_game==True and gamer_1<21:
        question=input(("Игрок 1, вы хотите взять еще карту? (y/n) "))
        if question=="y":
            new_cart=random_cart(name_carts,suit_carts, carts_gamer_1, carts_gamer_2)
            carts_gamer_1.append(new_cart)
            gamer_1+=translate_name(carts_gamer_1[-1][0])
            print("Вы достали ", new_cart, "у вас ",gamer_1,"очков")
        else: gamer_1_game=False
    else: gamer_1_game=False
    if gamer_2_game==True and gamer_2<21:
        question=input(("Игрок 2, вы хотите взять еще карту? (y/n) "))
        if question=="y":
            new_cart=random_cart(name_carts,suit_carts, carts_gamer_1, carts_gamer_2)
            carts_gamer_2.append(new_cart)
            gamer_2+=translate_name(carts_gamer_2[-1][0])
            print("Вы достали ", new_cart, "у вас ",gamer_2,"очков")
        else: gamer_2_game=False
    else: gamer_2_game=False
    
    #подведение итогов игры
    if gamer_1>21 and gamer_2>21:
        print("Вы оба проиграли(((...")
        break
    if gamer_2_game==False and gamer_1_game==False:
        print("Игра окончена. У игрока 1 ", gamer_1 , "очко(ов).")
        print("               У игрока 2 ", gamer_2 , "очко(ов).") 

        if gamer_1>gamer_2 and gamer_1<=21 and gamer_2<=21:
            print("Победил игрок 1")
            break
        elif gamer_2>gamer_1 and gamer_2<=21 and gamer_2<=21:
            print("Победил игрок 2")
            break
        elif gamer_1==gamer_2:
            print("Ничья...")
        elif gamer_2>21:
            print("Победил игрок 1")
            break
        elif gamer_1>21:
            print("Победил игрок 2")
            break"""