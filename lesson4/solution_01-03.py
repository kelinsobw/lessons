#Дан список my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 
#выведите все элементы, которые меньше 5.

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list=[]
for i in range(0,len(my_list)):
    if my_list[i]<5:
        new_list.append(my_list[i])
print(new_list)


#Ввести с клавиатуры строку, проверить является ли строка 
# палиндромом и вывести результат (yes/no) на экран. 
# Палиндром - это слово или фраза, которые одинаково 
# читаются слева направо и справа налево

polindrom=True
stroka=str(input())
stroka=list(stroka)
for i in range(0, len(stroka)):
    if stroka[i]!=stroka[i*(-1)-1]:
        polindrom=False
if polindrom==True:
    print("Строка полиндром")
else:
    print("Строка не полиндром")

#Написать функцию xor_cipher, принимающая 2 аргумента: 
# строку, которую нужно зашифровать, и ключ шифрования, 
# которая возвращает строку, зашифрованную путем применения 
# функции XOR (^) над символами строки с ключом. Написать 
# также функцию xor_uncipher, которая по зашифрованной 
# строке и ключу восстанавливает исходную строку.

import random

#шифрование файла
#ord() – преобразование символа в код ASCII
#chr() – преобразование кода ASCII в символ
def xor_cipher(text,key):
    result = ""
    for i in range(0,len(text)):
        result=result+chr(ord(text[i])^ord(key[i]))
    return(result)

#дешифрование текста
def my_xor_uncipher(text_cr,key):
    result=""
    for i in range(0,len(text)):
        result=result+chr(ord(text_cr[i])^ord(key[i]))
    return(result)

text=input("Введите текст для шифрования:")
key=""
for i in range(0,len(text)):
    key=key+str(random.randint(0,9))
print("Ключ:",key)

text_shifr=xor_cipher(text,key)
print("Зашифрованный текст",text_shifr)
text_rasshifr=my_xor_uncipher(text_shifr,key)
print("Расшифрованный текст",text_rasshifr)
