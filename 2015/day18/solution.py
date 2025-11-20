import copy
import enum

class LightState(str, enum.Enum):
    ON = '#'
    OFF = '.'

# tuples of x, y offsets from a cell to get it's relative neighbor

type Vec2 = tuple[int, int]

neighboring_vectors = [
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
]

class Lights:
    def __init__(self, width: int, height: int, stuck: list[Vec2]=[]):
        self.lights: list[list[LightState]] = [[LightState.OFF for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height
        self.stuck = stuck
        self.iterations = 0

        if self.stuck:
            for x, y in self.stuck:
                # set directly since set() will ignore attempts to set this coordinate
                self.lights[y][x] = LightState.ON

    def get(self, x: int, y: int) -> LightState | None:
        x_in_bounds = 0 <= x < self.width
        y_in_bounds = 0 <= y < self.height
        out_of_bounds = not (x_in_bounds and y_in_bounds)

        if (x, y) in self.stuck:
            return LightState.ON

        if out_of_bounds:
            return None

        return self.lights[y][x]

    def set(self, x: int, y: int, state: LightState):
        if (x, y) in self.stuck:
            return
        self.lights[y][x] = state

    def next_state(self, x, y):
        ch = self.get(x, y)
        assert ch
        if (x, y) in self.stuck:
            return LightState.ON
        is_on = ch == LightState.ON

        neighbors_on = 0
        for ch in self.neighbors(x, y):
            if ch == LightState.ON:
                neighbors_on += 1

        if is_on:
            if neighbors_on >= 2 and neighbors_on <= 3:
                return LightState.ON
            else:
                return LightState.OFF
        else:
            return LightState.ON if neighbors_on == 3 else LightState.OFF

    def count(self):
        lights_on = 0
        for row in self.lights:
            for light in row:
                if light == LightState.ON:
                    lights_on += 1

        return lights_on


    def neighbors(self, x, y):
        for vec in neighboring_vectors:
            new_x = vec[0] + x
            new_y = vec[1] + y

            ch = self.get(new_x, new_y)
            if ch is None:
                continue
            yield ch

    def print(self):
        if self.iterations == 0:
            print('INITIAL STATE')
        else:
            print('ITERATIONS:', self.iterations)
        for row in self.lights:
            print(''.join((c.value for c in row)))

    def iterate(self):
        buffer = copy.deepcopy(self.lights)
        for y in range(self.height):
            for x in range(self.width):
                buffer[y][x] = self.next_state(x, y)

        self.lights = buffer
        self.iterations += 1

    @classmethod
    def load_state(cls, text: str, stuck: list[Vec2]=[]):
        lines = text.splitlines()

        width = len(lines[0])
        height = len(lines)

        l = cls(width, height, stuck)

        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                l.set(x, y, LightState(ch))

        return l

if __name__ == '__main__':
    text = open('input.txt').read()
    lights = Lights.load_state(text)
    for i in range(100):
        lights.iterate()

    print('part one:', lights.count())

    lights2 = Lights.load_state(text, stuck=[(0, 0), (0, 99), (99, 0), (99, 99)])
    for i in range(100):
        lights2.iterate()
    print('part two:', lights2.count())
