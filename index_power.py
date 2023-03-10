"""
Дан массив с положительными числами и число N. Вы должны найти N-ую степень 
элемента в массиве с индексом N. Если N за границами массива, тогда 
вернуть -1. Не забывайте, что первый элемент имеет индекс 0.

Давайте посмотрим на несколько примеров:
- массив = [1, 2, 3, 4] и N = 2, тогда результат 32 == 9;
- массив = [1, 2, 3] и N = 3, но N за границами массива, так что результат -1.

Входные значения: Два агумента. Массив как список целых и число как целое.
Выходные значения: Целое число.
"""

def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    return array[n] ** n if n < len(array) else -1
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"