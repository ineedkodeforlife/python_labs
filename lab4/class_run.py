from lab_4_1_1_Daughter_1 import *
from lab_4_1_1_Daughter_2 import *

p1 = Car('12', 15)
p2 = Tractor('12', 13)
p3 = EliteCar('1', 1, 1)

print(p1 > p2)
print(p1.get_info())
print(p2.mean_consumption(50))
print(p3.price_after_year(20))
