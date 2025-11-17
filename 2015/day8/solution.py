import ast

def length_of_literal(string: str) -> int:
    return len(string)

def length_of_string(string: str) -> int:
    return len(ast.literal_eval(string))

def encode_string(string: str) -> str:
    escaped = string.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'

if __name__ == '__main__':
    with open('input.txt') as f:
        puzzle_input = f.read()

    literal_sum = 0
    string_sum = 0
    encoded_sum = 0

    for line in puzzle_input.splitlines():
        string = line.strip()
        encoded_string = encode_string(string)

        literal_len = length_of_literal(string)
        literal_sum += literal_len

        string_len = length_of_string(string)
        string_sum += string_len

        encoded_len = length_of_literal(encoded_string)
        encoded_sum += encoded_len

        print(string)
        print(encoded_string)
        print(f'LL: {literal_len}, SL: {string_len}, EL: {encoded_len}\n')

    print('-------------------------------------------\n')
    print('Part One Answer:', literal_sum - string_sum)
    print('Part Two Answer:', encoded_sum - literal_sum)
