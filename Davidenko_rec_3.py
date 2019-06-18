""" В виде рекурсивных функций оформите: Проверку, верно ли, что заданная строка S состоит только из цифр."""


def isAllNums(s):
    if len(s) == 0:
        return True
    else:
        if s[0].isdigit():
            return isAllNums(s[1:])
        else:
            return False


text = input("Введите текст ")
if len(text) == 0:
    print("Пустая строка")
else:
    if isAllNums(text):
        print("Строка состоит только из цифр")
    else:
        print("Строка состоит не только из цифр")
