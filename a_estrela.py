
# utility functions for dealing with square grids
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
    if 'start' in style and id == style['start']: r = "A"    # Origem
    if 'goal' in style and id == style['goal']: r = "Z"      # Destino
    if 'path' in style and id in style['path']: r = "@"      # Caminho executo desde a Origem até o destino
    if id in graph.walls: r = "#" * width                    # Desenhando os muros ( Edificios )
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
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
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
  ['G', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
  ['G', 'A', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
  ['G', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
  ['G', 'A', 'E', 'E', 'E', 'E', 'E', 'P', 'P', 'P'],
  ['G', 'A', 'E', 'P', 'P', 'P', 'P', 'P', 'P', 'E'],
  ['G', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'G'],
  ['G', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'G', 'G'],
  ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'A', 'G', 'G'],
  ['G', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'E', 'E'],
  ['G', 'E', 'A', 'A', 'A', 'E', 'E', 'A', 'A', 'A']
]


diagram = GridWithWeights(10, 10)
diagram.walls = []
diagram.weights = {}

for i in range(10):
  for j in range(10):
    if matriz[i][j] == 'E':
      diagram.walls.append((j, i))  # Adiciona nas paredes (Edificios) para ele nao poder passar no trecho, assim ignorando na hora de computar
    elif matriz[i][j] == 'A':
      diagram.weights[(j,i)] = 1  # Adiciona os pesos na fronteiras para o acumulador de custos
    elif matriz[i][j] == 'P':
      diagram.weights[(j,i)] = 3
    elif matriz[i][j] == 'T':
      diagram.weights[(j,i)] = 6
    elif matriz[i][j] == 'G':
      diagram.weights[(j,i)] = 10

import heapq

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
    path.append(start) # optional
    path.reverse() # optional
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


start, goal = (0, 0), (3, 4)
came_from, cost_so_far = a_star_search(diagram, start, goal)
draw_grid(diagram, width=3, point_to=came_from, start=start, goal=goal)  # Atualizando as letras pelo peso em custos
print()
draw_grid(diagram, width=3, number=cost_so_far, start=start, goal=goal)
print()

print('Custo de', start, 'até', goal,'é', cost_so_far[goal])