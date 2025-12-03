
DIAL = list(range(100))

def parse_operation(op: str) -> int:
    '''
    parses operations like L23 or R44 into a signed integer
    L23 -> -23
    R1 -> 1
    '''
    direction = op[0]
    magnitude = int(op[1:])
    if direction == 'R':
        return magnitude
    else:
        return -1 * magnitude

def part_one(instructions: str):
    times_at_zero = 0
    dial = 50
    print(f'The dial starts at {dial}')
    for line in instructions.splitlines():
        diff = parse_operation(line)
        dial = DIAL[(dial + diff) % 100]

        if dial == 0:
            times_at_zero += 1
        # print(f'The dial is rotated {line} to point at {dial}')

    return times_at_zero

def part_two(instructions: str):
    '''This is an extremely naive approach at solving the problem, but for the input size it still completes very fast.'''
    total_times_at_zero = 0
    dial = 50

    operations = [parse_operation(line) for line in instructions.splitlines()] 

    # print(f'Dial Start: {dial}')
    for op in operations:
        going_right = op > 0
        op_times_at_zero = 0

        for _ in range(abs(op)):
            if going_right:
                dial += 1
            else:
                dial -= 1

            if dial == 100:
                dial = 0
            elif dial == -1:
                dial = 99

            if dial == 0:
                op_times_at_zero += 1

        # print('> {0:+} -> {1} [{2}]'.format(op, dial, op_times_at_zero))
        total_times_at_zero += op_times_at_zero

    return total_times_at_zero

if __name__ == '__main__':
    input_text = open('input.txt').read()
    # input_text = open('example-input.txt').read()

    answer1 = part_one(input_text)
    print(f"SOLUTION A: {answer1}")

    # SOLUTION B
    answer2 = part_two(input_text)
    print(f"SOLUTION B: {answer2}")
