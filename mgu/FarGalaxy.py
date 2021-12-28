# Ввести построчно четвёрки вида «число число число слово»,
# где первые три числа — это координаты галактики по имени «слово»
# (некоторые галактики могут называться одинаково, но координаты у всех разные).
# Последняя строка ввода не содержит пробелов и не учитывается.
# Вывести в алфавитном порядке имена любых двух наиболее удалённых друг от друга галактик.
# Считается, что одинаковых расстояний в списке нет.
#
# 35.764 -797.636 -770.320 almost
# 88.213 -61.688 778.457 gene
# -322.270 -248.555 -812.730 trend
# 721.262 630.355 968.287 dow
# -895.519 -970.173 97.282 non
# -561.036 -350.840 -723.149 disco
# -151.546 -900.962 -658.862 bidder
# -716.197 478.576 -695.843 hawaii
# -744.664 -173.034 -11.211 sad
# -999.968 990.467 650.551 erik
# .
# almost erik


def two_most_distant_galaxy(galaxies):
    distance_dict = dict()
    coordinates = list(galaxies.keys())
    max_distance = 0.0
    for i in range(len(coordinates)):
        a_coordinate = coordinates[i]
        for j in range(i + 1, len(coordinates)):
            b_coordinate = coordinates[j]
            distance_squared = distance2(a_coordinate, b_coordinate)
            distance_dict |= {distance_squared: (galaxies[a_coordinate], galaxies[b_coordinate])}
            if max_distance < distance_squared:
                max_distance = distance_squared

    # for k, v in sorted(distance_dict.items()):
    #     print(f'Distance: {k}, between {v}')

    print(' '.join(sorted(distance_dict[max_distance])))


def distance2(a, b):
    return (a[0] - b[0]) * (a[0] - b[0]) + \
           (a[1] - b[1]) * (a[1] - b[1]) + \
           (a[2] - b[2]) * (a[2] - b[2])


if __name__ == '__main__':
    galaxies = dict()
    user_input = input()
    while ' ' in user_input:
        x, y, z, name = user_input.split()
        galaxies |= {(float(x), float(y), float(z)): name}
        user_input = input()
    two_most_distant_galaxy(galaxies)
