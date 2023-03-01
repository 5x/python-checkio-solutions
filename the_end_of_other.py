"""
Дан набор слов в нижнем регистре. Проверьте есть ли в этом наборе пара слов, 
такая что одно слово заканчивается другим (суффикс или совпадение). 
Для примера: {"hi", "hello", "lo"} -- "lo" это окончание "hello", так что 
результат True.
Замечания: Для этой задачи вы можете прочитать о типе данных set и 
строковых функциях.

Вх. данные: Слова как набор (set) строк (str).
Вых. данные: True или False, как булево выражение.
"""

def checkio(w):
    return any([j for j in w if i != j and i.endswith(j)] for i in w)
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"