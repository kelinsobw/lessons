#   Дано выражение x = 2 + 2 * 2 - 2 / 2, расставить скобки таким образом, 
#чтобы значение x было равно 2, найти два варианта решения задачи.

x = (2 + 2 * 2 - 2) / 2
print(x)

x = (2 + (2 * 2 - 2)) / 2
print(x)


'''Пользователь делает вклад в размере 2130 рублей сроком на 5 лет под 10% годовых
(каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к 
сумме вклада, и на них в следующем году тоже будут проценты). Рассчитать сумму 
на счету пользователя по окончании вклада и вывести на печать, если в конце 
каждого года ему начисляется бонус в размере 120 рублей.'''


vklad=2130
year=5
procent=0.1
for i in range(0,year):
    vklad=vklad*procent+vklad+120
print("После пяти лет стало",int(vklad),"рублей.")


#Создать список состоящий из отдельных единичных символов, преобразовать список 
#в строку, инвертировать строку и вывести на печать.


spisok=[9,2,4,5,'a','s','d','f','g','h','j','k','i',3,4,7,8,2]
new_str="".join(str(x) for x in spisok)
print("Было:",spisok)
print("Стало:",new_str[::-1])