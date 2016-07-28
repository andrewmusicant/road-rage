from road import Road
from car import Car

class Simulation:
    def __init__(self):
        self.t_max = 60
        self.d_time = 1  # time interval
        self.time = 0


def main():
    road = Road()
    car_list = road.populate_road()
    for car in car_list:
        print(car.position)

if __name__ == '__main__':
    main()
