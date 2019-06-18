"""Дана последовательность из n целых чисел. Найти наибольший элемент
и его номер среди элементов, следующих после первого нулевого элемента (если
таких элементов несколько, то первый из них)."""

print("Введите n")
n = int(input("n = "))
sequence = []

print("Введите %d целых чисел" % n)
for i in range(n):
    sequence.append(int(input()))

i = 0
for i in range(n):
    if sequence[i] == 0:
        break

if i == n:
    print("Нет нулевых элементов")
elif i == n - 1:
    print("Нулевой элемент последний")
else:
    i += 1
    indexMax = i
    maxElement = sequence[i]
    while i < n:
        if sequence[i] > maxElement:
            maxElement = sequence[i]
            indexMax = i
        i += 1

    print(maxElement)
    print(indexMax)
