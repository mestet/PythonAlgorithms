import re


# You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of S that contains 2 or more vowels.
# Also, these substrings must lie in between 2 consonants and should contain vowels only.


def find_vowel_substrings(text, n=2):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

    # n or more vowels between two consonants
    pattern = f'(?=([{consonants}])([{vowels}]{{{n},}})([{consonants}]))'

    found = re.findall(pattern, text)
    if found:
        return '\n'.join([_[1] for _ in found])  # second group is needed for result
    else:
        return -1


if __name__ == '__main__':
    input_str = input()
    print(find_vowel_substrings(input_str, 2))
