"""Дан список целых чисел. Создать словарь, в который входят пары
(ключ/значение): число из списка и количество повторений числа.
Например, для списка L = [1, 2, 1, 2, 1, 2, 1] создается словарь: D = {1:4, 2:3}."""
import random


def countEachNum(listnum):
    map = dict()
    for num in listnum:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    return map


n = 10
random.seed()
nums = [random.randint(0, 9) for i in range(n)]
print("Исходный список: ", nums)
d = countEachNum(nums)
for key, value in d.items():
    print(key, value, sep='-', end='  ')
