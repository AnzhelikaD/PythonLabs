"""Дана строка, состоящая из нулей и единиц. Написать и вызвать функцию
для подсчета в тексте количества подстрок ’101’"""


def countSubstrings(s):
    substr = "101"
    count = 0
    while s.find(substr) != -1:
        count += 1
        startIdx = s.find(substr)
        s = s[startIdx + 1:]
    return count


string = input("Введите строку из нулей и единиц ")
print(countSubstrings(string))
