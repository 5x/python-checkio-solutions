"""
Дан массив целых чисел. Нужно найти сумму элементов с четными индексами 
(0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного 
массива. Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 (ноль).

Входные данные: Список (list) целых чисел (int).
Выходные данные: Число как целочисленное (int).
"""

def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    return array[-1] * sum(array[::2]) if array else 0
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
