# Определитель матрицы 4×4
#
# Матрица 4×4 задаётся кортежем из 4 кортежей по 4 целых числа в каждом.
# Посчитать точный определитель этой матрицы. Пользоваться itertools нельзя.
#
# Examples:
# (5, -4, 4, -7), (1, -2, 6, 0), (3, -8, -6, -4), (-1, 2, -9, 3)
# 702
#
# (-4, -2, -7, 8), (2, 7, 4, 9), (2, 0, 6, -3), (6, 4, -10, -4)
# -1926

def find_determinant_four(matrix):
    det = 0
    sign = 1
    for i in range(4):
        a = matrix[0][i]
        m3 = get_sub_matrix(matrix, i)
        det_a = find_determinant_three(m3)
        det += (a * sign * det_a)
        sign *= -1
    return det


def get_sub_matrix(m4, ignore):
    m3 = []
    for i in range(1, 4, 1):
        row = []
        for j in range(4):
            if j != ignore:
                row += [m4[i][j]]
        m3 += [row]
    return m3


def find_determinant_three(m):
    d = m[0][0] * m[1][1] * m[2][2] + \
        m[0][1] * m[1][2] * m[2][0] + \
        m[0][2] * m[1][0] * m[2][1] - \
        m[0][2] * m[1][1] * m[2][0] - \
        m[0][0] * m[1][2] * m[2][1] - \
        m[0][1] * m[1][0] * m[2][2]
    return d


if __name__ == "__main__":
    input_data = eval(input())
    result = find_determinant_four(input_data)
    print(result)
