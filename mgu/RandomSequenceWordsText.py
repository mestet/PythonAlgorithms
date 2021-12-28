import random
import sys
from collections import defaultdict


# В первой строке программа вводит натуральное число N⩾3.
# Во всех последующих — роман Л. Н. Толстого «Анна Каренина» (именно из этого файла).
# Написать программу, которая составляет случайный текст длинной в N слов таким образом,
# чтобы любые три стоящие рядом «слова» встречались в этом же сочетании в романе.
#
# «Словами» считаются:
# любые последовательности непробельных символов (например, тире между словами)
#
# Красная строка (перевод строки и четыре пробела) в начале абзаца (например, в прямой речи)
# Все остальные непробельные символа считаются «буквами»:
# например слово со знаком препинания или кавычкой не равно просто слову.
#
# Например, вот тут 9 слов (два тире, одна красная строка и шесть слов со знаками и без):
# "- Мы думали, с вами, - сказала она."


def read_input():
    limit = int(input())
    base_text = sys.stdin.read().replace("\n    ", " @ ").split()

    word_heap = defaultdict(init_word)
    for i in range(1, len(base_text) - 2):
        a = base_text[i]
        b = base_text[i + 1]
        c = base_text[i + 2]
        word_heap[(a, b)] |= {c}

    del base_text

    start, prev = random_word(word_heap.keys())
    next_words = word_heap[(start, prev)]
    random_word_sequence = [start, prev]
    for x in range(limit - 2):
        word = random_word(next_words)
        next_words = word_heap[(prev, word)]
        random_word_sequence.append(word)
        prev = word

    combined_text = " ".join(random_word_sequence).replace("@", "\n    ")
    print(combined_text)


def random_word(col):
    return random.choice(list(col))


def init_word():
    return set()


if __name__ == "__main__":
    read_input()
