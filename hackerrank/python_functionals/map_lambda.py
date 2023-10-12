# One line of input: an integer N.
# Print a list on a single line containing the cubes of the first N fibonacci numbers.
def fibonacci(number):
    if number <= 0:
        return []

    if number == 1:
        return [0]

    a, b = 0, 1
    result = [a, b]
    for it in range(2, number):
        a, b = b, a + b
        result.append(b)

    return result


if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x ** 3, fibonacci(n))))
