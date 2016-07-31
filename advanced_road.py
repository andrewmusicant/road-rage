from advanced_car import Car


class Road:
    def __init__(self, decel_chance):
        self.length = 1000.0  # equals 1km
        self.car_list = []
        self.number_of_cars = 30
        self.decel_chance = decel_chance  # [0.1, 0.4, 0.1, 1.0, 0.1, 0.2, 0.1]

    def populate_road(self):
        pos = 0.0
        for _ in range(self.number_of_cars):
            self.car_list.append(Car(pos, self.decel_chance))
            pos += (self.length / self.number_of_cars)
        return self.car_list
