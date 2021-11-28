import math

def area(s):
    panels=[]
    s_ost=s
    while s_ost>=4:
        side_1=int(math.sqrt(s))
        panels.append(side_1)
        prjamoug_1=[math.sqrt(s),math.sqrt(s)-side_1]
        prjamoug_2=[side_1,math.sqrt(s)-side_1]
        s_ost=s_ost-side_1**2
        s=s_ost
        print("  ")
        print("Выерезаем квадрат",side_1,"*",side_1)
        print("Остается 2 куска размерами",prjamoug_1,"и",prjamoug_2)
        print("Общей площадью:", s_ost)

    print("И добавляем ", int(s_ost),"панель(и) размерами 1*1.")
    for i in range(int(s_ost)):
        s_ost-=1
        panels.append(1)

    print([i for i in panels])
    panels=[i*i for i in panels]
    return(panels)

#изначально предполагаем что панель квадратная
s=int(input("Введите площадь панели:"))
panels=area(s)
print("Количество панелей:",len(panels),",размерами:",[str(i)+"кв.ярд." for i in panels])