valid_chars = '0123456789-'

def extract_numbers(s: str):
    current_block = []
    for c in s:
        if c in valid_chars:
            current_block.append(c)
        elif len(current_block) > 0:
            number = ''.join(current_block)
            yield number
            current_block = []

    if current_block:
        yield ''.join(current_block)

with open('input.txt', 'r') as f:
    input_text = f.read()

sum = 0
for n in extract_numbers(input_text):
    print(f'+{n}')
    sum += int(n)

print(f'= {sum}')
