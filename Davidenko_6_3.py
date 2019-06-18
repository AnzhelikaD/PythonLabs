"""Выяснить, является ли данный текст десятичной записью целого числа."""


def isInteger(s):
    if s[0] == "-":
        s = s[1:]
        if s == "":
            return False
    for i in range(len(s)):
        if not s[i] in '0123456789':
            return False
    return True


def isIntegerPythonMethods(s):
    if s[0] == "-":
        s = s[1:]
    return s.isdigit()


text = input("Введите текст ")
if text == "":
    print("Ошибка: Пустая строка")
else:
    if isInteger(text):
        print("Это целое число")
    else:
        print("Это не целое число")

    if isIntegerPythonMethods(text):
        print("Это целое число")
    else:
        print("Это не целое число")
