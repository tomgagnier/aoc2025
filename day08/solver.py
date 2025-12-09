import math
from itertools import combinations

for file_name, count in ('example.txt', 10), ('input.txt', 1000):
    boxes = [tuple(map(int, line.split(','))) for line in open(file_name).readlines()]
    circuits = {frozenset([b]) for b in boxes}
    ds = sorted(combinations(boxes, 2), key=lambda p: math.dist(p[0], p[1]))

    i, part1, part2 = 0, 0, 0
    while len(circuits) > 1:
        box0, box1 = ds[i]
        part2 = box0[0] * box1[0]
        circuit0, circuit1 = [next(c for c in circuits if b in c) for b in (box0, box1)]
        circuits -= {circuit0, circuit1}
        circuits.add(circuit0 | circuit1)

        i += 1
        if i == count:
            circuits_ = sorted(map(len, circuits))[-3:]
            part1 = math.prod(circuits_)

    print(file_name)
    print('  part 1:', part1)
    print('  part 2:', part2)
