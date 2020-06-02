import math


class Loja():
    def __init__(self, x, y):
        self.x = x
        self.y = y

TAMANHO = 42

matriz = [
    ['G', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'A', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'A', 'G', 'A', 'A', 'A', 'A', 'A', 'A',
     'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['G', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'A', 'G', 'A', 'P', 'P', 'P', 'P', 'P',
     'P', 'P', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'A', 'E', 'E', 'P', 'P', 'G'],
    ['G', 'A', 'E', 'E', 'E', 'E', 'E', 'P', 'P', 'P', 'P', 'P', 'E', 'P', 'A', 'A', 'A', 'P', 'E', 'E', 'E', 'E',
     'E', 'E', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'E', 'E', 'E', 'A', 'E', 'E', 'P', 'P', 'G'],
    ['G', 'A', 'E', 'P', 'P', 'P', 'P', 'P', 'P', 'E', 'E', 'E', 'E', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
     'P', 'E', 'P', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'E', 'A', 'A', 'A', 'A', 'E', 'P', 'P', 'G'],
    ['G', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'E', 'P', 'P', 'P',
     'P', 'E', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'P', 'G'],
    ['G', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'E',
     'E', 'E', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'G'],
    ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'A', 'A', 'A', 'A', 'T', 'T', 'T',
     'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'G'],
    ['G', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'E', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'E', 'E', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'E', 'A', 'A', 'A', 'E', 'E', 'A', 'A', 'A', 'E', 'A', 'A', 'A', 'E', 'A', 'E', 'G', 'G', 'T', 'T', 'T',
     'T', 'G', 'G', 'G', 'E', 'E', 'E', 'E', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'A', 'E', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'G', 'G', 'T', 'G', 'G',
     'T', 'P', 'P', 'P', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'A', 'E', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'G', 'G', 'T', 'G', 'G',
     'T', 'G', 'T', 'T', 'T', 'G', 'G', 'T', 'T', 'T', 'G', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'A', 'E', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'G', 'G', 'T', 'G', 'G',
     'T', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'P', 'G', 'G', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'A', 'E', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'G', 'P', 'T', 'G', 'G',
     'T', 'G', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'P', 'P', 'P', 'P', 'P', 'P', 'G', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'A', 'A', 'A', 'A', 'E', 'A', 'A', 'A', 'E', 'A', 'A', 'A', 'E', 'G', 'P', 'T', 'T', 'T',
     'T', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'E', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'G', 'P', 'G', 'G', 'G',
     'G', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P',
     'P', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G'],
    ['G', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'G'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
     'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'G', 'E',
     'E', 'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E',
     'E', 'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'G', 'G', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E',
     'E', 'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'G', 'G', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E',
     'E', 'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'T', 'P', 'P', 'P', 'P', 'P', 'P', 'T', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'G', 'G', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'A', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
     'P', 'P', 'P', 'P', 'P', 'G', 'G', 'G', 'T', 'P', 'T', 'P', 'E', 'E', 'E', 'E', 'P', 'T', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'G', 'G', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E',
     'E', 'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'T', 'P', 'E', 'E', 'E', 'E', 'T', 'T', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E',
     'E', 'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'T', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'T'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'P', 'E',
     'E', 'G', 'G', 'E', 'E', 'G', 'G', 'G', 'T', 'P', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T'],
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'A', 'E', 'E', 'G', 'G', 'E', 'E', 'G', 'E',
     'E', 'G', 'G', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
     'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['G', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P',
     'G', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P',
     'G', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'E', 'E', 'E', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P', 'G', 'P',
     'G', 'G', 'G', 'G', 'G', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T'],
    ['G', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'P', 'G', 'G',
     'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'T', 'T', 'T', 'T', 'G', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
     'E', 'E', 'G', 'G', 'P', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'G', 'G', 'G', 'G'],
    ['G', 'E', 'E', 'E', 'G', 'T', 'T', 'T', 'T', 'G', 'E', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'E', 'E', 'E',
     'E', 'E', 'G', 'G', 'P', 'E', 'E', 'G', 'G', 'E', 'E', 'E', 'E', 'E', 'P', 'G', 'A', 'A', 'A', 'A'],
    ['G', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'G', 'E', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'A', 'A', 'A',
     'A', 'E', 'G', 'G', 'P', 'E', 'E', 'G', 'G', 'E', 'E', 'E', 'E', 'E', 'P', 'G', 'P', 'P', 'P', 'P'],
    ['G', 'E', 'E', 'E', 'G', 'T', 'T', 'T', 'T', 'G', 'E', 'A', 'A', 'A', 'E', 'A', 'A', 'A', 'A', 'E', 'E', 'E',
     'E', 'E', 'G', 'G', 'P', 'E', 'E', 'G', 'G', 'E', 'E', 'E', 'E', 'E', 'P', 'G', 'E', 'E', 'E', 'E'],
    ['G', 'E', 'E', 'E', 'G', 'T', 'T', 'T', 'T', 'G', 'E', 'E', 'E', 'A', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
     'E', 'E', 'G', 'G', 'P', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'P', 'G', 'A', 'A', 'A', 'A'],
    ['G', 'E', 'E', 'E', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'A', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'G', 'G', 'G', 'G', 'T']
]

class Mapa():
    def __init__(self, matriz, exibir_cores=False):
        self.exibir_cores = exibir_cores
        self.mapa = []
        for i in range(0, TAMANHO):
            self.mapa.append([])
            coordenada = Coordenada(0, 0)
            for j in range(0, TAMANHO):
                if matriz[i][j] == "G":
                    coordenada = Coordenada(i, j, '.', 10)
                elif matriz[i][j] == "A":
                    coordenada = Coordenada(i, j, '.', 1)
                elif matriz[i][j] == "P":
                    coordenada = Coordenada(i, j, '.', 3)
                elif matriz[i][j] == "T":
                    coordenada = Coordenada(i, j, '.', 6)
                elif matriz[i][j] == "E":
                    coordenada = Coordenada(i, j, '#', -1)
                self.mapa[i].append(coordenada)

    def reset_mapa(self, agente, revendas, pessoas):
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                self.mapa[i][j].F = math.inf
                self.mapa[i][j].G = math.inf
                if self.mapa[i][j].tipo == "#":
                    self.mapa[i][j].tipo = "#"
                else:
                    self.mapa[i][j].tipo = "."
        for revenda in revendas:
            self.mapa[revenda.x][revenda.y].tipo = "R"
        for pessoa in pessoas.queue:
            self.mapa[pessoa[1].x][pessoa[1].y].tipo = "P"
            self.mapa[pessoa[1].casa_x][pessoa[1].casa_y].tipo = "C"
        self.mapa[agente.x][agente.y].tipo = "A"

    def mostrar_mapa(self):
        if self.exibir_cores:
            cores = {
                ".": '\33[1:30:40m',
                "#": '\33[1:31:41m',
                "P": '\33[1:33:43m',
                "A": '\33[1:34:44m',
                "R": '\33[1:35:45m',
                "C": '\33[1:36:46m',
                "|": '\33[1:32:42m',
            }
        else:
            cores = {
                ".": '',
                "#": '',
                "P": '',
                "A": '',
                "R": '',
                "C": '',
                "|": '',
            }
        print("Áreas")
        print("")
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                print(cores[self.mapa[i][j].tipo] + self.mapa[i][j].tipo, end=" ")
                print('\33[0:0m', end="")
            print('')
        print("")

    def apresenta_map_G(self):
        print("")
        print("Mapa - Visão G")
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                print(self.mapa[i][j].G, end=" ")
            print('')
        print("")

    def apresenta_map_F(self):
        print("")
        print("Mapa - Visão F")
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                print(self.mapa[i][j].F, end=" ")
            print('')
        print("")


class Coordenada():
    def __init__(self, x, y, tipo=".", peso=0, veio_de_y=0):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.peso = peso
        self.F = math.inf
        self.G = math.inf
        self.veio_de_x = 0
        self.veio_de_y = 0

    def __repr__(self):
        return "(%s,%s)" % (self.x, self.y)

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        return self.y <= other.y

    def atribuir_valores(self, F, G):
        self.F = F
        self.G = G

    def valido(self):
        if self.tipo == "#":
            return False
        return True


class Pessoa():
    def __init__(self, x, y, casa_x, casa_y, ajuda=True):
        self.x = x
        self.y = y
        self.casa_x = casa_x
        self.casa_y = casa_y
        self.ajuda = ajuda

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        return self.y <= other.y


class Agente():
    def __init__(self, x, y, mapa, sucesso=False):
        self.x = x
        self.y = y
        self.sucesso = sucesso
        mapa.mapa[self.x][self.y].tipo = "A"


