import random


def get_random_string(length: int) -> str:
    small_letters = list(map(chr, range(97, 123)))
    big_letters = list(map(lambda char: char.upper(), small_letters))
    digits = list(range(0, 10))
    total = small_letters + big_letters + digits
    string_1 = ""
    for i in range(0, length):
        k = random.choice(total)
        string_1 = string_1 + str(k)
    return string_1


while True:
    try:
        n = int(
            input("Введите длину строки для вывода случайных больших и маленьких букв латинского алфавита и цифр, n: "))
    except:
        print('Введите число!')
    else:
        if n > 0:
            break
        else:
            print("Пробуйте еще раз ")

print(f"Случайная строка, заданной длины: ", get_random_string(n))

