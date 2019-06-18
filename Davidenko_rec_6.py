"""В виде рекурсивных функций оформите: Проверку, верно ли, что все числа в списке – положительные;"""


def isAllNumsPositive(lst):
    if len(lst) == 0:
        return True
    else:
        lastIdx = len(lst) - 1
        if lst[lastIdx] > 0:
            lst.pop()
            return isAllNumsPositive(lst)
        else:
            return False


n = int(input("Введите длину списка: "))
if n < 0:
    print("Ошибка: длина не может быть меньше 1")
else:
    nums = []
    print("Введите %d целых чисел" % n)
    for i in range(n):
        nums.append(int(input()))
    if isAllNumsPositive(nums):
        print("Все числа положительные")
    else:
        print("Не все числа положительные")
