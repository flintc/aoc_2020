from common import *


def parse_input():
    with open("./day4.txt") as f:
        return [dict([y for y in x.split(":")] for x in it.chain(*map(lambda x: x.split(" "), passport.split("\n")))) for passport in f.read().split("\n\n")]


def satisfies_hgt_req(hgt):
    try:
        m = re.match("([0-9]+)(in|cm)", hgt)
        value = int(m[1])
        units = m[2]
        if units == "cm":
            return value >= 150 and value <= 193
        elif units == "in":
            return value >= 59 and value <= 76
        print(value, units)
    except IndexError:
        return False


req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
field_rules = {
    "byr": lambda byr: len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002,
    "iyr": lambda iyr: len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020,
    "eyr": lambda eyr: len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030,
    "hgt": satisfies_hgt_req,
    "hcl": lambda hcl: hcl[0] == "#" and re.match("([0-9]|[a-f]){6}", hcl[1:])[0] == hcl[1:],
    "ecl": lambda ecl: ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda pid: len(pid) == 9 and re.match("^[0]*", pid)
}


def valid_passport_part1(passport, req_fields):
    return all(x in passport for x in req_fields)


def valid_passport_part2(passport, req_fields):
    try:
        return all(valid_passport_part1(passport, req_fields) and field_rules[x](passport.get(x, [])) for x in req_fields)
    except TypeError:
        return False


print("Part 1:\n", len(
    list(filter(lambda passport: valid_passport_part1(passport, req_fields),  parse_input()))))

print("Part 2:\n", len(
    list(filter(lambda passport: valid_passport_part2(passport, req_fields),  parse_input()))))
