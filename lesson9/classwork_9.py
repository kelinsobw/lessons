class Animal:
    def __init__(self, height, weight, name, age):  
        self.height=height
        self.weight=weight
        self.name=name
        self.age=age
    
    def print_name(self):
        print(f'Имя: {self.name}')

    def jump(self):
        print(f'{self.name} to jump')

    def run(self):
        print(f'{self.name} to run')


    def change_name(self,name):
        self.name=name



class Dog(Animal):

    def bark(self):
        print(f'{self.name} to bark')

class Cat(Animal):

    def meow(self):
        print(f'{self.name} to meow')



first_dog=Dog(30,3.5,"Businka",1)
first_dog.jump()
first_dog.run()
first_dog.bark()
first_dog.print_name()
first_dog.change_name("Eli")
first_dog.print_name()

first_cat=Cat(20,2,"Rishik",2)
first_cat.meow()
first_cat.jump()
first_cat.print_name()
first_cat.change_name("Chernish")
first_cat.print_name()

