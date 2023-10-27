import pytest

from lab_4_1_1_Daughter_1 import *
from lab_4_1_1_Daughter_2 import *
from class_run import My_except

def test_car_creation():
    car = Car("Toyota", 50)
    assert car.car_name == "Toyota"
    assert car.oil_volume == 50


def test_tractor_creation():
    tractor = Tractor("John Deere", 100)
    assert tractor.car_name == "John Deere"
    assert tractor.oil_volume == 100


def test_elite_car_creation():
    elite_car = EliteCar("Mercedes", 80, 1000000)
    assert elite_car.car_name == "Mercedes"
    assert elite_car.oil_volume == 80
    assert elite_car.price == 1000000


def test_my_except_with_valid_arguments():
    try:
        My_except("Toyota", "50")
    except ValueError:
        pytest.fail("Unexpected ValueError raised")


def test_my_except_with_invalid_arguments():
    with pytest.raises(ValueError):
        My_except(123, "50")


def test_car_comparison():
    car1 = Car("Toyota", 50)
    car2 = Car("Honda", 40)
    assert car1 > car2


def test_car_get_info():
    car = Car("Toyota", 50)
    assert car.get_info() == "Заправок еще не было"


def test_tractor_mean_consumption():
    tractor = Tractor("John Deere", 100)
    assert tractor.mean_consumption(50) == 'Примерная трата бензина 2000'


def test_elite_car_price_after_year():
    elite_car = EliteCar("Mercedes", 80, 1000000)
    assert elite_car.price_after_year(20) == 20000000


# def test_file_write():
#     with open('output.txt', 'rb') as file:
#         contents = file.read(13)
#         contents = contents.decode('utf-8')
#         assert contents == "1 1"
