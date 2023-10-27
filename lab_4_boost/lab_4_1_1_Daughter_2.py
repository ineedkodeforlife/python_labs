from lab_4_1_1_Parent import Car


class EliteCar(Car):
    def __init__(self, car_name: str, oil_volume: (int, float), price: (int, float)):
        Car.__init__(self, car_name, oil_volume)
        if isinstance(price, (int, float)):
            self.price = price
        else:
            raise ValueError("Цена автомобиля должна быть числом")

    def price_after_year(self, year):
        return self.price * year
