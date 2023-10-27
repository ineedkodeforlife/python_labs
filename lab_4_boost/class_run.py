import pytest

from lab_4_1_1_Daughter_1 import *
from lab_4_1_1_Daughter_2 import *


class My_except(Exception):
    def __init__(self, *args):
        if isinstance(args[0], str) != True:
            raise ValueError("Вы ошиблись  при вводе марки")
        elif args[1].isdigit() == False:
            raise ValueError("Вы ошиблись при вводе размера топливного бака, размер должен быть числовым")


try:
    print("Введите марку машины и размер топливного бака")
    car_params = (input(), input())
    My_except(car_params[0], car_params[1])
    p1 = Car(car_params[0], int(car_params[1]))
except Exception as e:
    print(e)

try:
    print("Введите марку трактора и размер топливного бака")
    tract_params = (input(), input())
    My_except(tract_params[0], tract_params[1])
    p2 = Tractor(tract_params[0], int(tract_params[1]))
except Exception as e:
    print(e)

try:
    print("Введите марку элитной машины, размер топливного бака и ее стоимость в рублях")
    elite_car_params = (input(), int(input()), int(input()))
    p3 = EliteCar(*elite_car_params)
except Exception as e:
    print("Данные должны быть введены в формате ввод первого числа, энтер, ввод следующего, размер бакка должен быть"
          "числом, как и цена автомобиля")
    print(e)

try:
    print(p1 > p2)
    print(p1.get_info())
    print(p2.mean_consumption(50))
    print(p3.price_after_year(20))
except Exception as e:
    print('Перезапустите программу, и постарайтесь не ошибиться')


try:
    # Открываем файл для записи
    with open('output.txt', 'wb') as file:
        text = ' '.join(car_params)
        file.write(text.encode('utf-8'))

except Exception as e:
    print(e)


def test_car_creation():
    car = Car("Toyota", 50)
    assert car.car_name == "Toyota"
    assert car.oil_volume == 50


def test_tractor_creation():
    tractor = Tractor("John Deere", 100)
    assert tractor.tractor_name == "John Deere"
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
    assert car.get_info() == "Brand: Toyota, Fuel Tank Size: 50"


def test_tractor_mean_consumption():
    tractor = Tractor("John Deere", 100)
    assert tractor.mean_consumption(50) == 2


def test_elite_car_price_after_year():
    elite_car = EliteCar("Mercedes", 80, 1000000)
    assert elite_car.price_after_year(20) == 800000


def test_file_write():
    with open('output.txt', 'rb') as file:
        contents = file.read(13)
        contents = contents.decode('utf-8')
        assert contents == "Toyota 50"

