# python-checkio-solutions

Some solutions for coding challenges on [https://checkio.org/](https://checkio.org/).


## Solutions

### [absolute_sorting.py](absolute_sorting.py)
Массив (`tuple`) содержит различные числа. Вам необходимо отсортировать их, но 
отсортировать на основе абсолютных значений в возрастающем порядке. Для 
примера, последовательность (-20, -5, 10, 15) будет отсортирована следующим 
образом (-5, 10, 15, -20). Ваша функция должна возвращать список (`list`) или 
кортеж (`tuple`).

Входные данные: Массив чисел как кортеж (`tuple`).
Выходные данные: Список (`list`) или кортеж (`tuple`) (но не генератор) 
отсортированный по абсолютным значениям чисел.

### [binary_count.py](binary_count.py)
Дано положительное целое число. Вам необходимо сконвертировать его в двоичную 
форму и подсчитать сколько единиц в написании данного числа. 
Для примера: 5 = 0b101 содержит две единицы, так что ответ 2.

Вх. данные: Число как положительное целочисленное (int).
Вых. данные: Число единиц в двоичной форме данного числа (int).

### [boolean_algebra.py](boolean_algebra.py)
В матаматике и математической логике, Булева алгебра это подраздел алгебры в 
котором значения переменных истинны или ложны и обычно обозначенны 0 или 1 
соответственно. В отличии от простой алгебры где значение переменных это числа 
и основные операции это сложение и умножение, основные операции Булевой 
алегбры это конъюнкция (обозначенная ∧), дизъюнкция (обозначенная ∨) и 
отрицание (обозначенное ¬).

В этой миссии вам нужно реализовать несколько булевых операций:
- "конъюнкция" ("conjunction") обозначенная x ∧ y, удовлетворяющая условиям 
x ∧ y = 1 если x = y = 1 и  ∧ y = 0 иначе.
- "дизъюнкция" ("disjunction") обозначенная x ∨ y, удовлетворяющая условиям 
x ∨ y = 0 если x = y = 0 и x ∨ y = 1 иначе.
- "импликация" ("implication") (прямая импликация) обозначенная x→y и 
описанная как ¬ x ∨ y. Если x это истина, тогда значение x → y берется 
такое как у y. Но если x ложь, тогда значение y может быть игнорированно.
- "исключение" ("exclusive") (исключающее ИЛИ) обозначенное x ⊕ y и описанное 
как (x ∨ y)∧ ¬ (x ∧ y). Это исключает вероятность обоих x и y. В терминах 
арифметики, это сложение по модулю 2, где 1 + 1 = 0.
- "эквивалентность" ("equivalence") обозначенная x ≡ y и описанная 
как ¬ (x ⊕ y). Это истина, когда x и y имеют одинаковые значения.
Здесь вы можете увидеть таблицу истинности для данных операций:
```
 x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
--------------------------------------
 0 | 0 |  0  |  0  |  1  |  0  |  1  |
 1 | 0 |  0  |  1  |  0  |  1  |  0  |
 0 | 1 |  0  |  1  |  1  |  1  |  0  |
 1 | 1 |  1  |  1  |  1  |  0  |  1  |
--------------------------------------
```
Даны два булевых значения x и y как 1 или 0 и дано имя операции, как 
описано ранее. Вы должны вычислить значение и вернуть его как 1 или 0.

Входные значения: Три аргумента. X и Y как 0 или 1. Имя операции, как строка.
Выходное значение: Результат как 1 или 0.

### [brackets.py](brackets.py)
Дано выражение с цифрами, скобками и операторами. 
В данной задаче важны только скобки. Скобки представлены в трех 
вариациях: "{}" "()" и "[]". Скобки используются, чтобы определить порядок 
применения операторов или ограничить участок выражения. Если скобка 
открывается, то она должна закрываться скобкой того же типа. Участки 
ограниченные одной парой скобок, не должны пересекаться с участками других 
скобок. В этой задаче, вам необходимо определить правильное ли выражение или 
нет, основываясь на расположении скобок. И не обращайте внимание на операторы 
и операнды.

Входные данные: Выражение для проверки, как строка (str, unicode).
Выходные данные: Решение, правильное выражение или нет, как булево значение.

### [building_base.py](building_base.py)
Сингулярность всё-таки наступила, и мы обязаны построить идеальный робо-город 
для наших повелителей. В этом сияющем робополисе все здания будут 
прямоугольными, а все улицы идти в направлениях "север-юг" и "восток-запад", 
образуя восхитительную решётку. Прежде чем начать строительство, мы должны 
создать класс, представляющий совершенное здание.

Так как все здания в городе прямоугольные, и их стены параллельны улицам, мы 
можем определить любое здание, используя только пару координат юго-западного 
угла, длину стен, идущих с запада на восток, длину стен, идущих с севера на 
юг, а также высоту здания. Эти значения выражены как положительные числа в 
обычных единицах измерения. Начало координат расположено в юго-западном углу 
города, следовательно, северные стороны зданий имеют значения координат 
больше, чем южные. Для решения этой задачи нам потребуется разработать 
несколько методов. Описание класса смотрите далее.
```
class Building(south, west, width_WE, width_NS, height=10)
```
Возвращает новый экземпляр класса Building (класса здания) с юго-западным 
углом расположенным в точке с координатами [south, west], длиной стен, 
идущих по направлению "восток-запад" - width_WE, длиной стен, идущих по 
направлению "север-юг" - width_NS, и высотой height. Параметр height 
является положительным числом со значением по умолчанию равным 10.
```
>>> Building(10, 10, 1, 2, 2)
Building(10, 10, 1, 2, 2)
>>> Building(0, 0, 10.5, 2.546)
Building(0, 0, 10.5, 2.546, 10)

corners()
```
Возвращает словарь (dictionary) с координатами углов здания. Словарь имеет 
следующие ключи: "north-west", "north-east", "south-west", "south-east". 
Значениями являются списки (list) или кортежи (tuples) с двумя числовыми 
значениями.
```
>>> Building(1, 2, 2, 2).corners()
{"north-west": [3, 2], "north-east": [3, 4], "south-west": [1, 2], 
"south-east": [1, 4]}

area()
```
Возвращает площадь основания здания.
```
>>> Building(1, 2.5, 4.2, 1.25).area()
5.25

volume()
```
Возвращает объем здания.
```
>>> Building(1, 2.5, 4.2, 1.25, 101).volume()
530.25

__repr__()
```
Это представление объекта Building в виде текстовой строки. 
Метод используется в функциях print или str (преобразование в строку). 
Возвращает строку следующего вида:
```
"Building({south}, {west}, {width_we}, {width_ns}, {height})"
>>> str(Building(0, 0, 10.5, 2.546))
"Building(0, 0, 10.5, 2.546, 10)"
```
Входные данные: операторы и выражения, использующие класс Building.
Выходные данные: поведение экземпляра как описано выше.

### [common_words.py](common_words.py)
Продолжим изучение слов. Даны две строки со словами, разделенными запятыми. 
Попробуйте найти что общего между этими строками. Слова внутри каждой строки 
не повторяются.

Ваша функция должна находить все слова, которые появляются в обеих строках. 
Результат должен быть представлен, как строка со словами разделенными запятыми
и отсортированными в алфавитном порядке.

Вх. данные: Два аргумента как строки (str).
Вых. данные: Общие слова как строка (str).

### [days_between.py](days_between.py)
Сколько вам лет в днях? Это легко вычислить - достаточно вычесть свой день 
рождения от сегодняшнего дня. Мы имеем реальную задачу - посчитать разницу 
между любыми датами.
У вас есть две даты в картежах с тремя числами - год, месяц и день. Например, 
19 апреля 1982 будет (1982, 4, 19). Вы должны найти разницу в днях между 
имеющимися датами. Например, между сегодня и вчера = 1 день. Разница между 
днями всегда будет положительной или нулем, не забывайте про абсолютное 
значение.

Входные данные: Две даты, как кортежи целых чисел.
Выходные данные: Разница между датами в днях, как целое число.

### [digits_multiplication.py](digits_multiplication.py)
Дано положительное целое число. Вам необходимо подсчитать произведение всех 
цифр в этом числе, за исключением нулей.
Для примера: Дано число 123405. 
Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).

Входные данные: Положительное целое число.
Выходные данные: Произведение цифр как целочисленное (int).

### [even-last.py](even-last.py)
Дан массив целых чисел. Нужно найти сумму элементов с четными индексами 
(0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного 
массива. Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 (ноль).

Входные данные: Список (list) целых чисел (int).
Выходные данные: Число как целочисленное (int).

### [friends_cls.py](friends_cls.py)
Create friends class.


### [house_password.py](house_password.py)
Стефан и София забывают о безопасности и используют простые пароли для всего. 
Помогите Николе разработать модуль для проверки паролей на безопасность. 
Пароль считается достаточно стойким, если его длина больше или равна 10 
символам, он содержит, как минимум одну цифру, одну букву в верхнем и одну в 
нижнем регистре. Пароль может содержать только латинские буквы и/или цифры.

Вх. данные: Пароль как строка (str, unicode).

Вых. данные: Безопасность пароля в виде булевого значения (bool) или любого 
типа данных, который может быть сконвертирован и представлен как булево 
значение (True или False)

### [index_power.py](index_power.py)
Дан массив с положительными числами и число N. Вы должны найти N-ую степень 
элемента в массиве с индексом N. Если N за границами массива, тогда 
вернуть -1. Не забывайте, что первый элемент имеет индекс 0.

Давайте посмотрим на несколько примеров:
- массив = [1, 2, 3, 4] и N = 2, тогда результат 32 == 9;
- массив = [1, 2, 3] и N = 3, но N за границами массива, так что результат -1.

Входные значения: Два агумента. Массив как список целых и число как целое.
Выходные значения: Целое число.

### [letter_queue.py](letter_queue.py)
В области информационных технологий, очередь это структура данных с принципом 
доступа к элементам «первый пришёл — первый вышел» (First In — First Out). 
Добавление элемента (принято обозначать словом "enqueue" — поставить в очередь
    или "push") возможно лишь в конец очереди, выборка — только из начала 
очереди (что принято называть словом "dequeue" — убрать из очереди или "pop"), 
при этом выбранный элемент из очереди удаляется. То есть чтобы добраться до 
нового добавленного элемента, нам надо "вытащить" элементы, которые были 
добавлены ранее.

Попробуем сделать модель очереди на Python. Вам дана последовательность команд:
- "PUSH X" -- поставить в очередь X, где X - это буква в верхнем регистре.
- "POP" -- убрать из начала очереди элемент. Если очередь пустая, то это 
команда ничего не делает.
Очередь содержит только буквы.

Вам необходимо обработать все команды и собрать все буквы, которые остались в 
очереди, в одно слово, от начала до конца очереди.

Рассмотрим пример. Дана последовательность команд:
```
["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]
Команда     Очередь Примечания
PUSH A      A       Добавили "A" в пустую очередь
POP                 Убрали "A"
POP                 Очередь уже пуста
PUSH Z      Z   
PUSH D      ZD  
PUSH O      ZDO 
POP         DO  
PUSH T      DOT     Результат
```
Входные данные: Последовательность команд, как список (list) строк (str).
Выходные данные: Содержание очереди, как строка (str).

### [median.py](median.py)
Медиана - это числовое значение, которое делит сортированый массив чисел на 
большую и меньшую половины. В сортированом массиве с нечетным числом элементов
медиана - это число в середине массива. Для массива с четным числом элементов,
где нет одного элемента точно посередине, медиана - это среднее значение двух 
чисел, находящихся в середине массива. В этой задаче дан непустой массив 
натуральных чисел. Вам необходимо найти медиану данного массива.

Входные данные: Массив как список (list) чисел (int).
Выходные данные: Медиана как число (int, float).

### [monkey-typing.py](monkey-typing.py)
Предположим, что наши обезьяны печтают, и печатают, и печатают, и уже 
настрочили множество разнообразных коротких отрывков текста. Давайте проверим 
их на вхождение осмысленных слов.

Вам предлагается некоторый текст, который может содержать осмысленные слова. 
Вы должны подсчитать количество таких слов в этом тексте. Слово может стоять 
отдельно, а может присутствовать как часть другого слова. Регистр букв не 
имеет значения. Слова даны в нижнем регистре и не повторяются. Если слово 
встречается в тексте несколько раз, оно должно быть посчитано только один раз.

Например, текст "How aresjfhdskfhskd you?", слова - ("how", "are", "you", 
	"hello"). Результат должен быть равен 3.

Вход: Два аргумента. Текст как строка (юникод в Python 2) и слова в виде 
	множества (set) строк (юникод в Python 2).
Выход: Количество слов в тексте в виде целого числа.

### [most-numbers.py](most-numbers.py)
Дан массив чисел (float или/и int). Вам нужно найти разницу между самым 
большим (максимум) и самым малым (минимум) элементом. Ваша функция должна 
уметь работать с неопределенным количеством аргументов. Если аргументов нет,
то функция возвращает 0 (ноль).

Числа с плавающей точкой представлены в компьютерах как двоичная дробь 
(прочитать здесь). Результат проверяется с точностью до третьего знака, 
как ±0.001
Прочитайте о том как работать с переменым числом аргументов.

Вх. данные: Переменное число аргументов как числа (int, float).
Вых. данные: Разница между максимумом и минимумом как число (int, float).

### [most-wanted-letter.py](most-wanted-letter.py)
Дан текст, который содержит различные английские буквы и знаки препинания. 
Вам необходимо найти самую частую букву в тексте. Результатом должна быть 
буква в нижнем регистре.
При поиске самой частой буквы, регистр не имеет значения, так что при подсчете 
считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, 
цифры и пробелы, а только буквы.

Если в тексте две и больше буквы с одинаковой частотой, тогда результатом 
будет буква, которая идет первой в алфавите. Для примера, "one" содержит "o", 
"n", "e" по одному разу, так что мы выбираем "e".

Вх. данные: Текст для анализа, как строка (str, unicode).
Вых. данные: Наиболее частая буква, как строка.

### [non_unique_elements.py](non_unique_elements.py)
Дан непустой массив целых чисел (X). В этой задаче вам нужно вернуть массив, 
состоящий только из неуникальных элементов данного массива. Для этого 
необходимо удалить все уникальные элементы (которые присутствуют в данном 
массиве только один раз). Для решения этой задачи не меняйте оригинальный 
порядок элементов. Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и 
результат будет [1, 3, 1, 3].

Вх. данные: Список (list) целых чисел (int).
Вых. данные: Список (list) целых чисел (int).

### [number_radix.py](number_radix.py)
Дано положительное число как строка и основание системы счисления для него. 
Ваша функция должна конвертировать это число в десятичную систему счисления. 
Основание системы счисления меньше 37 и больше 1. В задаче используются цифры 
и буквы A-Z внутри строчного представления числа.

Будьте осторожны со случаями, когда число нельзя сконвертировать. 
Для примера: "1A" не может быть сконвертировано при основании системы 
счисления 9. В этих случаях ваша функция должна возвращать -1.

Вх. данные: Два аргумента. Число как строка (str) и основание системы 
	счисления как целочисленное (int).
Вых. данные: Сконвертированное число как целочисленное (int).

### [pangram.py](pangram.py)
Панграмма (Греческий:παν γράμμα, pan gramma, "каждая буква") или предложение 
состоящее из разных букв алфавита, используя каждую букву по крайней мере один
раз.

Для этого задания, вы будете использовать латинский алфавит (A-Z). 
У вас есть текст с латинскими буквами и знаками препинания. 
Вы должны проверить является ли предложение панграммой или нет. 
Регистр не имеет значения.

Входные данные: Текст как строка.
Выходные данные: Является предложение панграммой или нет как логическое.

### [restricted_sum.py](restricted_sum.py)
Наш калькулятор свихнулся на цензуре и отказывается использовать некоторые 
слова. Вам необходимо обмануть его и написать программу для для суммирования 
чисел.

Дан массив чисел, необходимо найти сумму этих чисел. Ваше решение не должно 
содержать запрещенные слова, даже как часть слов.

Список запретных слов:
```
sum
import
for
while
reduce
```
Входные данные: Массив, как список (list) целых чисел (int).
Выходные данные: Сумма чисел, как целое число (int).

### [right_to_left.py](right_to_left.py)
Один робот был занят простой задачей: объеденить последовательность строк в 
одно выражение для создания инструкции по обходу корабля. Но робот был левша 
и зачастую шутил и запутывал своих друзей правшей.
Дана последовательность строк. Вы должны объединить эти строки в блок текста, 
разделив изначальные строки запятыми. В качестве шутки над праворукими 
роботами, вы должны заменить все вхождения слова "right" на слова "left", 
даже если это часть другого слова. Все строки даны в нижнем регистре.
Входные данные: Последовательность строк, как кортеж строк (юникод).
Выходные данные: Текст, как строка.
Как это используется: Это просто пример операций, использующих строки и 
последовательности.
```
Предусловие:
0 < len(phrases) < 42
```

### [secret_message.py](secret_message.py)
Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как 
они встречаются в куске текста.

Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем 
все заглавные буквы, то получим сообщение "HELLO".

Входные данные: Текст как строка (юникод).
Выходные данные: Секретное сообщение как строка или пустая строка.

### [the_end_of_other.py](the_end_of_other.py)
Дан набор слов в нижнем регистре. Проверьте есть ли в этом наборе пара слов, 
такая что одно слово заканчивается другим (суффикс или совпадение). 
Для примера: {"hi", "hello", "lo"} -- "lo" это окончание "hello", так что 
результат True.
Замечания: Для этой задачи вы можете прочитать о типе данных set и 
строковых функциях.

Вх. данные: Слова как набор (set) строк (str).
Вых. данные: True или False, как булево выражение.

### [three-words.py](three-words.py)
Дана строка со словами и числами, разделенными пробелами (один пробел между 
словами и/или числами). Слова состоят только из букв. Вам нужно проверить 
есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one 
two three 7 end" есть три слова подряд.

Входные данные: Строка со словами (str).
Выходные данные: Ответ как логическое выражение (bool), True или False.


## License

The code is available under the [MIT license](LICENSE).