from lab_4_1_1_Daughter_1 import *
from lab_4_1_1_Daughter_2 import *

p1 = Product(12, 15)
p2 = Lamp(12, 13, '4')
p3 = Desk(1, 1, 1, 1)

print(p1 + p2)
print(p1.get_info())
print(p2.sale(50))
print(p3.sale(20))
