
def parse_operation(op):
    direction = op[0]
    magnitude = int(op[1:])
    if direction == 'R':
        return magnitude
    else:
        return -1 * magnitude

if __name__ == '__main__':
    DIAL = list(range(100))
    input_text = open('input.txt').read()
    # input_text = open('example-input.txt').read()

    # SOLUTION A
    times_at_zero = 0
    dial = 50
    print(f'The dial starts at {dial}')
    for line in input_text.splitlines():
        diff = parse_operation(line)
        dial = DIAL[(dial + diff) % 100]

        if dial == 0:
            times_at_zero += 1
        # print(f'The dial is rotated {line} to point at {dial}')

    print(f"SOLUTION A: {times_at_zero}")

    # SOLUTION B

