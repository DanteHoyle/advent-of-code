def look_and_say(digits: str):
    final = ''
    current_digit = ''
    count = 0

    for d in digits:
        if current_digit == '':
            current_digit = d
            count = 1
            continue
        if d == current_digit:
            count += 1
            continue

        final += str(count) + str(current_digit)

        current_digit = d
        count = 1

    final += str(count) + str(current_digit)

    return final

def interpreter():
    MAX_DISPLAY = 64
    def help():
        print('enter a number to have it turned get its look and say value')
        print('press enter with no input to use the previous output as new input')
        print('use "exit" to quit and "help" to see this message again')

    help()

    output = ''
    iteration = 1
    while True:
        user_input = input('> ')

        if user_input == '':
            digits = output
            iteration += 1
        elif user_input.isdigit():
            digits = user_input
        elif user_input in ('q', 'Q', 'quit', 'exit'):
            break
        elif user_input in ('h', 'H', 'help'):
            help()
            continue
        else:
            print(f'{user_input} is not valid')
            continue

        output = look_and_say(digits)
        length = len(output)

        display = output if length < MAX_DISPLAY else output[:MAX_DISPLAY] + '...'

        print(f'Iteration {iteration}: Length={length}')
        print(display)

if __name__ == '__main__':
    interpreter()
