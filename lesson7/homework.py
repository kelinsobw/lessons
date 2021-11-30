import math
import time
import random
import os

'''def chess(pos_1, pos_2):
    horisont=(1,2,3,4,5,6,7,8)
    vertical=(1,2,3,4,5,6,7,8)
    #horisont
    if pos_1[0]==pos_2[0]:
        return("yes")
    #vertical
    if pos_1[1]==pos_2[1]:
        return("yes")
    #diogonal
    if abs(int(pos_1[0])-int(pos_2[0]))==abs(int(pos_1[1])-int(pos_2[1])):
        return("yes")
    else:
        return("No")


def main():
    print(chess("34","22"))

if __name__=="__main__":
    main()'''

#0-вое задание
"""
def translate(coord,horisont=["A","B","C","D","E","F","G","H"]):
    return(horisont.index(coord))


def chess(pos_1, pos_2):
    if abs(translate(pos_1[0])-translate(pos_2[0]))==2 and abs(int(pos_1[1])-int(pos_2[1]))==1 or abs(translate(pos_1[0])-translate(pos_2[0]))==1 and abs(int(pos_1[1])-int(pos_2[1]))==2:
        return("Yes")
    else:
        return("No")

def main():
    print(chess("C1","B3"))


if __name__=="__main__":
    main()"""

#Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки 
# городов в этих странах. Написать функцию которая осуществляет поиск по городу и возвращает 
# страну. Оформить в виде программы, которая считывает название города и выводит на печать страну.

#По заданию вроде какработаем со списками, а не со словорями. Хотя может я и ошибаюсь...
"""def searh_counry(counrty,town):
    for index in counrty:
        for town_name in index[1]:
            if town_name==town:
                return index[0]


def main():
    country=[["Belarus",["Borisov","Minsk","Molodechno","Vitebsk"]],["Russia",["Moskow","Ekaterenburg","Sochi","Cheljabinsk"]],
    ["Germany",["Berlin","Hamburg","Hagen","Duren"]]]
    print(searh_counry(country,"Duren"))
    print(searh_counry(country,"Molodechno"))
    print(searh_counry(country,"Sochi"))
    city=input("Введите город:")
    city_counrty=searh_counry(country,city)
    print(city_counrty)

if __name__ =="__main__":
    main()

"""

#По условию была задача создать текстовый файл, так как я не был уверен можно ли использоать csv, то написал все в txt расширении.

def print_result(*arg):
    for i in arg:
        print(i)

def main():
    file=open("price.txt","r")
    baza=[]
    for line in file:
        baza.append(line[:-1])
    file.close()

    #Переведем все в многомерный список
    temp=[]
    for event in baza:
        temp.append((str(event)).split(","))
    baza=temp

    #Задание a:
    #пишем всех покупателей
    customer=[]
    for event in baza:
        if event[0] not in customer:
            customer.append(event[0])
    #создаем список в котором будет ответ
    temp=[]
    for i in range(0,len(customer)):
        temp.append(customer[i])
        temp.append("покупки")
        temp.append(0)
        temp.append(0)

    customer=[]
    for i in range(0,len(temp),4):
        temp2=[]
        temp2.append(temp[i])
        temp2.append(temp[i+1])
        temp2.append(temp[i+2])
        temp2.append(temp[i+3])
        customer.append(temp2)

    #производим рассчеты
    for x in range(0,len(customer)):
        for i in range(0,len(baza)):
            if baza[i][0]==customer[x][0]:
                customer[x][2]+=int(baza[i][2])
                customer[x][3]+=float(baza[i][3])*int(baza[i][2])


    for i in range(0,len(customer)):
        print(customer[i][0],"купил(а)",customer[i][2]," покупок стоимостью",customer[i][3])

 #задание B
 #Создаем списки
    tovar=[]
    for i in range(0,len(baza)):
        if baza[i][1] not in tovar:
            tovar.append(baza[i][1])

    temp2=[]
    for i in range(0,len(tovar)):
        temp3=[]
        temp3.append(tovar[i])
        temp3.append(0)
        temp3.append(0)
        temp2.append(temp3)
    tovar=temp2

#заполняем и считаем кол-во штук
    for i in range(0,len(baza)):
        for x in range(0,len(tovar)):
            if tovar[x][0]==baza[i][1]:
                tovar[x][1]+=int(baza[i][2])
                tovar[x][2]=float(baza[i][3])
#узнаем общую стоимость
    for i in range(0,len(tovar)):
        tovar[i][2]=tovar[i][1]*tovar[i][2]
        print("Товар",tovar[i][0],"купили",tovar[i][1],"шт, общей стоимостью",tovar[i][2],"руб.")

    print_result(customer,tovar)

if __name__=="__main__":
    main()