"""Даны целые a , b . Получить значения выражений
u = min( a; b ); v = min( ab; a + b ); w = min( u + v 2 ; 14) :"""


def minimum(x, y):
    return x if x < y else y


print("Введите 2 целых числа")
a = int(input("a = "))
b = int(input("b = "))

u = minimum(a, b)
v = minimum(a * b, a + b)
w = minimum(u + v*v, 14)

print("u = ", u)
print("v = ", v)
print("w = ", w)
