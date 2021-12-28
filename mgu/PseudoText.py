import codecs
import random
from collections import defaultdict


def read_input():
    limit = int(input())
    # base_text = sys.stdin.read().replace("\n    ", " @ ").split()
    base_text = read_file(26944).replace("\n    ", " @ ").split()

    word_heap = defaultdict(init_word)
    for i in range(1, len(base_text) - 2):
        a = base_text[i]
        b = base_text[i + 1]
        c = base_text[i + 2]
        word_heap[a]["n+1"] |= {b}
        word_heap[a]["n+2"] |= {c}

    word_heap[base_text[-2]]["n+1"] |= {base_text[-1]}  # last one
    del base_text

    random_word_sequence = list()
    word = random_word(word_heap.keys())

    random_word_sequence.append(word)
    next_words = word_heap[word]["n+1"]
    narrow = word_heap[word]["n+2"]
    for x in range(limit - 1):
        word = random_word(next_words)
        next_words = word_heap[word]["n+1"] & narrow
        narrow = word_heap[word]["n+2"]
        random_word_sequence.append(word)

    combined_text = " ".join(random_word_sequence).replace("@", "\n    ")
    print(combined_text)


def random_word(col):
    return random.choice(list(col))


def read_file(limit):
    with codecs.open("C:\\Users\\MVlasov\\PycharmProjects\\PythonAlgorithms\\resources\\AnnaKarenina.txt", "r",
                     "utf_8_sig") as file:
        head = "".join([next(file) for _ in range(limit)])
        file.close()
        return head


def init_word():
    return {"n+1": set(), "n+2": set()}


if __name__ == "__main__":
    read_input()
