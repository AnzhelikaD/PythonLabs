import recModul.recursion

text = input("Введите текст ")
if len(text) == 0:
    print("Пустая строка")
else:
    if recModul.recursion.isAllNums(text):
        print("Строка состоит только из цифр")
    else:
        print("Строка состоит не только из цифр")

n = int(input("Введите длину списка: "))
if n < 0:
    print("Ошибка: длина не может быть меньше 1")
else:
    nums = []
    print("Введите %d целых чисел" % n)
    for i in range(n):
        nums.append(int(input()))
    if recModul.recursion.isAllNumsPositive(nums):
        print("Все числа положительные")
    else:
        print("Не все числа положительные")
