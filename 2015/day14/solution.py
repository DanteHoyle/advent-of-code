import collections
import itertools
import re

with open('input.txt') as f:
    text = f.read()

regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'

reindeer_results = {}

def reindeer_position(t_seconds, speed, fly_duration, rest_duration):
    velocity_t = itertools.cycle((*([speed] * fly_duration), *([0] * rest_duration)))

    final_position = 0

    for _, v in zip(range(t_seconds), velocity_t):
        final_position += v

    return final_position

final_time = 2503

for name, speed, fly_duration, rest_duration in re.findall(regex, text):
    final_position = reindeer_position(final_time, int(speed), int(fly_duration), int(rest_duration))
    reindeer_results[name] = final_position

ranked_results = sorted(reindeer_results.items(), key=lambda item: item[1])

for rd, pos in ranked_results:
    print(rd, pos)

