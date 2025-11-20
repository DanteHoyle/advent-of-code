import enum

symbol = { True: '✅', False: '❌' }

def check_all_rules(password: str):
    def rule_has_increasing_straight(string: str) -> bool:
        limit = len(string) - 2
        for i in range(limit):
            ch_a = ord(string[i])
            ch_b = ord(string[i+1])
            ch_c = ord(string[i+2])

            if ch_a == ch_b - 1 == ch_c - 2:
                return True

        return False

    def rule_has_allowed_letters(string: str) -> bool:
        BANNED = 'iol'

        for b in BANNED:
            if b in string:
                return False
        return True

    def rule_has_enough_pairs(string: str) -> bool:
        limit = len(string) - 1

        pairs_found = 0

        # index in string of second letter of last found pair
        last_was_pair = False

        for i in range(limit):
            if last_was_pair:
                last_was_pair = False
                continue

            if string[i] == string[i+1]:
                last_was_pair = True
                pairs_found += 1

        return pairs_found >= 2

    has_increasing_straight = rule_has_increasing_straight(password)
    has_allowed_letters = rule_has_allowed_letters(password)
    has_enough_pairs = rule_has_enough_pairs(password)

    # print(f'{password}: T1={symbol[has_increasing_straight]} T1={symbol[has_allowed_letters]} T3={symbol[has_enough_pairs]}')

    return has_increasing_straight and has_allowed_letters and has_enough_pairs


def find_next_valid_password(password: str):
    def increment_password(password: str):
        last_index = len(password) - 1
        newchars = []
        for i in range(last_index, 0, -1):
            ch = password[i]
            if ch == 'z':
                newchars.append('a')
            else:
                newchars.append(chr(ord(ch) + 1))
                break
        return password[:-len(newchars)] + ''.join(reversed(newchars))

    next_password = increment_password(password)

    while check_all_rules(next_password) is False:
        next_password = increment_password(next_password)

    return next_password

if __name__ == '__main__':
    password = 'hepxcrrq'
    answer_part1 = find_next_valid_password(password)
    print(f'Part One: {answer_part1}')
    answer_part2 = find_next_valid_password(answer_part1)
    print(f'Part Two: {answer_part2}')


