"""
Продолжим изучение слов. Даны две строки со словами, разделенными запятыми. 
Попробуйте найти что общего между этими строками. Слова внутри каждой строки 
не повторяются.

Ваша функция должна находить все слова, которые появляются в обеих строках. 
Результат должен быть представлен, как строка со словами разделенными запятыми
и отсортированными в алфавитном порядке.

Вх. данные: Два аргумента как строки (str).
Вых. данные: Общие слова как строка (str).
"""

def checkio(first, second, sep=','):
    return sep.join(sorted(set(first.split(sep)) & set(second.split(sep))))
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
