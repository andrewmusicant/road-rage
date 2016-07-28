import numpy as np

class Car:
    def __init__(self, position, car_in_front=None):
        self.mav_velocity = 33.3  # m/s
        self.acceleration = 2  # 2 m/s^2
        self.velocity = 0
        self.position = np.array([position, position + 5])

    def update_car(self):
        self.velocity += self.acceleration
        self.position += self.velocity
