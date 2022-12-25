# hw11
# Написать функцию которая принимает целое число - number.
# Функция должна возвращать 'yes' если number является степенью двойки, иначе 'no'.
# Запрещено пользоваться функцией или оператором возведение в степень.

# Пример:

# is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256

# is_power_of_two(125) # 'no' потому что это не степень двойки

# вариант 1

def power_2(number):
    if number <= 0:
        return (False)
    else:
        if number & (number - 1):
            return (False)
        else:
            return (True)


n = 0
k = 1
number = int(input("Введите число number для проверки - является ли число number степенью двойки:"))

k = int(power_2(number))
if k == False:

    print("number(", number, ") # 'no' потому что это не степень двойки")
else:
    while k < number:
        k = k * 2
        n += 1
    if k == number:
        print("number(", number, ") # 'yes' потому что 2 в ", n, " степени это  ", number)


# вариант 2
def power_2(number):
    k = 1
    if number <= 0:
        return False
    while k <= number:
        if k == number:
            return True
        k = k * 2
    else:
        return False


number = int(input("Введите число number для проверки - является ли число number степенью двойки:"))
result = power_2(number)

if result == True:
    print('Число является степенью двойки')
else:
    print('Число не является степенью двойки')


# вариант 3
def power_2(number):
    k = 1
    n = 0
    if number <= 0:
        return (False)
    while k <= number:
        if k == number:
            return (True)
        k = k * 2
        n += 1

    else:
        return (False)


number = int(input("Введите число number для проверки - является ли число number степенью двойки:"))
result = power_2(number)

if result == True:
    print("Число ", number, " является степенью двойки, потому что 2 в степени", n, "является числом ", number)
else:
    print("Число", number, "не является степенью двойки")
