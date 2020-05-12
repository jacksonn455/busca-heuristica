import random
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


class Mapa():

    def __init__(self,caminho):
        self.arq = open(caminho, 'r')         # abre o arquivo
        self.matriz = {} # declaro o vetor 2


    def gera_mapa(self,n_colunas,n_linhas):
        count = 0 # inicia contador
        agrupa = "" #inicia var para agrupar as letras da lista
        lista = self.arq.read().split("\n")

        while(len(lista) != count):

            agrupa += lista[count]
            count+=1

        count = 0
        matrizaux = {}
        for i in range(0,n_colunas):
            temp = {}
            for j in range(0,n_linhas):
                if(agrupa[count] == "G"):
                    elemento = 10
                elif (agrupa[count] == "A"):
                    elemento = 1
                elif (agrupa[count] == "P"):
                    elemento = 3
                elif (agrupa[count] == "T"):
                    elemento = 6
                elif (agrupa[count] == "E"):
                    elemento = 0
                count += 1
                self.matriz[(i,j)] = elemento

        return self.matriz



def from_id_width(id, width):
    return (id % width, id // width)


def draw_tile(graph, id, style, width,valor):

    r = valor
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = ">"
        if x2 == x1 - 1: r = "<"
        if y2 == y1 + 1: r = "v"
        if y2 == y1 - 1: r = "^"
    if 'start' in style and id == style['start']: r = "X"    # Origem
    if 'goal' in style and id == style['goal']: r = "Z"      # Destino
    if 'path' in style and id in style['path']: r = "@"      # Caminho executo desde a Origem até o destino
    if id in graph.walls: r = "#" * width                    # Desenhando os muros ( Edificios )
    return r



def draw_grid(graph, agente , width=2, **style):
    arquivo = open('mapa.txt', 'r')

    count = 0  # inicia contador
    agrupa = ""  # inicia var para agrupar as letras da lista
    lista = arquivo.read().split("\n")  # le as linhas do arquivo cortando nas quebras de lihas

    while (len(lista) != count):  # loop para agrupamento dos caracteres
        agrupa += lista[count]
        count+=1
    count=0
    for y in range(graph.height):
        for x in range(graph.width):
            if((x,y) in agente):
                print("%%-%ds" % width % draw_tile(graph, (x, y), style, width,"F"), end="")
            else:
                print("%%-%ds" % width % draw_tile(graph, (x, y), style, width, agrupa[count]), end="")
            count+=1
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

mapa = Mapa('mapa.txt')
matriz = mapa.gera_mapa(42,42)
diagram = GridWithWeights(42, 42)
contador = 0



print(matriz)

diagram.weights = matriz


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
a = 21
b = 25
sorteado = []
termina = 1
start = (a, b)

soma = 0

while(termina != 4):  # Gera as pessoas para a matriz


    x = random.randint(0, 41)  # sorteia a coluna
    y = random.randint(0, 41)  # sorteia a linha
    goal = (x, y)


    if(goal not in sorteado):

        came_from, cost_so_far = a_star_search(diagram, start, goal)
        draw_grid(diagram, agente, width=4, number=cost_so_far, start=start, goal=goal)
        soma+=cost_so_far[goal]


        print()
        print("Custo: {}".format(soma))
        print()
        if (goal in agente):

            termina += 1
            print("agente achou a pessoa {0} de 3 , achado na pos {1}".format(termina, goal))

        start = goal

        for i in range(x+4):
            for j in range(y+4):
                verifica.append((i,j));
                if((i,j) in agente):
                    goal = (i,j)
                    came_from, cost_so_far = a_star_search(diagram, start, goal)
                    draw_grid(diagram, agente, width=4, number=cost_so_far, start=start, goal=goal)
                    soma+= cost_so_far[goal]

                    print()
                    print("Custo: {}".format(soma))
                    print("agente achou a pessoa {0} de  3 , achado na pos {1}".format(termina,goal))
                    print()
                    termina += 1
                    start = goal
                    agente.remove(goal)
                    sorteado.append(goal)

        sorteado.append(goal)