"""
Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как 
они встречаются в куске текста.

Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем 
все заглавные буквы, то получим сообщение "HELLO".

Входные данные: Текст как строка (юникод).
Выходные данные: Секретное сообщение как строка или пустая строка.
"""

def find_message(text):
    """Find a secret message"""
    return ''.join([i for i in text if i.isupper()])
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"