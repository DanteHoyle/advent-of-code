from enum import Enum

class BooleanLights:
    def __init__(self, *, width=1000, height=1000, init_state=False):
        self.lights = []

        for y in range(height):
            self.lights.append([])

            for _ in range(width):
                self.lights[y].append(init_state)

    def enable(self, x, y):
        self.lights[y][x] = True

    def disable(self, x, y):
        self.lights[y][x] = False

    def toggle(self, x, y):
        self.lights[y][x] = not self.lights[y][x]

    def count_on(self):
        count = 0
        for row in self.lights:
            count += sum(row)

        return count

class IntLights:
    def __init__(self, *, width=1000, height=1000, init_brightness=0):
        self.lights = []

        for y in range(height):
            self.lights.append([])

            for _ in range(width):
                self.lights[y].append(init_brightness)

    def change_brightness(self, x, y, amount):
        new_brightness = self.lights[y][x] + amount
        self.lights[y][x] = max(0, new_brightness)

    def check_brightness(self):
        brightness = 0
        for row in self.lights:
            brightness += sum(row)

        return brightness

class Commands(str, Enum):
    TURN_ON = 'turn on'
    TURN_OFF = 'turn off'
    TOGGLE = 'toggle'

def command_line_parser(text: str):
    command = None

    for potential_command in Commands:
        if text.startswith(potential_command.value):
            command = potential_command
            break

    assert command, f'failed to detect command from {text}'

    range_text = text[len(command.value):].strip()

    p0_text, p1_text = range_text.split('through')

    x0_text, y0_text = p0_text.split(',')
    x0 = int(x0_text)
    y0 = int(y0_text)

    x1_text, y1_text = p1_text.split(',')
    x1 = int(x1_text)
    y1 = int(y1_text)

    return command, (x0, y0), (x1, y1)

def points_in_rect(x0, y0, x1, y1):
    for y in range(y0, y1+1):
        for x in range(x0, x1+1):
            yield x, y

def run_command(lights: BooleanLights|IntLights, command: Commands, start: tuple[int, int], stop: tuple[int, int]):
    if type(lights) == BooleanLights:
        match command:
            case  Commands.TURN_ON:
                func = lights.enable
            case Commands.TURN_OFF:
                func = lights.disable
            case Commands.TOGGLE:
                func = lights.toggle

        for x, y in points_in_rect(*start, *stop):
            func(x, y)
    elif type(lights) == IntLights:
        match command:
            case  Commands.TURN_ON:
                amount = 1
            case Commands.TURN_OFF:
                amount = -1
            case Commands.TOGGLE:
                amount = 2
        for x, y in points_in_rect(*start, *stop):
            lights.change_brightness(x, y, amount)



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input_text = f.read()

    xmas_lights = BooleanLights()
    xmas_lights_v2 = IntLights()

    for line in input_text.splitlines():
        command = command_line_parser(line)
        run_command(xmas_lights, *command)
        run_command(xmas_lights_v2, *command)

    print(xmas_lights.count_on())
    print(xmas_lights_v2.check_brightness())
