import matplotlib.pyplot as plt
import matplotlib.animation as animation

from road import Road
from car import Car


class Simulation:
    def __init__(self):
        self.t_max = 60
        self.d_time = 1  # time interval
        self.time = 0

    def get_final_velocity(self):
        road = Road()
        car_list = road.populate_road()
        while self.time <= self.t_max:
            for index, car in enumerate(car_list):
                if index >= len(car_list) -1:
                    car_list[index].update_car(car_list[0], road)
                else:
                    car_list[index].update_car(car_list[index+1], road)
            self.time += self.d_time
        return car_list


def main():
    sim = Simulation()
    car_list = sim.get_final_velocity()
    for car in car_list:
        plt.plot(car.velocity_list)
        plt.title(car)
    plt.show()

if __name__ == '__main__':
    main()
