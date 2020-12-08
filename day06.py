from common import *


def parse_input():
    with open("./day06.txt") as f:
        groups = [x.strip().split("\n") for x in f.read().split("\n\n")]
    return groups


print("Part 1:\n", sum([len(set.union(*map(set, group)))
                        for group in parse_input()]))
print("Part 2:\n", sum([len(set.intersection(*map(set, group)))
                        for group in parse_input()]))
