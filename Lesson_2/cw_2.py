#какие бывают типы данных, - изменяемые и не изменяемые.
# Nonetype
# Числа
# Исключения
# Строки
# Байты
# множества
# списки
# кортежи
# словари
tseloe = 1
with_point = 1.2
complex_num = complex(1, 2) # зачем? для специфических задач, конечно же)
# вдруг вы захотите посчитать вольт-амперную характеристику?)
"""ПОБИТОВЫЕ ОПЕРАЦИИ
https://www.math.spbu.ru/user/nlebedim/bit_operat_2017.pdf - годная методичка
Применение:
- Проверка, сброс и установка отдельных битов в составе целого числа
- повышение производительности программ( битовые операции могут
выполняться одновременно над всеми разрядами в отличие от арифметических операций,где нужно учитывать перенос.)
- работа с регистрами аппаратуры
И:
0100
1001



0000
"""
# print(int((bin(8)), 2))
# a = hex(8)
# b = oct(10)
# a_d = int(a, 16)
# print(a_d)
# print(4&9)

# b_d =

# a = 9999999
# print("Number is dec: ", a)
# print("number in bin: ", bin(a))
# print("Number in oct: ", oct(a))
# print(int((hex(a)), 16))
# print(int((oct(a)),8))



# print(abs(-6))
# print(4&6)
# print(4|6)
# print(4^6)
# print(4<<6)
# print(4>>6)
# print(int(17.5))
# print(int('10001',2))
# print(bin(17))
# print(oct(17))
# print(hex(17))


#Сдвиг
# a = 3
# a = a << 4
# print(a)
# a = a >> 1
# print(a)

#Байты и BYTEARRAY
# ПЕРВЫЕ НЕИЗМЕНЯЕМЫЕ, ВТОРЫЕ - ДА
#БОЛЬШЕ ИНФО - https://pythonworld.ru/tipy-dannyx-v-python/bajty-bytes-i-bytearray.html


# b = 'Пример'.encode('UTF-8') #затем эту последовательность прошвыриваем в какой-нибудь websocket
# print(b)
# print(chr(123), chr(124), chr(125))  #берем символ из таблицы ASCII
# print(ord("{"),ord("|"), ord("}"))


# """СТРОКИ - НЕЗИМЕНЯЕМЫЙ ТИП
# ПОЛНЫЙ СПИСОК НА PYTHONWORLD.RU"""
# test_string = "ThiS is Test STRiNg"
# print(test_string)
# print("Make all letters in uppercase", test_string.upper(), test_string)
# print("make all letters in lowercase", test_string.lower())
# print("make first letters in uppercase", test_string.capitalize())
# print("is digit:", test_string.isdigit())
# Что можем сделатб :
# s = "first" + "second"
# print(s)
# print(s * 3)
# print(s[0], s[1], s[2], s[3], s[4])

""" СРЕЗЫ - ЭТО КРАЕУГОЛЬНЫЙ КАМЕНЬ ПИТОНА
Общая формула среза : [start:finish:step]"""
s = '0123456789'
# print(s[1::2])
# print(s[::2])
# print(s[1:2:5])
# #БЫСТРЫЙ РЕВЕРС
# print(s[-1]) # то как берем элементы с конца.
# print(s[::-1])
# print(reversed(s))


"""ЦИКЛ FOR ДЛЯ ОБХОДА ПОСЛЕДОВАТЕЛЬНОСТЕЙ"""
# for x in s:
#     print(x)

#аналог
# cnt = 0
# while len(s) > cnt:
#     print(s[cnt])
#     cnt += 1

#РАЗБИЕНИЕ СТРОКИ НА ЭЛЕМЕНТЫ СПИСКА
# print(list("split"))
#
# s = 'some, test - string'
# l = s.split(",")
# print(l)

#ОБРАТНАЯ ОПЕРАЦИЯ
# l = ['Hello', 'Bonjur', 'Hola']
# print(" ".join(l))

# """КОЛЛЕКЦИИ.
# СПИСКИ - ИЗМЕНЯЕМЫЕ"""
#ПОЛНЫЙ СПИСОК МЕТОДОВ - https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
# ОНИ БЫВАЮТ УПОРЯДОЧНЫЕ И НЕ УПОРЯДОЧНЫЕ * СРЕДИ УПОРЯДОЧНЫХ - ЭТО
# СПИСКИ И КОРТЕЖИ. * НЕУПОРЯДОЧНЫЕ - ЭТО СЛОВАРИ И МНОЖЕСТВА
# l1 = [1, 2, 3, 4, 5]
# l2 = [True, False, 1, 2, 3]
# l3 = ['t', 'e', 's', 't']
# # print(False in l1)
# l4 = [l1, l2, l3]
# print(l4)
# l2[1] = 'ANOTHER VAL'
# #
# # l4.insert(1, [100, 200, 300])
# print(l4)
# l = [1]
# if l:
#     print("не пустой")
# else:
#     print('пустой')

#ОБЪЕДИНЕНИЕ СПИСКОВ
#print(l1 + l2 + l3)
# print(l2.index(0))  # ВАЖНЫЙ МОМЕНТ : False/True и 0 - это одно и тоже для index
# print(l1.index(3))

#ДОБАВЛЕНИЕ В СПИСОК
# l2.insert(3, 'SOME VALUE')  #ДОБАВЛЕНИЕ В ПОЗИЦИЮ
# print(l2)
# l2.append('ONE MORE ELEMENT')
# print(l2)

# # ПОЛУЧИТЬ ЭЛЕМЕНТ ИЗ СПИСКА С ЕГО УДАЛЕНИЕМ ИЗ НЕГО
# elem = l2.pop(2)
# print(elem, l2)



# """КОЛЛЕКЦИИ.
# КОРТЕЖИ - НЕИЗМЕНЯЕМЫЕ
# ПОДРОБНЕЕ - https://pythonworld.ru..."""
# a = 1
# b = 2
# a, b = b, a
# print(a, b)
#
# t = ([1, 2], 3, 4)
# t[0][1] = "asdasd"
# print(t)
# ЗАЧЕМ? ДЛЯ БЕЗОПАСНОСТИ.
#
# ПЕРЕСТАВИТЬ ЭЛЕМЕНТЫ В ЛИСТЕ
# l = [1, 2, 3, 4]
# l[0], l[3] = l[3], l[0]
# print(l)

#"""
# КОЛЛЕКЦИИ.
# МНОЖЕСТВА - ИЗМЕНЯЕМЫЕ НЕ УПОРЯДОЧНЫЕ, РАБОТАЕТ КАК УНИКАЛИЗАТОР
# И ЕСЛИ НЕ ВАЖЕН ПОРЯДОК(ПОИСК БЫСТРЕЕ ВСЕГО)
# МЕТОДЫ - https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html"""
# a = {1, 2, 3, 4, 5}
# print(a)
# # ЗАЧЕМ? ЕСЛИ НУЖНО ДЕРЖАТЬ УНИКАЛЬНЫЕ ЭЛЕМЕНТЫ И НЕ ВАЖЕН ПОРЯДОК
# # для неизменяемости нужно использовать frozenset

# # УНИКАЛИЗАТОР
# l = [1, 1, 1, 2, 2, 2]
# print(set(l))  # на собеседовании не прокатит))

# t = tuple() # - пустой кортеж
# c = ()
# print(type(c))

# s = set()  # приведение к типу множества пустого
# s = {}  # это будет пустой словарь. не путать.

# """
# КОЛЛЕКЦИИ.
# СЛОВАРИ - ИЗМЕНЯЕМЫЕ (Словарь - это тип данных , который хранит пары типа "ключ-значение")
# МЕТОДЫ - https://phytonworld.ru/tipy-dannyx-v-python/
# ЗАЧЕМ? ЭТО ОЧЕНЬ СИЛЬНЫЙ ИНСТРУМЕНТ ДЛЯ ХРАНЕНИЯ ИНФОРМАЦИИ, А ТАКЖЕ МОЖЕТ ИСПОЛЬЗОВАТЬСЯ
# В СЛУЧАЯХ, КАК АЛЬТЕРНАТИВА УСЛОВНЫМ ОПЕРАТОРАМ
# Что может являться ключом , словаря? Ключом словаря может являться любой неизменяемый обьект.
# some_dict = {"name": "Andrey",
#              "surname": "Krylov",
#              "position": "Student"}
# print(some_dict["name"])
# print(len(some_dict))
# Кортежи могут быть ключами словаря, но только в одном случае. - Если он из неизменяемых.

# # БОГАТЫРСКИЙ КАМЕНЬ
# decision = input("Enter direction: ").lower()
# if decision == "left":
#     print("lose horse")
# elif decision == "right":
#     print("Lose life")
# elif decision == "straight":
#     print("Lose your mind")


# story_stone = {
#     "left": "Lose horse",
#     "right": "Lose life",
#     "straight": "Lose mind"
# }
# decision = input("enter direction: ").lower()
# print(story_stone[decision])
# print(story_stone.get(decision))   # ВАЖНО ПОНИМАТЬ РАЗНИЦУ
# print(story_stone.keys())
# print(story_stone.values())
# print(story_stone.items())
# В словарях самое быстрое обращение
# """NoneType"""
# c = None
# print(print(c, type(c)))

#ТЕРНАРНЫЙ ОПЕРАТОР
# a = 1
# b = 2
# if a == 3:
#     result = 123
# else:
#     result = 5
#
# result = 123 if a == 3 else 5

#"""Exceptions - исключение. Нужны для обработки внештатных ситуаций"""
# try:
#     1 / 0
# except ZeroDivisionError as err:
#     c = 1
#     print("Error!!!", err)
