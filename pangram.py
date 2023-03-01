"""
Панграмма (Греческий:παν γράμμα, pan gramma, "каждая буква") или предложение 
состоящее из разных букв алфавита, используя каждую букву по крайней мере один
раз.

Для этого задания, вы будете использовать латинский алфавит (A-Z). 
У вас есть текст с латинскими буквами и знаками препинания. 
Вы должны проверить является ли предложение панграммой или нет. 
Регистр не имеет значения.

Входные данные: Текст как строка.
Выходные данные: Является предложение панграммой или нет как логическое.
"""

from string import ascii_lowercase
​
def check_pangram(text):
    return ascii_lowercase in ''.join(sorted(set(text.lower())))
​
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"