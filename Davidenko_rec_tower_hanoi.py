""""Переписать «Пример 2. Ханойские башни» на Python.
Перепишите рекурсивную процедуру, заменив условный оператор на “if n=0
then ...”."""


def tower(fromt, auxt, tot, n):
    if n == 1:
        print(fromt, " -> ", tot)
    else:
        tower(fromt, tot, auxt, n-1)
        print(fromt, " -> ", tot)
        tower(auxt, fromt, tot, n-1)


def tower2(fromt, auxt, tot, n):
    if n == 0:
        return
    else:
        tower2(fromt, tot, auxt, n - 1)
        print(fromt, " -> ", tot)
        tower2(auxt, fromt, tot, n - 1)


tower('A', 'B', 'C', 5)
print()
tower2('A', 'B', 'C', 5)
