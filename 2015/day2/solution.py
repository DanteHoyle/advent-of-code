def parse_string_to_dimensions(s: str) -> tuple[int, int, int]:
    numbers = s.split('x')
    assert len(numbers) == 3, f'{s} is not a valid dimension string (expected value like 10x20x3)'

    length, width, height = (int(n) for n in numbers)
    return length, width, height

def calculate_needed_wrapping_paper(length: int, width: int,  height: int) -> int:
    '''answer calculated in square feet'''
    sides = [
        length * width,
        width * height,
        height * length
    ]

    surface_area = 2 * sum(sides)
    extra_paper = min(sides)

    return surface_area + extra_paper

def calculate_needed_ribbon(length: int, width: int, height: int) -> int:
    perimeters = [
        2*length + 2*width,
        2*length + 2*height,
        2*width + 2*height,
    ]

    perimeter_ribbon = min(perimeters)

    # used for bow
    volume = length * width * height

    return perimeter_ribbon + volume

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read().strip()

    paper_to_order = 0
    ribbon_to_order = 0

    for box_strings in input.splitlines():
        dimensions = parse_string_to_dimensions(box_strings)
        paper_to_order += calculate_needed_wrapping_paper(*dimensions)
        ribbon_to_order += calculate_needed_ribbon(*dimensions)

    print(paper_to_order)
    print(ribbon_to_order)
