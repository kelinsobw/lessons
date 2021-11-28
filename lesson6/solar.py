import math

def area(s):
    panels=[]
    s_ost=s
    while s_ost>=4:
        side_1=int(math.sqrt(s))
        panels.append(side_1)
        side_ost=math.sqrt(s)- side_1
        prjamoug_1=[math.sqrt(s),math.sqrt(s)-side_1]
        prjamoug_2=[side_1,math.sqrt(s)-side_1]
        s_ost=prjamoug_1[0]*prjamoug_1[1]+prjamoug_2[0]*prjamoug_2[1]
        s=s_ost
        print("  ")
        print("Выерезаем квадрат",side_1,"*",side_1)
        print("Остается 2 куска размерами",prjamoug_1,"и",prjamoug_2)

    for i in range(int(s_ost)+1):
        s_ost-=1
        panels.append(1)
        print(" ")
        print("Выерезаем квадрат 1 * 1")
        print("Остается 2 куска размерами",prjamoug_1,"и",prjamoug_2)

    print([i for i in panels])
    panels=[i*i for i in panels]
    return(panels)




s=int(input("Введите площадь панели:"))
panels=area(s)
print(panels)