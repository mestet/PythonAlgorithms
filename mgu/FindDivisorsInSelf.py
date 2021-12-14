def find_divisors(input_number):
    number_digits = list(map(int, str(input_number)))
    count = 0
    for digit in number_digits:
        if input_number % digit == 0:
            count += 1
    print(count)


find_divisors(int(input()))
