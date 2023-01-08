# hw_15
# Есть фрагмент текста, состоящий из предложений.
# Предложение - это строка, которая начинается с большой буквы и заканчивается точкой, вопросительным
# или восклицательным знаком (или несколькими такими знаками).
# Слова состоят только из латинских букв, разделяются отделяются пробелами или запятыми с пробелами.
# Предложение может состоять из одного слова.
# Составить предложение из первых слов предложений фрагмента.
# Только первое слово итогового предложения должно быть с большой буквы, остальные с маленькой.
# Предложение должно заканчиваться точкой.
# def generate_sentence(text: str) -> str:
#   pass
# "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.." -> "Hello and who or yes claro."
# "Hola..." -> Hola.


# import re
# text="Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."
# res=[]
# split_regex = re.compile(r'[.|!|?|…]')
# sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(text)])
# for s in sentences:
#     res.append(s)
# res=list(map(str.lower,res)) #поменял на нижние буквы весь текст
# res=list(filter(None, res))
# def first_word(text: str) -> str:
#     # функция ниже убирает лишние точки и запятые в слове
#     def removeExtraSymbols(text: str) -> str:
#         result = text.replace('.', '')
#         result = result.replace(',', '')
#         return result

#     allWords = text.split() # разбиваем на слова по пробелу
#     for word in allWords: # пробежимся по всем "словам" в предложении
#         if not removeExtraSymbols(word) == '':  # если после удаления лишних символов у нас есть буквы
#             if "." in word: # если нам подсунули Hello.World (без пробела после точки)
#                 word = word.split(".")[0] # берем только первое слово перед точкой
#             if "," in word: # если нам подсунули Hello,World (без пробела после запятой)
#                 word = word.split(",")[0] # берем только первое слово перед запятой
#             return removeExtraSymbols(word) # возвращаем слово без символов
# p=[]
# for i in range(len(res)):
#     k=first_word(res[i])
#     p.append(k)
# l=(' '.join(p)+".").capitalize()
# print (l)


import re


def generate_sentence(text: str) -> str:
    res = []
    split_regex = re.compile(r'[.|!|?|…]')
    sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(text)])
    for s in sentences:
        res.append(s)
    res = list(map(str.lower, res))
    res = list(filter(None, res))

    def first_word(text: str) -> str:
        def removeExtraSymbols(text: str) -> str:
            result = text.replace('.', '')
            result = result.replace(',', '')
            return result

        allWords = text.split()
        for word in allWords:
            if not removeExtraSymbols(word) == '':
                if "." in word:
                    word = word.split(".")[0]
                if "," in word:
                    word = word.split(",")[0]
                return removeExtraSymbols(word)

    p = []
    for i in range(len(res)):
        k = first_word(res[i])
        p.append(k)
    l = (' '.join(p) + ".").capitalize()
    res = l
    return res


text1 = "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."
text2 = "Hola..."

print("Текст 1 для обработки:", text1)
g1 = generate_sentence(text1)
print(g1)
print("Текст 2 для обработки:", text2)
g2 = generate_sentence(text2)
print(g2)