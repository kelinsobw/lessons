import random
import requests
import os

#Создайте функцию three_args(), которая принимает 
#1, 2 или 3 ключевых параметра.  В результате ее 
#работы на печать выводятся значения переданных переменных, 
#но только если они не равны None. Получим, например, следующее 
#сообщение: Переданы аргументы: var1 = 2, var3 = 10.

'''def three_args(a=None,b=None,c=None):
    mass=""
    if a!=None:
        mass=mass+str("var1="+str(a)+", ")
    if b!=None:
        mass=mass+str("var2="+str(b)+" ")
    if c!=None:
        mass=mass+str("var3="+str(c))
    return mass

print(three_args(a=1,c=3))'''


#Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с именами участников. 
#Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент. Ваша программа 
#должна используя список имен участников выдать на выходе пары, кто и кому будет дарить, причем сам себе человек не может подарить, 
#дубликаты тоже не допустимы.

def santa(persons):
    print(persons)
    itog={}
    for i in range(0,len(persons)):
        cel_santi=random.choice((persons[0:i]+persons[i+1:]))
        itog[persons[i]]=cel_santi
    return itog

persons=('Kiril', 'Olga', 'Maria', 'Oleg', 'Mihail')
itog=santa(persons)
count=1
while itog.setdefault(persons[-1])==persons[-1]:
    count+=1
    itog=santa(persons)
print(itog)
print(count)


#Написать функцию, которая используя модуль requests скачивает файл сохраняет его на файловой системе, функция имеет два параметра: 
# ссылка на файл и имя на файловой системе. В качестве примера ссылки на файл можно использовать лицензию из ГитХаба из вашего 
# репозитория: https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE

'''def dow_and_save(url,path):
    r = requests.get(url)
    with open(path,'wb') as f:
        f.write(r.content)

url="https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE"
path="/home/kelinso/Документы/file7.txt"
dow_and_save(url,path)'''