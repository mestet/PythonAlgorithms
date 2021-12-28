import os
import random
import sys


def far(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


with open(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "resources\\google-10000-english.txt")) as f:
    words = [w for w in f.read().split() if 2 < len(w) < 8]
if len(sys.argv) > 2:
    words = random.sample(words, int(sys.argv[2]))

N = 42 if len(sys.argv) <= 1 else int(sys.argv[1])
m, M = -1000, 1000

Dists = set()
Galaxies = set()
while len(Galaxies) < N:
    x0, y0, z0 = (random.random() * (M - m) + m for i in range(3))
    NDists = set()
    for x1, y1, z1 in Galaxies:
        dist = far((x0, y0, z0), (x1, y1, z1))
        if dist in Dists:
            print("OOPS", x0, y0, z0)
            break
        NDists.add(dist)
    else:
        Dists |= NDists
        Galaxies.add((x0, y0, z0))
        print("{:5.3f} {:5.3f} {:5.3f} {}".format(x0, y0, z0, random.choice(words)))
print(".")
