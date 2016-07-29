from car import Car
from road import Road
import numpy as np

def test_get_current_position():
    car = Car(10)
    road = Road()
    car.get_current_position(road)
    assert (car.position == np.array([10,15])).all()


def test_accelerate():
    car1 = Car(0)
    car2 = Car(50)
    car1.accelerate(car2)
    assert car1.acceleration == 2
    assert car1.velocity == 2


def test_check_distance_between_cars():
    car1 = Car(0)
    car2 = Car(9)
    car1.accelerate(car2)
    assert car1.velocity == 2
    car1.accelerate(car2)
    assert car1.velocity == 0
