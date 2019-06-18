"""Найти значение выражения
0o100 * 8 + 0o100 / 8 в десятичной, двоичной, восьмеричной и шестнадцатиричной системах счисления."""

a, b = 0o100, 8

value = a * b + a // b

formatText = "0o100 * 8 + 0o100 / 8 ="

print(formatText, str(value))
print(formatText, bin(value))
print(formatText, oct(value))
print(formatText, hex(value))
