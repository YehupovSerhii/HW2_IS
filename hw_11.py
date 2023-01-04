# 11.
# Написать функцию, которая возвращает случайную строку заданной длины.
# Строка должна состоять из больших и маленьких латинских букв и цифр.
# def get_random_string(length: int) -> str:
#   pass
# Ограничения:
# - Не использовать модуль string
# - Не создавать руками список ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]

import random
def get_random_string(length: int) -> str:
    small_letters = list(map(chr, range(97, 123)))
    big_letters = list(map(lambda char: char.upper(), small_letters))
    digits = list(range(0, 9))
    total = small_letters + big_letters + digits
    # print(type(total))
    # n=int(input())
    string_1 = ""
    for i in range(0, length):
        k = random.choice(total)
        string_1 = string_1 + str(k)
    # print(string_1)
    return string_1
while True:
    try:
        n = float(
            input("Введите длину строки для вывода случайных больших и маленьких букв латинского алфавита и цифр, n: "))
    except:
        print('Введите число!')
    else:
        if float.is_integer(n) and n > 0:
            n = int(n)
            break
        else:
            print("Пробуйте еще раз ")

print(f"Случайная строка, заданной длины: ", get_random_string(n))

