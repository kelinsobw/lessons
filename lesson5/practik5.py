import random
#Написать функцию, которая получает на вход имя и 
#выводит строку вида: f"Hello, {name}". Создать список из 
#5 имен. Вызвать функцию для каждого элемента списка в цикле.

'''def print_name(name):
    print(f"Hello, {name}")

    
list_name=[]
for i in range(0,5):
    list_name.append(str(input("Введите имя " + str(i+1)+": ")))
for i in range(0,len(list_name)):
    print_name(list_name[i])'''


#Создать функцию, которая принимает на вход неопределенное 
#количество аргументов и возвращает их сумму и максимальное 
#из них.


'''def okol(*elements):
    summa=0
    max=elements[0]
    for i in elements:
        summa=summa+i
        if i>max:
            max=i

    return(summa,max)

summa,max=okol(random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)) 
print(summa)
print(max)'''


#Написать функцию принимающая на вход неопределенным количеством аргументов и именованный 
#аргумент func_type. В зависимости от func_type вернуть минимальное либо максимальное значение. 
#Написать программу в виде трех функций.

'''def opredelit(*args,**kwargs):
    if kwargs.get('func_type')=="mine":
        result=mine(args)
    if kwargs.get('func_type')=="maxe":
        result=maxe(args)
    return result

def mine(elements):
    min=elements[0]
    print(elements)
    for i in range(len(elements)):
        if int(elements[i]) <min:
            min=elements[i]
    return min


def maxe(elements):
    max=elements[0]
    for i in range(len(elements)):
        if int(elements[i]) >max:
            max=elements[i]
    return max


result= opredelit(1,2,4,5,7,-1,func_type="maxe")
print(result)'''


#Написать функцию month_to_season(), которая принимает 
#1 аргумент - номер месяца - и возвращает название сезона, 
#к которому относится этот месяц. Например, передаем 2, 
#на выходе получаем "Winter".

def month_to_season(nomer_m):
    slovar={0:"leto",1:"osen",2:"zima",3:"vesna"}
    return slovar.get(nomer_m)

print(month_to_season(int(input("Номер сезона: "))))