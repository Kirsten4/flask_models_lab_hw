from models.order import *
from datetime import date


order_1 = Order("Kirsten", date(2021,11,22), 3, "Galaxy", False)
order_2 = Order("David", date(2021,10,13), 2, "Lindt", True)
order_3 = Order("Linda", date(2021,10,7), 4, "Milkybar", False)

orders=[order_1,order_2,order_3]