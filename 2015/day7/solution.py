import sys

type WireState = dict[str, str | int]

# mask all math to 16 bit integer math using this constant
UINT16_MAX = 0xFFFF

def load_wirestate(input: str) -> WireState:
    state: WireState = {}
    for line in input.splitlines():
        expr, wire = line.split('->')
        state[wire.strip()] = expr.strip()

    return state

def parse(state: WireState, expr: str) -> int:
    if expr.isdigit():
        # expr is just a number
        return int(expr)
    elif expr in state.keys():
        # expr is a wire name
        return find_wire_val(state, expr)

    match expr.split():
        case (left, 'AND', right):
            value = parse(state, left) & parse(state, right)
        case (left, 'OR', right):
            value = parse(state, left) | parse(state, right)
        case (left, 'LSHIFT', right):
            value = parse(state, left) << parse(state, right)
        case (left, 'RSHIFT', right):
            value = parse(state, left) >> parse(state, right)
        case ('NOT', expr):
            value = ~parse(state, expr)
        case _:
            print(f'failed to evaluate {expr}', file=sys.stderr)
            raise ValueError

    return value & UINT16_MAX

def find_wire_val(state: WireState, wire: str) -> int:
    expr = state[wire]

    # if wire value has been solved, just return it
    if isinstance(expr, int):
        return expr

    # parse statement that defines wire value, and then save its integer representation
    parsed_value = parse(state, expr)
    state[wire] = parsed_value
    return parsed_value

if __name__ == '__main__':
    with open('input.txt') as f:
        puzzle_input = f.read()

    print("Part 1:")
    state = load_wirestate(puzzle_input)
    print('a:', find_wire_val(state, 'a'))

    print("\nPart 2")
    state = load_wirestate(puzzle_input)
    state['b'] = '46065'
    print('a:', find_wire_val(state, 'a'))
