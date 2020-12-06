from common import *


def parse_input_line(line):
    return list(map(str.strip, line.split(":")))


def parse_input(input_filepath):
    with open(input_filepath) as f:
        return [list(map(str.strip, x.split(":"))) for x in f.readlines()]


def num_letters_between(letter, min_num, max_num, value):
    out = re.findall(
        f"{letter}", value)
    return len(out) >= min_num and len(out) <= max_num


def parse_rule(rule_str):
    range_str, letter = rule_str.split(" ")
    min_instances, max_instances = range_str.split("-")
    return {"num1": int(min_instances), "num2": int(max_instances), "letter": letter}


def satisfies_num_letters_cond(cond_str, pw):
    rule = parse_rule(cond_str)
    return num_letters_between(rule["letter"], rule["num1"], rule["num2"], pw)


def satisfies_letter_pos_cond(cond_str, pw):
    rule = parse_rule(cond_str)
    pos1_match = pw[rule["num1"]-1] == rule["letter"]
    pos2_match = rule["num2"] <= len(
        pw) and pw[rule["num2"]-1] == rule["letter"]
    return pos1_match != pos2_match


puzzle_input = parse_input("./day2.txt")

print("Part 1\n", len(
    list(filter(lambda x: satisfies_num_letters_cond(*x), puzzle_input))))
print("Part 2\n", len(
    list(filter(lambda x: satisfies_letter_pos_cond(*x), puzzle_input))))
