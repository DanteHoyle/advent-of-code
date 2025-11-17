import itertools


def is_nice_v1(text: str):
    VOWELS = 'aeiou'
    BANNED_STRINGS = ['ab', 'cd', 'pq', 'xy']
    # define requirements
    has_matching_neighbors = False
    vowels_required = 3

    vowels_seen = 0

    for a, b in itertools.pairwise(text):
        if not has_matching_neighbors and a == b:
            has_matching_neighbors = True

        if (a + b) in BANNED_STRINGS:
            return False

        if a in VOWELS:
            vowels_seen += 1

    # pairwise loop misses the last vowel in the text string
    if text[-1] in VOWELS:
        vowels_seen += 1

    has_enough_vowels = vowels_seen >= vowels_required

    return has_matching_neighbors and has_enough_vowels

def is_nice_v2(text: str):

    has_sandwiched_char = False
    has_duplicated_pair = False

    limit = len(text) - 2
    for i in range(limit):
        if not has_sandwiched_char:
            substr = text[i: i+3]
            has_sandwiched_char = substr[0] == substr[2]

        if not has_duplicated_pair:
            pair = text[i] + text[i+1]
            has_duplicated_pair = pair in text[i+2:]

        if has_sandwiched_char and has_duplicated_pair:
            break

    return has_sandwiched_char and has_duplicated_pair


with open('input.txt', 'r') as f:
    input_string = f.read()

nice_v1_cnt = 0
nice_v2_cnt = 0

for text in input_string.splitlines():
    if is_nice_v1(text):
        nice_v1_cnt += 1
    if is_nice_v2(text):
        nice_v2_cnt += 1

print(nice_v1_cnt)
print(nice_v2_cnt)
