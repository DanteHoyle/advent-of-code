import itertools
import collections

def all_combinations(containers):
    limit = len(containers)
    for i in range(1, limit+1):
        yield from itertools.combinations(containers, i)

eggnog_target = 150

text = open('input.txt').read()
containers = [int(line) for line in text.splitlines()]
print(f'{containers=}')

matching = 0
lengths = []

for combi in all_combinations(containers):
    liters = sum(combi)

    if liters == eggnog_target:
        matching += 1
        print('+'.join([str(c) for c in combi]), '=', liters)
        lengths.append(len(combi))

c = collections.Counter(lengths)
print('Total combinations that meet requirements:', matching)

minimum_containers_needed = min(c.keys())
print(f'You need {minimum_containers_needed} containers to fill {eggnog_target} liters, and you can do it {c[minimum_containers_needed]} ways')
