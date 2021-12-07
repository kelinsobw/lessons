class Car:
    def __init__(self,marka,model,god,speed=0):
        self.marka=marka
        self.model=model
        self.god=god
        self.speed=speed

    def speed_up(self):
        self.speed+=5

    def speed_down(self):
        self.speed-=5

    def speed_stop(self):
        self.speed=0

    def print_speed(self):
        print(f'Скорость: {self.speed}')

    def speed_back(self):
        self.speed*=-1