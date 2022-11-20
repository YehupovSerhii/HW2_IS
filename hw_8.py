# 1
# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

print("""
Задание 1
""")


def change(lst):
    first_element = lst[0]
    last_element = lst[-1]
    total = lst[1:len(lst) - 1]
    total.append(first_element)
    total.insert(0, last_element)
    return total


print("Введите список элементов через запятую (минимум 2 элемента, пустые значения будут прогнорированы):")
b = results = []
while True:
    a = input().split(",")
    for i in a:
        if len(i.split()) != 0:
            b.append(i)
    if len(b) >= 2:
        results = change(b)
        break
    else:
        print("Кол-во элементов меньше двух, добавьте элемент(ы)")

print("""Список элементов: 
""", b)

print("""Список элементов, с измененными местами первого и последнего элемента между собой 
""", results)

########################################################################################################
# 2
# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

print("""
Задание 2
""")


def to_dict(lst):
    lst = list(set(lst))
    return {k: k for k in lst}


print(
    "Введите список элементов через запятую (минимум 2 элемента, пустые и повторяющиеся значения будут прогнорированы):")
b = []
while True:
    a = input().split(",")
    for i in a:
        if len(i.split()) != 0:
            b.append(i)
    if len(b) >= 2:
        break
    else:
        print("Кол-во элементов меньше двух, добавьте элемент(ы)")
print("""Список элементов: 
""", b)
dict_print = to_dict(b)
print("""Словарь из списка каждый элемент которого является и ключом и значением:""", dict_print)

########################################################################################################
# 3
# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

print("""
Задание 3
""")


def sum_range(start, end):
    # var.1
    summ = 0
    for ii in range(start, end + 1):
        summ += ii
    # var.2
    # summ=0
    # k=start
    # while k<=end:
    #     summ=summ+k
    #     k+=1

    return summ


a = []
while True:
    start = int(input("Введите целочисленное значение START: "))
    end = int(input("Введите целочисленное значение END: "))
    a.append(start)
    a.append(end)
    if start == end:
        print("Значения одинаковые, введите еще раз:")
        a.clear()
    else:
        a.sort()
        break
start = int(a[0])
end = int(a[1])
result = sum_range(start, end)
print("Сумма всех целых чисел в диапазоне: ", a, " включительно, равна: ", result)

########################################################################################################
# 4
# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).

print("""
Задание 4
""")
d = []
m = []


def read_last(lines, file):
    f = open("number_5.txt", "rt")
    file = f.read()
    f.close()
    print("Файл для выбора строк: ", file)

    import re
    q = len(re.findall(r"[\n']+?", open('number_5.txt').read()))

    from itertools import islice
    for line in islice(open("number_5.txt"), q - a, q):
        m.append(line)
    return m


#
while True:
    try:
        a = float(input(
            "Введите колличество строк (lines) из файла number_5.txt для вывода на печать построчно последние строки в колличестве: "))
    except:
        print('Введите число!')
    else:
        if float.is_integer(a) and a > 0:
            a = int(a)
            break
        else:
            print("Пробуйте еще раз ")

l = read_last(a, d)
print("Выбранные ", a, " строк: ")
for x in l:
    print(x)
