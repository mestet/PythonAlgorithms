import re


# A valid mobile number is a ten-digit number starting with a 7,8 or 9.
def process(times):
    phone_pattern = r'[7,8,9][\d]{9}'
    lines = [input() for _ in range(times)]
    for phone in lines:
        if re.fullmatch(phone_pattern, phone):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    process(int(input()))
