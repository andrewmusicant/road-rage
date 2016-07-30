import numpy as np
import random


class Car:
    def __init__(self, position, decel_chance, car_in_front=None):
        self.acceleration = 2.0  # 2 m/s^2
        self.decel_chance = decel_chance
        self.max_velocity = 33.3  # m/s
        self.velocity = 0.0
        self.position = np.array([position, position + 5.0])
        self.velocity_list = []
        self.position_list = []

    def update_car(self, car_in_front, road):
        if random.random() < self.decel_chance:
            self.decelerate(car_in_front)
        else:
            self.accelerate(car_in_front)
        self.get_current_position(road)
        self.velocity_list.append(self.velocity)

    def accelerate(self, car_in_front):
        self.velocity += self.acceleration
        if self.velocity >= self.max_velocity:
            self.velocity = self.max_velocity
        self.check_distance_between_cars(car_in_front)

    def decelerate(self, car_in_front):
        self.velocity -= self.acceleration
        self.check_distance_between_cars(car_in_front)

    def check_distance_between_cars(self, car_in_front):
        distance_between = car_in_front.position[0] - self.position[1]
        if distance_between <= self.velocity:
            if self.velocity > car_in_front.velocity:
                self.velocity = car_in_front.velocity

    def get_current_position(self, road):
        self.position += self.velocity
        if self.position[1] >= road.length:
            self.position = self.position % road.length
        self.position_list.append(self.position[0])
