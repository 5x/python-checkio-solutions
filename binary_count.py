"""
Дано положительное целое число. Вам необходимо сконвертировать его в двоичную 
форму и подсчитать сколько единиц в написании данного числа. 
Для примера: 5 = 0b101 содержит две единицы, так что ответ 2.

Вх. данные: Число как положительное целочисленное (int).
Вых. данные: Число единиц в двоичной форме данного числа (int).
"""

def checkio(number):
    return bin(number).count('1')
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9