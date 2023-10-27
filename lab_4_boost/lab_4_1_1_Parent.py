from datetime import datetime


class Car:
    def __init__(self, car_name: str, oil_volume: int):
        if isinstance(car_name, str) and isinstance(oil_volume, (int, float)):
            self.car_name = car_name
            self.oil_volume = oil_volume
            self.remaining_oil = 0
            self.lst_data = []
        else:
            raise ValueError("Введите марку автомобиля, и объем бензобака в литрах")

    def refill(self, liters_oil: int):
        if isinstance(liters_oil, (int, float)):
            if self.remaining_oil + liters_oil <= self.oil_volume:
                self.remaining_oil += liters_oil
                self.lst_data.append((datetime.now(), liters_oil))
            else:
                raise ValueError("Вы переполнили бензобак")
        else:
            raise ValueError("Введите целое число для значения литров бензина")

    @staticmethod
    def mean_consumption(kilometer: (int, float)):
        if isinstance(kilometer, (int, float)):
            return f'Примерная трата бензина {kilometer * 8.2}'

    def get_info(self):
        if len(self.lst_data) > 0:
            return self.__str__()
        else:
            return "Заправок еще не было"

    def __str__(self):
        return f'Последние заправки были в числах {self.lst_data[:10][0]}, каждый раз было : ' \
               f'{self.lst_data[:10][1]} литров'

    def __lt__(self, other):
        return self.oil_volume < other.oil_volume
