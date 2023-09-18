from lab_4_1_1_Parent import Product


class Desk(Product):
    def __init__(self, price, product_volume, wood, amount):
        Product.__init__(self, price, product_volume)
        if isinstance(amount, int) and amount > 0:
            self.wood = wood
            self.amount = amount
        else:
            raise ValueError("Количество должно быть положительным целым числом")

    def sale(self, discount):
        return Product.sale(self, discount) * self.amount

    def __str__(self):
        return f'Цена продукта: {self.price}, объем одной единицы продукта: {self.product_volume}, название дерева' \
               f'использумовоего как материал: {self.wood}, количество парт: {self.amount}'



