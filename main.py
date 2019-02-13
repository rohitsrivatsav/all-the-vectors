from vector import Vector
from functools import reduce

vectors = []
with open('vectors.txt') as f:
    for line in f:
        v = Vector(*tuple(map(int, line.strip().split(','))))
        vectors.append(v)

vectors = [vectors[0].scale(3)] + [vectors[-1].scale(3)] + vectors[1:-1]
final = reduce(lambda acc, vec: acc + vec, vectors, Vector(0, 0))

print(final)

# v1 = Vector(1, 2, 3)
# v2 = Vector(1, 2, 3)
# print(v1, v2)
# v3 = v1 + v2
# print(v3)
# d = v1.dot(v2)
# print('d', d)
# v4 = v1.scale(3)
# print('v4', v4)
# size = v1.norm()
# print('v1 size', size)
