#задание 1

'''def account(way,days):
    days.append(days[-1]+days[-1]*1.1)
    if days[-1]>=way: return days 
    return account(way,days)


if __name__=="__main__":
    way=int(input("Весь маршрут в км: "))
    days=[]
    days.append(int(input("Пробежал в первый день: ")))
    result=len(account(way,days))
    print(f"Весь маршрут пройден за {result} дня.")
'''
#задание 2

'''subsequence=[1, 2, 2, 2, 2, 2, 2, 3, 7, 2, 2, 7, 4, 4, 4, 0, 5, 5, 5]
subsequence=subsequence[:subsequence.index(0)]
max_repeat=1
result_max=1
max_repeat_name=subsequence[0]
for i in range(1,len(subsequence)):
    if subsequence[i]==subsequence[i-1]:
        max_repeat+=1
        if result_max<max_repeat:
            result_max=max_repeat
            max_repeat_name=subsequence[i]
    else:
        max_repeat=1

print(f"Число {max_repeat_name} повторилось {result_max} раз.")'''


#задание 3. Использовалась инструкция https://www.youtube.com/watch?v=rFuQCd4RvI0 


def hanoi(n,i,k):
    if n==1:
        print(f"Перекидываем диск {n} с {i} стержня на {k}.")
    else:
        tmp=6-i-k
        hanoi(n-1,i,tmp)
        print(f"Перекидываем диск {n} с {i} стержня на {k}.")
        hanoi(n-1,tmp,k)

disks=int(input("Количество дисков: "))
hanoi(disks,1,3)
