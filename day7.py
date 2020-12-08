from common import *


def parse(data):
    return[[x.strip().split(",") for x in line.split("bags contain")]
           for line in data]


def parse_input():
    with open("./day7.txt") as f:
        return parse(f)


example_p1 = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''


example_p2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''


def get_rules_map(rules):
    rules_map = {"no other": {}}
    for rule in rules:
        rule_spec = []
        for x in rule[1]:
            key = "".join(re.findall("[a-z,\s]", x)
                          ).replace("bags", "").replace("bag", "").strip()
            try:
                value = int(re.match("[0-9]*", x.strip()).group(0))
            except ValueError:
                value = 0
            rule_spec.append([key, value])
        rules_map[rule[0][0]] = dict(rule_spec)
    return rules_map


def total_can_contain(can_contain, level, rules_map):
    can_contain[f"level_{level}"] = {}
    for key in can_contain[f"level_{level-1}"]:
        for k, v in rules_map.items():
            if key in v:
                can_contain[f"level_{level}"][k] = v

    if len(can_contain[f"level_{level}"].keys()) == 0:
        return can_contain
    else:
        return total_can_contain(can_contain, level+1, rules_map)


def total_bags_within(containing_bag, rules_map):
    count = 0
    for contained_bag, quantity in rules_map[containing_bag].items():
        count += quantity + quantity * \
            total_bags_within(contained_bag, rules_map)
    return count


rules_map = get_rules_map(parse_input())
print("Part 1:\n", len(
    list(set(it.chain.from_iterable([(x.keys()) for x in total_can_contain({"level_0": {"shiny gold": 0}}, 1, rules_map).values()]))))-1)
print("Part 2:\n", total_bags_within("shiny gold", rules_map))
