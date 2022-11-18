# Задание 1
# Дан файл с произвольным текстом, необходимо найти все числа в файле и
# записать в список numbers

print("""
Задание 1
""")
f = open('data.txt', 'r')
a = (f.read())
f.close()
print("Текст из файла: ", a)

m = []
for b in a.split():
    try:
        m.append(float(b))
    except ValueError:
        pass
numbers = []
for b in m:
    if int(b) == b:
        numbers.append(int(b))
    else:
        numbers.append(float(b))
print("Числа из текста в файле, записанные в список numbers:", numbers)

# Задание 2
# Запросить у пользователя текст и записать его в файл data.txt

print("""
Задание 2
""")
a = str(input("Введите текст для записи в файл data_2.txt: "))
f = open('data_2.txt', 'w')
f.write(a)
f.close()
f = open('data_2.txt', 'r')
print("Текст из файла data_2.txt: ", f.read())
f.close()

##############################################################################################
# Задание 3
# Запросить у пользователя число N и запросить N чисел у пользователя,
# потом записать их в файл numbers.txt через пробел

print("""
Задание 3
""")

n = int(input('Введите число N (колличество чисел для записи в файл numbers.txt):'))
print("Введите", n, "чисел:")

a = []
for b in range(n):
    try:
        b = float(input("Введите число: "))
        a.append(b)
    except ValueError:
        pass
numbers = []
for b in a:
    if int(b) == b:
        numbers.append(int(b))
    else:
        numbers.append(float(b))
print("Список чисел для записи в файл numbers.txt: ", numbers)

# var1
p = (" ".join(map(str, numbers)))
# var2
# p=" "
# for i in numbers:
#     p+=str(i)+" "

f = open('numbers.txt', 'w')
f.write(p)
f.close()

f = open('numbers.txt', 'r')
print("Текст из файла numbers.txt: ", f.read())
f.close()

#################################################################################

# Задание 4
# Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt,
# где одна строка = одно число

print("""
Задание 4
""")
import random

a = [random.randint(0, 100) for _ in range(100)]
print("100 рандомных чисел для записи в файл random_numbers.txt: ", a)
ff = open(r"random_numbers.txt", "a")
for i in a:
    ff.write(str(i) + '\n')
ff.close()
f = open('random_numbers.txt', 'r')
print("Текст из файла random_numbers.txt: ")
print(f.read())
f.close()
#################################################################################
# Задание 5
# Дан файл с произвольным текстом, нужно найти количество слов в файле
# и вывести пользователю

print("""
Задание 5
""")

f = open("number_5.txt", "rt")
d = f.read()
w = d.split()
i = 0
for d in w:
    if d.isnumeric():
        i += 1
print("Колличество слов в файле number_5.txt: ", (len(w) - i))
f.close()

#################################################################################
# Задание 6
# Дан файл в котором записаны числа через пробел, необходимо вывести
# пользователю сумму этих чисел

print("""
Задание 6
""")

f = open('number_6.txt', 'r')
a = (f.read())
f.close()
print("Числа из файла number_6.txt: ", a)

m = []
for b in a.split():
    try:
        m.append(float(b))
    except ValueError:
        pass
numbers = []
for b in m:
    if int(b) == b:
        numbers.append(int(b))
    else:
        numbers.append(float(b))
print("Сумма всех чисел в в файле number_6.txt: ", sum(numbers))

#################################################################################
# Задание 7
# Дан файл в котором записан текст, необходимо вывести топ 5 строк
# которые чаще всего повторяются, пример:
# 'в' - 20 раз
# 'привет' - 10 раз
# 'как' - 9 раз
# 'у' - 7
# 'world' - 4

print("""
Задание 7
""")

s = {}

f = open('number_5.txt', 'r')
a = (f.read())

print("""Текст из файла number_5.txt:
    """, a)
print("ТОП 5 строк которые чаще всего повторяются: ")
f.close()

f = open('number_5.txt', 'r')  # cчитываю файл

line = f.readline().lower()

while line:
    line = line.split()
    i1 = 0
    i2 = ''
    q = 0
    t = []
    min1 = 0
    for i in line:  # ввожу слова в словарь
        if i not in s:  # проверяю есть ли слово в словаре,если есть,то добавляю1
            s[i] = 1
        else:
            s[i] += 1
    for values in s.values():  # нахожу максимальное повторение
        if values > i1:
            i1 = values
    for keys, values in s.items():
        if values == i1:
            min1 = keys
    for keys, values in s.items():  # если слова встречаются одинаковое кол-во,
        if values == i1:  # то находим  лексикографически первое
            if min1 > keys:
                min1 = keys
    line = f.readline().lower()

for _ in range(5):
    print("строка <", (next(ch for ch, code in s.items() if code == i1)), "> повторилась ", i1, " раз")
    i1 = i1 - 1
f.close()
