from common import *


def parse_input():
    with open("./day05.txt") as f:
        return [line.strip() for line in f.readlines()]


def split(curr_range):
    splt = curr_range[0]+int(((curr_range[1]-curr_range[0])+1)/2)
    return [[curr_range[0], splt], [splt, curr_range[1]]]


def partition_binary_space(value, init_range, lower_cond, upper_cond):
    curr_range = init_range
    for x in value:
        lower, upper = split(curr_range)
        if (lower_cond(x)):
            curr_range = lower
        elif (upper_cond(x)):
            curr_range = upper
    return curr_range[0]


def get_row_spec(seat, n_rows):
    return seat[0:int(math.log(n_rows, 2))]


def get_col_spec(seat, n_cols):
    return seat[-int(math.log(n_cols, 2)):]


def get_seat_id(seat, n_rows, n_cols):
    row = partition_binary_space(get_row_spec(
        seat, n_rows), [0, n_rows-1], lower_cond=lambda x: x == "F", upper_cond=lambda x: x == "B")
    col = partition_binary_space(get_col_spec(
        seat, n_cols), [0, n_cols-1], lower_cond=lambda x: x == "L", upper_cond=lambda x: x == "R")
    return row*8+col


seat_ids = [get_seat_id(seat, 128, 8) for seat in parse_input()]

print("Part 1:\n", max(seat_ids))
print("Part 2:\n", set(range(min(seat_ids), max(seat_ids))).difference(set(seat_ids)))
