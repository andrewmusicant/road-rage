class Car:
    def __init__(self, position):
        self.mav_velocity = 33.3  # m/s
        self.acceleration = 2  # 2 m/s^2
        self.velocity = 0  #
        self.position = [position, position + 5]
