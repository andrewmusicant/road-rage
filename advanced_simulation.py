import statistics as st

from advanced_road import Road


class Simulation:
    def __init__(self):
        self.t_max = 60
        self.d_time = 1  # time interval
        self.time = 0
        self.decel_chance = [0.1]  # [0.1, 0.4, 0.1, 1.0, 0.1, 0.2, 0.1]

    def get_final_velocity(self):
        total_car_list = []
        for percentage in self.decel_chance:
            road = Road(percentage)
            car_list = road.populate_road()
            while self.time <= self.t_max:
                for index, car in enumerate(car_list):
                    if index >= len(car_list) - 1:
                        car_list[index].update_car(car_list[0], road)
                    else:
                        car_list[index].update_car(car_list[index+1], road)
                self.time += self.d_time
            total_car_list.append(car_list)
        return total_car_list

    def get_car_means(car_list):
        car_means = []
        for car in car_list:
            car_means.append(st.mean(car.velocity_list))
        return car_means

    def get_speed_limit(car_means):
        total_mean = st.mean(car_means)
        stdev = st.pstdev(car_means)
        speed_limit = total_mean + stdev
        return speed_limit

    def get_multiple_sims():
        loop_set = []
        car_means = []

        for _ in range(100):
            sim = Simulation()
            car_list = sim.get_final_velocity()

            for car in car_list:
                # Looking at 30-60 second range for speed limit calculation
                car_means.append(st.mean(car.velocity_list[30:]))
            loop_set.append(car_list)

        total_mean = st.mean(car_means)
        stdev = st.pstdev(car_means)
        speed_limit = total_mean + stdev
        return total_mean, speed_limit, loop_set


def main():
    pass

if __name__ == '__main__':
    main()
