from itertools import permutations, pairwise

def parse_input(input: str):
    happieness = {}
    for line in input.splitlines():
        words = line.split()

        opinion_holder = words[0]
        target = words[-1].replace('.', '')
        opinion = words[2:4]

        if opinion[0] == 'gain':
            modifier = int(opinion[1])
        else:
            modifier = - int(opinion[1])

        if opinion_holder not in happieness.keys():
            happieness[opinion_holder] = {}

        happieness[opinion_holder][target] = modifier

    return happieness

def score_arrangement(happieness_map, order):
    utility = 0
    for a, b in pairwise(order):
        utility += happieness_map[a][b] + happieness_map[b][a]

    first = order[0]
    last = order[-1]

    utility += happieness_map[first][last] + happieness_map[last][first]

    return utility

def part_one(puzzle_input: str):
    print('Part One')
    happieness = parse_input(puzzle_input)
    knights = list(happieness.keys())
    max_order = None
    max_utility = 0

    for orders in permutations(knights):
        score = score_arrangement(happieness, orders)
        if score > max_utility:
            max_order = orders
            max_utility = score

    print('Best Seating Arrangement:', max_order)
    print('Score:', max_utility)

def part_two(puzzle_input: str):
    print('Part Two')
    happieness = parse_input(puzzle_input)
    knights = [*happieness.keys()]

    me = 'Dante'

    happieness[me] = {}

    for knight in knights:
        happieness[me][knight] = 0
        happieness[knight][me] = 0

    knights.append(me)

    max_utility = 0
    max_order = None
    for orders in permutations(knights):
        score = score_arrangement(happieness, orders)
        if score > max_utility:
            max_order = orders
            max_utility = score
    print('Best Seating Arrangement:', max_order)
    print('Score:', max_utility)

with open('input.txt') as f:
    input_text = f.read()

part_one(input_text)
part_two(input_text)
