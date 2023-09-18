class Product:
    def __init__(self, price, product_volume):
        if isinstance(price, (int, float)) and isinstance(product_volume, (int, float)):
            self.price = price
            self.product_volume = product_volume
        else:
            raise ValueError("Введите целые числа, для значений цены и объема")

    def sale(self, discount):
        if isinstance(discount, (int, float)):
            return self.price - round(self.price * (discount/100), 2)
        else:
            raise ValueError("Введите целое число для значения процента")

    def volume(self, depth, width, length):
        if isinstance(depth, (int, float)) and isinstance(width, (int, float)) and isinstance(length, (int, float)):
            return (depth * width * length) // self.product_volume
        else:
            raise ValueError("Введите целые числа")

    def get_info(self):
        return self.__str__()

    def __add__(self, other):
        return self.price + other.price

    def __str__(self):
        return f'Цена продукта: {self.price}, объем одной единицы продукта: {self.product_volume}'



