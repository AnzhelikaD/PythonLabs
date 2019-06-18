"""Найти значение выражения
0b101001 + 0o255 - 0x1E в десятичной, двоичной,
восьмеричной и шестнадцатиричной системах счисления."""

a, b, c = 0b101001, 0o255, 0x1e

value = a + b - c

formatText = "0b101001 + 0o255 - 0x1E ="

print(formatText, str(value))
print(formatText, bin(value))
print(formatText, oct(value))
print(formatText, hex(value))
