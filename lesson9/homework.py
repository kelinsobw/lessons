from class_car import Car


if __name__=="__main__":
    my_car=Car("Mercedes","E500",2000)

    while my_car.speed<100:
        my_car.speed_up()

    my_car.print_speed()
