from common import *


def parse_input(filepath):
    with open(filepath) as f:
        inputList = f.readlines()
    return [int(x.replace("\n", "")) for x in inputList]


def get_answer(values, cond, nValues):
    for comb in it.combinations(values, nValues):
        if (cond(comb)):
            return reduce(op.mul, comb, 1)


def sum_to_2020(values):
    return sum(values) == 2020


puzzle_input = parse_input("./day1.txt")
print("Part 1\n", get_answer(puzzle_input, sum_to_2020, 2), "winner!!!")
print("Part 2\n", get_answer(puzzle_input, sum_to_2020, 3), "winner!!!")
