"""Дано действительное x . Вычислить приближенное значение бесконечной суммы"""


def infSum(x, exp):
    elem = x
    step = 1
    sumElems = elem if abs(elem) > exp else 0
    while abs(elem) > exp:
        step += 2
        elem = x**step / step
        sumElems += elem
    return sumElems


x = float(input("Введите действительное число x "))
exp = float(input("Введите действительное число exp "))
if abs(x) >= 1:
    print("Ошибка: |x| >= 1")
elif exp < 0:
    print("Ошибка: exp < 0")
else:
    print(infSum(x, exp))
