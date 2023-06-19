# Dzmitry Yakimchyk
# Date: 06/05/2023
# Description: Homework 3
# Grodno IT Academy Python 3.11

def pairs(numbers_string: str) -> bool | int:
    # Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    # Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
    # Входные данные - строка из чисел, разделенная пробелами.
    # Выходные данные - количество пар.
    # Важно: `1 1 1` - это 3 пары, `1 1 1 1` - это 6 пар.
    # Хорошая и логичная проверка. 
    if len(numbers_string) <= 1:
        return 0
    else:
        result = 0
        for i in set(numbers_string.split()):
            # количество пар
            result += int((numbers_string.count(i) * (numbers_string.count(i) - 1)) / 2)
        return result


def uniques(array: list) -> list:
    # Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
    # Элементы нужно выводить в том порядке, в котором они встречаются в списке.
    result = [i for i in array if array.count(i) == 1]
    return result


def ordered_list(array: list) -> list:
    # Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
    # не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
    # дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
    # Верните полученный список.
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(i)
    return array


def tuple_to_list(in_tuple: tuple) -> list:
    # Возьмите кортеж `('a', 'b', 'c')`, И сделайте из него список.
    return list(in_tuple)


def euclid(a: int, b: int) -> int:
    # Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы не знаем
    # функции и рекурсию). can't call itself
    """В остальных случаях для нахождения наибольшего общего делителя двух чисел нужно соблюдать такой порядок действий:
    1. Большее число поделить на меньшее.
    2. Меньшее число поделить на остаток, который получается после деления.
    3. Первый остаток поделить на второй остаток.
    4. Второй остаток поделить на третий и т. д.
    5. Деление продолжается до тех пор, пока в остатке не получится нуль. Последний делитель и есть наибольший общий
    делитель."""
    # Я понял, что надо сохранять остаток в ту переменную, которую делили
    while a != 0 and b != 0:  # Когда не останется остатка от деления => делитель получен
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


# Dictionaries
def cities(input_string: str) -> str:
    # Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
    # Учтите, что бывают ситуации когда город с таким называнием бывает в разных странах (Брест есть в Беларуси и Франции).
    # Входные данные
    # Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
    # В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
    # Выходные данные
    # Для каждого из запроса выведите название страны, в котором находится данный город.
    # Пример данных:
    # Входные данные
    # 2
    # Russia Moscow Petersburg Novgorod Kaluga
    # Ukraine Kiev Donetsk Odessa
    # 3
    # Odessa
    # Moscow
    # Novgorod
    # Выходные данные
    # Ukraine
    # Russia
    # Russia
    """У меня четкое ощущение, что можно сделать проще, но я только такую реализацию придумал"""
    output_string = list()
    input_string = input_string.split('\n')
    dictionary = dict()
    items_number = int(input_string[0])
    compare_index = items_number + int(input_string[items_number + 1])
    for i in range(1, items_number + 1):
        val = input_string[i].split()
        key = val.pop(0)
        dictionary.update({key: val})
    # for key, val in dictionary.items():
    #     for j in range(items_number+1, compare_index+2):
    #         if input_string[j] in val:
    #             output_string.append(key)
    for i in range(items_number + 1, compare_index + 2):
        temp = list()
        for key, val in dictionary.items():
            if input_string[i] in val:
                temp.append(key)
        output_string.append(' '.join(temp))
    return '\n'.join(output_string).strip('\n')


# Sets
def languages(input_string: str) -> str:
    # Задачи для домашней работы
    # Языки
    # Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
    # Входные данные
    # Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
    # Пример входных данных:
    # 3 # N количество школьников
    # 2 # M1 количество языков первого школьника
    # Russian # языки первого школьника
    # English
    # 3 # M2 количество языков второго школьника
    # Russian
    # Belarusian
    # English
    # 3
    # Russian
    # Italian
    # French
    # Выходные данные
    # В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков.
    # Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
    input_string = input_string.split('\n')
    students = int(input_string.pop(0))
    students_list = list()
    lang = int(input_string.pop(0))
    for i in range(students):
        temp = list()

        for j in range(int(lang)):
            temp.append(input_string.pop(0))
        if input_string:
            lang = input_string.pop(0)

        students_list.append(set(temp))
    inter = set.intersection(*students_list)
    uni = set.union(*students_list)
    final_string = '\n'.join([str(len(inter)), *inter, str(len(uni)), *uni])
    # return f"{len(inter)}\n{str(*inter)}\n{len(uni)}\n{uni}"
    return '\n'.join([str(len(inter)), *inter, str(len(uni)), *uni])
    # return [str(len(inter)), str(inter), str(len(uni)), str(uni)]


# Generators
def list_gen(arr1: list, arr2: list) -> list:
    # Генераторы списков
    # Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv']. из ['x','y'] & ['y','z','v']
    # пример:
    # lst = [i + j for i in arr1 for j in arr2]
    return [i + j for i in arr1 for j in arr2]


# Генераторы словарей
def dict_gen(n: int) -> dict:
    # Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до N, а значениями кубы этих чисел.
    # dct = {element: element ** 3 for element in range(1, n+1)}
    return {element: element ** 3 for element in range(1, n + 1)}


# Кортежи
def multiplication_table(n: int):
    # Создайте генератор, который возвращает строки таблицы умножения от 0 до заданного числа.
    for i in range(n + 1):
        output = ''
        for j in range(n + 1):
            output += str(i * j)
            if j != n:
                output += ' '
        yield output

# Решения отличные, комментировать нечего. Для общего интереса - можешь ознакомиться с альтернативными решениями в Ответах.
