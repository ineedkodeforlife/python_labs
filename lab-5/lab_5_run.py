import unittest
from lab_4_1_1_Daughter_1 import *
from lab_4_1_1_Daughter_2 import *


class Positive(ValueError):
    pass


a, b = input(), input()


def summator(a, b):
    return a + b


class TestDivideFunction(unittest.TestCase):

    try:
        a, b = float(a), float(b)
        if a < 0 or b < 0:
            raise Positive('number must be positive')
    except Exception as e:
        print("Ошибка", e)
    else:
        p1 = Product(a, b)
        p2 = Lamp(12, 13, '4')
        p3 = Desk(1, 1, 1, 1)

    def test_summator(self):
        self.assertEqual(self.p1 + self.p2, self.p2.price + self.p1.price)
        # result = summator(self.p1, self.p2)
        # self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()


# print(p1 + p2)
# print(p1.get_info())
# print(p2.sale(50))
# print(p3.sale(20))


