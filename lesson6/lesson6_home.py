#Напишите программу, которая принимает текст и 
#выводит два слова: наиболее часто встречающееся и самое длинное.


#"считем слова от 4 символов и более'
file=open("text_home.txt","r")
text=file.read()
text_v2=""
for i in text:
    if i not in "!21,?;:-.()@'/n" and i!='\n':
        text_v2+=i.lower()
    else: text_v2+=" "
words=[]
temp_word=""
for i in text_v2:
    if i not in " ":
        temp_word+=i
    else:
        words.append(temp_word)
        temp_word=""
max_lengh=0
max_word_l=""
max_cout=0
max_word_c=""
for word in words:
    if len(word)>max_lengh:
        max_lengh=len(word)
        max_word_l=word
    if max_cout<words.count(word) and len(word)>=4:
        max_cout=words.count(word)
        max_word_c=word
print("Болше всего встретилось слово   ---", max_word_c,".---    В тексте оно упомянулось", max_cout,"раз(а).")
print("Одно из самых длинных слов    ---", max_word_l, "---   состоит из",max_lengh,"символов.")
file.close()


#В школе решили набрать три новых класса по программированию. 
#Так как занятия по у них проходят в одно и то же время, было 
#решено выделить кабинет для каждого класса и купить в них новые парты. 
#За каждой партой может сидеть не больше двух учеников. Известно 
#количество учащихся в каждом из трёх классов. Сколько всего нужно закупить 
#парт чтобы их хватило на всех учеников? Программа получает на вход три 
#натуральных числа: количество учащихся в каждом из трех классов.

'''import math

a, b, c = (int(input("Количество учеников в классе: ")) for _ in range(3))
print("Необходимо купить",sum([(math.ceil(i/2)) for i in (a,b,c)]))'''
