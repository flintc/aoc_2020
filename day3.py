from common import *


def get_answer(slope, nTrees=0):
    x = 0
    dx, dy = slope
    with open("./day3.txt") as f:
        for line in it.islice(map(str.strip, f), dy, None, dy):
            x = (x+dx) % (len(line))
            if (line[x] == "#"):
                nTrees += 1
        return nTrees


part1_slope = [3, 1]
print("Part 1:\n", get_answer(part1_slope))
part2_slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print("Part 2:\n", reduce(op.mul, map(get_answer, part2_slopes), 1))
