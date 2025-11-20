import collections
import itertools
import math

class RouteTable:
    def __init__(self):
        self.routes: dict[str, dict[str, int]] = collections.defaultdict(dict)

    def add_route(self, a: str, b: str, distance: int):
        self.routes[a][b] = distance
        self.routes[b][a] = distance

    def get_adjacent_nodes(self, node) -> list[tuple[str, int]]:
        adjacent_routes = self.routes[node]

        adjacencies: list[tuple[str, int]] = []

        for destination, cost in adjacent_routes.items():
            adjacencies.append((destination, cost))

        return adjacencies

    def distance(self, path: tuple[str, ...]) -> int:
        cost = 0
        for a, b in itertools.pairwise(path):
            cost += self.routes[a][b]

        return cost

def parse_line(line: str) -> tuple[str, str, int]:
    cities, cost = line.split(' = ')
    city_a, city_b = cities.split(' to ')

    return city_a.strip(), city_b.strip(), int(cost)

if __name__ == '__main__':
    with open('input.txt') as f:
        puzzle_input = f.read()

    routes = RouteTable()

    for line in puzzle_input.splitlines():
        a, b, cost = parse_line(line)
        routes.add_route(a, b, cost)

    cities = list(routes.routes.keys())

    order_permutations = itertools.permutations(cities)

    shortest_path = None
    shortest_distance = math.inf
    longest_path = None
    longest_distance = 0

    for route in order_permutations:
        distance = routes.distance(route)
        print(route, distance)

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = route

        if distance > longest_distance:
            longest_distance = distance
            longest_path = route


    print('Part 1:')
    print('Shortest Path Distance', shortest_distance, 'Distance:', shortest_path, '\n')
    print('Part 2:')
    print('Longest Path Distance', longest_distance, 'Distance:', longest_path, '\n')
