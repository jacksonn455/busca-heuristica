import heapq
import random

class Agente():
    def __init__(self):
        self.agente = []

    def cria_agente(self):
        for i in range(3):  # Gera as pessoas a procura de alcool gel para a matriz
            x = random.randint(0, 41)  # sorteia a coluna
            y = random.randint(0, 41)  # sorteia a linha
            self.agente.append((x, y))

    def pega_agente(self):
        return self.agente


def from_id_width(id, width):
    return (id % width, id // width)


def draw_tile(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = ">"
        if x2 == x1 - 1: r = "<"
        if y2 == y1 + 1: r = "v"
        if y2 == y1 - 1: r = "^"
    if 'start' in style and id == style['start']: r = "A"
    if 'goal' in style and id == style['goal']: r = "Z"
    if 'path' in style and id in style['path']: r = "@"
    if id in graph.walls: r = "#" * width
    return r


def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()



class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)


matriz = [
    ['G', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'A', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'A', 'G', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
     'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['G', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'A', 'G', 'A', 'P', 'P', 'P', 'P', 'P', 'P',
     'P', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'A', 'E', 'E', 'P', 'P', 'G'],
    ['G', 'A', 'E', 'E', 'E', 'E', 'E', 'P', 'P', 'P', 'P', 'P', 'E', 'P', 'A', 'A', 'A', 'P', 'E', 'E', 'E', 'E', 'E',
     'E', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'E', 'E', 'E', 'A', 'E', 'E', 'P', 'P', 'G'],
    ['G', 'A', 'E', 'P', 'P', 'P', 'P', 'P', 'P', 'E', 'E', 'E', 'E', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
     'E', 'P', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'E', 'A', 'A', 'A', 'A', 'E', 'P', 'P', 'G'],
    ['G', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'E', 'P', 'P', 'P', 'P',
     'E', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'P', 'G'],
    ['G', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'E', 'E',
     'E', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'G'],
    ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'A', 'A', 'A', 'A', 'T', 'T', 'T', 'T',
     'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'G'],
    ['G', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'E', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'E', 'E', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'E', 'A', 'A', 'A', 'E', 'E', 'A', 'A', 'A', 'E', 'A', 'A', 'A', 'E', 'A', 'E', 'G', 'G', 'T', 'T', 'T', 'T',
     'G', 'G', 'G', 'E', 'E', 'E', 'E', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'A', 'E', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'G', 'G', 'T', 'G', 'G', 'T',
     'P', 'P', 'P', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'A', 'E', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'G', 'G', 'T', 'G', 'G', 'T',
     'G', 'T', 'T', 'T', 'G', 'G', 'T', 'T', 'T', 'G', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'A', 'E', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'G', 'G', 'T', 'G', 'G', 'T',
     'G', 'G', 'P', 'P', 'P', 'P', 'P', 'P', 'G', 'G', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'A', 'E', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'G', 'P', 'T', 'G', 'G', 'T',
     'G', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'P', 'P', 'P', 'P', 'P', 'P', 'G', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'A', 'A', 'A', 'A', 'E', 'A', 'A', 'A', 'E', 'A', 'A', 'A', 'E', 'G', 'P', 'T', 'T', 'T', 'T',
     'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'G', 'P', 'G', 'G', 'G', 'G',
     'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P',
     'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'G'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
     'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'G', 'E', 'E',
     'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E', 'E',
     'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'G', 'G', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E', 'E',
     'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'G', 'G', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E', 'E',
     'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'T', 'P', 'P', 'P', 'P', 'P', 'P', 'T', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'G', 'G', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'A', 'P', 'P', 'P', 'P', 'P', 'P', 'X', 'P', 'P',
     'P', 'P', 'P', 'P', 'G', 'G', 'G', 'T', 'P', 'T', 'P', 'E', 'E', 'E', 'E', 'P', 'T', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'G', 'G', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E', 'E',
     'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'T', 'P', 'E', 'E', 'E', 'E', 'T', 'T', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E', 'E',
     'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'T', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E', 'E',
     'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'G', 'E', 'E',
     'G', 'G', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
     'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['G', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G',
     'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G',
     'G', 'G', 'G', 'G', 'E', 'E', 'E', 'E', 'E', 'E', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G',
     'G', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T'],
    ['G', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G',
     'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'T', 'T', 'T', 'T', 'G', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
     'E', 'G', 'G', 'P', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'T', 'T', 'T', 'T', 'G', 'E', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'E', 'E', 'E', 'E',
     'E', 'G', 'G', 'P', 'E', 'E', 'G', 'G', 'E', 'E', 'E', 'E', 'E', 'P', 'G', 'A', 'A', 'A', 'A'],
    ['G', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'G', 'E', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'A', 'A', 'A', 'A',
     'E', 'G', 'G', 'P', 'E', 'E', 'G', 'G', 'E', 'E', 'E', 'E', 'E', 'P', 'G', 'P', 'P', 'P', 'P'],
    ['G', 'E', 'E', 'E', 'G', 'T', 'T', 'T', 'T', 'G', 'E', 'A', 'A', 'A', 'E', 'A', 'A', 'A', 'A', 'E', 'E', 'E', 'E',
     'E', 'G', 'G', 'P', 'E', 'E', 'G', 'G', 'E', 'E', 'E', 'E', 'E', 'P', 'G', 'E', 'E', 'E', 'E'],
    ['G', 'E', 'E', 'E', 'G', 'T', 'T', 'T', 'T', 'G', 'E', 'E', 'E', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
     'E', 'G', 'G', 'P', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'A', 'A', 'A', 'A'],
    ['G', 'E', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'G', 'G', 'G', 'G', 'T']
]

diagram = GridWithWeights(42, 42)
diagram.walls = []
diagram.weights = {}

for i in range(10):
    for j in range(10):
        if matriz[i][j] == 'E':
            diagram.walls.append((j, i))
        elif matriz[i][j] == 'A':
            diagram.weights[(j, i)] = 1
        elif matriz[i][j] == 'P':
            diagram.weights[(j, i)] = 3
        elif matriz[i][j] == 'T':
            diagram.weights[(j, i)] = 6
        elif matriz[i][j] == 'G':
            diagram.weights[(j, i)] = 10


def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return path


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far



cria_agente = Agente()
cria_agente.cria_agente()

agente = cria_agente.pega_agente()
termina = 0
verifica = []
a = 20  # linha 21, começando do 0
b = 24  # coluna 25, começando do 0
sorteado = []
termina = 1
start = (a, b)  # posicao inicial [21,25]
frasco = 3
soma = 0

while (termina != 4):  # Gera as pessoas para a matriz

    x = random.randint(0, 41)  # sorteia a coluna
    y = random.randint(0, 41)  # sorteia a linha
    goal = (x, y)

    if (goal not in sorteado):
        alcool = random.choice([True, False])
        came_from, cost_so_far = a_star_search(diagram, start, goal)
        draw_grid(diagram, width=4, point_to=came_from, start=start, goal=goal)
        print()
        draw_grid(diagram, width=4, number=cost_so_far, start=start, goal=goal)
        print()
        soma += cost_so_far[goal]

        print()
        print("Custo: {}".format(soma))
        print()
        if (goal in agente):
            termina += 1

        start = goal

        for i in range(x + 4):
            for j in range(y + 4):
                verifica.append((i, j));
                if ((i, j) in agente):
                    goal = (i, j)
                    came_from, cost_so_far = a_star_search(diagram, start, goal)
                    draw_grid(diagram, width=4, point_to=came_from, start=start, goal=goal)
                    print()
                    draw_grid(diagram, width=4, number=cost_so_far, start=start, goal=goal)
                    print()
                    soma += cost_so_far[goal]

                    print()
                    print("Custo: {}".format(soma))
                    if alcool is True:  # Se a pessoa aceita ir para casa
                        print(
                            "O agente convenceu a pessoa {0} na posição {1} a ir para casa".format(
                                termina, goal))
                        termina += 1
                        start = goal
                        agente.remove(goal)
                    elif alcool is False:
                        frasco -= 1  # diminui um frasco do agente
                        print("O agente nao convenceu a pessoa a ir para casa, mas a pessoa aceitou o frasco de alcool gel")
                    print()
        sorteado.append(goal)
