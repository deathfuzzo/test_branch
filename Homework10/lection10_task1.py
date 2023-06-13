# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name():
    num_iteration = 1
    while num_iteration != 0:
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]  # задаем списком используемый алфавит латинский букв
        first_word_length, second_word_length = random.randrange(1, 16), random.randrange(1, 16)  # генерируем длину слов, для 15 символов берётся диапазон 1-16, т.к. граница справа не включается
        first_word, second_word = "", ""
        for i in range(first_word_length):  # циклом составляем первое слово
            letter = letters[random.randrange(26)]
            first_word += letter
        for i in range(second_word_length):  # циклом составляем второе слово
            letter = letters[random.randrange(26)]
            second_word += letter
        yield first_word + " " + second_word  # в остановке генератора выводим склейку через пробел получившихся слов


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
