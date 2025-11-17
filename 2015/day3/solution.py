from dataclasses import dataclass
import itertools

visited = {(0, 0)}

token_vectors = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0)
}

@dataclass()
class Santa:
    x: int = 0
    y: int = 0

    def move(self, token: str):
        assert token in token_vectors.keys(), f'{token} is not a valid movement token'
        dx, dy = token_vectors[token]
        self.x += dx
        self.y += dy

        visited.add((self.x, self.y))

def santa_dispatcher(santas, instructions):
    for token, santa in zip(instructions, itertools.cycle(santas)):
        santa.move(token)


if __name__ == '__main__':
    # select an input from arguments or file
    with open('input.txt', 'r') as f:
        puzzle_input = f.read().strip()

    use_robo_santa = input("1 or 2 santas?: ") == '2'

    if use_robo_santa:
        print("Continuing with just one santa")
    else:
        print("Continuing with Santa and Robo Santa")

    santas = []
    santas.append(Santa())
    if use_robo_santa:
        santas.append(Santa())

    santa_dispatcher(santas, puzzle_input)

    houses_visited = len(visited)
    print(f'{houses_visited =}')
