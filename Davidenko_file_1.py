"""Прочитать текст из файла и вывести его на экран.
Проверить, есть ли в файле строки, начинающиеся и оканчивающиеся одним и
тем же символом."""


def printFile(file):
    for line in file:
        print(line, end='')


def isStartEndLine(file):
    for line in file:
        length = len(line)
        if length > 0:
            if line[length-1] == '\n':
                length -= 1
                line = line[:length]
            if length > 0:
                if line[0] == line[length-1]:
                    return True
    return False


f = open("Input.txt", 'r')
printFile(f)
print('\n')
f.seek(0)
if isStartEndLine(f):
    print("В файле есть строки, начинающиеся и оканчивающиеся одним и тем же символом")
else:
    print("В файле нет строк, начинающихся и оканчивающихся одним и тем же символом")
