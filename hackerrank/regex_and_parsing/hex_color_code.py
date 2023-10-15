import re


# The first line contains N, the number of code lines.
# The next N lines contains CSS Codes.
# Output the color codes with '#' symbols on separate lines.
def task():
    abc = '1234567890abcdefABCDEF'
    pattern = f'(#[{abc}]{{{3}}}|#[{abc}]{{{6}}})([,;)])'

    text = ''.join([input() for _ in range(int(input()))])
    for match in re.finditer(pattern, text):
        print(match.group(1))


if __name__ == '__main__':
    task()
