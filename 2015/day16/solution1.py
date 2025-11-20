import re

YES = 'yes',
NO = 'no'
UNKNOWN = 'UNKNOWN'

symbols = { YES: '✅', NO: '❌', UNKNOWN: '⁉️' }

regex = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'

text = open('aunts-input.txt').read()

aunts = {}

for n, k1, v1, k2, v2, k3, v3 in re.findall(regex, text):
    aunts[n] = {
        k1: int(v1),
        k2: int(v2),
        k3: int(v3)
    }

facts = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

history = {}

for aunt, info in aunts.items():
    truths = {}
    for key, val in info.items():
        target = facts.get(key)
        if not target:
            truths[key] = UNKNOWN
        elif target == val:
            truths[key] = YES
        else:
            truths[key] = NO
    history[aunt] = truths

for aunt, results in history.items():
    if NO in results.values():
        continue
    print('Aunt', aunt, end='')
    for key, result in results.items():
        print(' {}={}'.format(key, symbols[result]), end='')
    print()
