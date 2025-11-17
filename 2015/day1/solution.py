import sys

def parse_floor_changes(input: str):
    floor = 0
    first_underground_at = None
    for index, token in enumerate(input):
        match token:
            case '(':
                floor += 1
            case ')':
                floor -= 1
            case _:
                print(f'Unexpected character: {token}', file=sys.stderr)

        if not first_underground_at and floor < 0:
            first_underground_at = index + 1

    return {
        'final_floor': floor,
        'first_underground_at': first_underground_at,
        'tokens_parsed': len(input)
    }


if __name__ == '__main__':
    # select an input from arguments or file
    if len(sys.argv) == 1:
        with open('input.txt', 'r') as f:
            input = f.read().strip()
    else:
        input = sys.argv[1]

    for stat, value in parse_floor_changes(input).items():
        print(f'{stat} = {value}')

