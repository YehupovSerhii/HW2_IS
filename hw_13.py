# 13.Написать функцию, которая принимает несколько итерируемых объектов,
# и возвращает список из кортежей составленных из элементов итерируемых объектов одного индекса.
# Функция также должна принимать параметры с дефолтными значения:
# full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной
# default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default
# seq1 = [1, 2, 3, 4, 5]
# seq2 = [9, 8, 7]
# custom_zip(seq1, seq2) -> [(1, 9), (2, 8), (3, 7)]
# custom_zip(seq1, seq2, full=True, default="Q") -> [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
# Встроенную функцию zip не используем.
# def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
#   pass
# """


def custom_zip(*sequences, full=False, default=None):
    sequences = list(sequences)
    if full:
        sq_start = max(sequences, key=len)
    else:
        sq_start = min(sequences, key=len)

    sq_count = len(sequences)

    res = []
    for cnt, item in enumerate(sq_start):
        tup = ()
        for i in range(0, sq_count):
            if full and len(sequences[i]) < cnt + 1:
                tup = tup + (default,)
            else:
                tup = tup + (sequences[i][cnt],)
        res.append(tup)
    return res


print(custom_zip([1, 2, 3], [4, 5, 6, 7], [8, 9]))
print(custom_zip([1, 2, 3, 4, 5], [9, 8, 7]))
print(custom_zip([1, 2, 3, 4, 5], [9, 8, 7], full=True, default="Q"))
