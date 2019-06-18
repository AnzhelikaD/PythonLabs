"""Дана строка. Подсчитать сколько раз в строке встречается каждый символ."""


def countEachChar(s):
    map = dict()
    for i in range(len(s)):
        if s[i] in map:
            map[s[i]] += 1
        else:
            map[s[i]] = 1
    return map


text = input("Введите текст ")
d = countEachChar(text)
for key, value in d.items():
    print(key, value, sep='-', end='  ')
