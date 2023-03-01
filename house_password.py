"""
Стефан и София забывают о безопасности и используют простые пароли для всего. 
Помогите Николе разработать модуль для проверки паролей на безопасность. 
Пароль считается достаточно стойким, если его длина больше или равна 10 
символам, он содержит, как минимум одну цифру, одну букву в верхнем и одну в 
нижнем регистре. Пароль может содержать только латинские буквы и/или цифры.

Вх. данные: Пароль как строка (str, unicode).

Вых. данные: Безопасность пароля в виде булевого значения (bool) или любого 
типа данных, который может быть сконвертирован и представлен как булево 
значение (True или False)
"""

checkio = lambda p: not any((len(p) < 10, p.islower(), p.isupper(), p.isdigit(), p.isalpha()))
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"