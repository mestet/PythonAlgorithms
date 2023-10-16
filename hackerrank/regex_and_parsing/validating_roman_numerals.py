import re


# Validate roman numeral from 1 to 3999
def is_roman(numeral):
    pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return bool(re.match(pattern, numeral))


if __name__ == '__main__':
    valid = [
        'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI',
        'CCXII', 'CDXXI', 'CDXCIX', 'MMMDCCXLII', 'MMMCMXCIX'
    ]
    invalid = [
        'DXXVIIII', 'IIII', 'XVV'
    ]
    for test in valid:
        if not is_roman(test):
            raise AssertionError(f'Valid roman numeral was not accepted: {test}')

    for test in invalid:
        if is_roman(test):
            raise AssertionError(f'Invalid roman numeral was accepted: {test}')

    print("Test end")
