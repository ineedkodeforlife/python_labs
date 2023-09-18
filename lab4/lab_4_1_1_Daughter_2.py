from lab_4_1_1_Parent import Product


class Lamp(Product):
    def __init__(self, price, product_volume, light):
        Product.__init__(self, price, product_volume)
        self.light = light

    def __str__(self):
        return f'Цена продукта: {self.price}, объем одной единицы продукта: {self.product_volume}, цвет света: ' \
               f'{self.light}'

