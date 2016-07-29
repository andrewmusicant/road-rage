from car import Car


class Road:
    def __init__(self):
        self.length = 1000  # equals 1km
        self.car_list = []
        self.number_of_cars = 30

    def populate_road(self):
        pos = 0
        for _ in range(self.number_of_cars):
            self.car_list.append(Car(pos))
            pos += (self.length / self.number_of_cars)
        return self.car_list
