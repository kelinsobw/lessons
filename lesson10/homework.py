#Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure. 
#Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса; 
#методы: нахождение периметра и площади окружности), Triangle (атрибуты: три точки, 
#методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: 
#нахождение площади и периметра). При потребности создавать все необходимые методы 
#не описанные в задании. 

import math


class Point:
    def __init__(self, xy_1, xy_2, xy_3=None):
        self.xy_1=xy_1
        self.xy_2=xy_2
        self.xy_3=xy_3
        Figure.cout+=1
        Figure.items.append(self)


class Figure(Point):

    items=[]
    cout=0

    def __str__(self):
        return(f'Площадь состовляет {self.space()}, периметр: {self.perimeter()} усл.уд.')


class Circle(Figure):

    def space(self):
        return math.pi*self.xy_2*self.xy_2

    def perimeter(self):
        return 2*math.pi*self.xy_2*self.xy_2


class Triangle(Figure):
     
    def perimeter(self):
        a=math.sqrt(math.pow((self.xy_1[0]-self.xy_2[0]),2)+math.pow((self.xy_1[1]-self.xy_2[1]),2))
        b=math.sqrt(math.pow((self.xy_2[0]-self.xy_3[0]),2)+math.pow((self.xy_2[1]-self.xy_3[1]),2))
        c=math.sqrt(math.pow((self.xy_3[0]-self.xy_1[0]),2)+math.pow((self.xy_3[1]-self.xy_1[1]),2))
        return a+b+c

    def space(self):
        a=math.sqrt(math.pow((self.xy_1[0]-self.xy_2[0]),2)+math.pow((self.xy_1[1]-self.xy_2[1]),2))
        b=math.sqrt(math.pow((self.xy_2[0]-self.xy_3[0]),2)+math.pow((self.xy_2[1]-self.xy_3[1]),2))
        c=math.sqrt(math.pow((self.xy_3[0]-self.xy_1[0]),2)+math.pow((self.xy_3[1]-self.xy_1[1]),2))
        p=(Triangle.perimeter(self))/2
        
        s=math.sqrt(p*(p-a)*(p-b)*(p-c))
        return s


class Square(Figure):

    def perimeter(self):
        p=(self.xy_1[0]-self.xy_2[0])*2+(self.xy_1[1]-self.xy_2[1])*2
        return abs(p)

    def space(self):
        s=(self.xy_1[0]-self.xy_2[0])*(self.xy_1[1]-self.xy_2[1])
        return abs(s)

c_1=Circle([0,0],2)
c_2=Circle([2,4],5)

triangle_2=Triangle([2,4],[4,6],[9,2])
triangle_1=Triangle([1,1],[3,3],[1,3])
triangle_1=Triangle([1,1],[3,3],[2,4])
sqr=Square([2,1],[4,3])

#А вот и  список
mass=[Square([8,4],[6,2]), Square([5,2],[1,3])]

#Я изначально не правильно понял условие: создал не список объектов,
#а добовлял объекты в список:
[print(Figure.items[i]) for i in range(Figure.cout)]