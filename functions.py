"""
Definições\criações das funções que serão utilizadas no arquivo main do nosso projeto.

- Implementação da função de busca.
- definição da função para busca de pessoas dentro no mapa;
- definição de locais onde podem ser encontrados os itens;
- encaminhamento das pessoas sorteadas ao seu destino final(casa);
- Acompanhamento de localização de agente e pessoa auxiliada.
"""


from queue import PriorityQueue
from models import *
from random import *



# Nesta função efetuaremos a aplicação da busca heurística

def heuristica(atual, destino):
    return abs(atual.x - destino.x) + abs(atual.y - destino.y)

def busca_heuristica(mapa, origem, destino):
    front = PriorityQueue()
    front.put([0, origem])

    mapa.mapa[origem.x][origem.y].atribuir_valores(heuristica(origem, destino), 0)

    while not front.empty():
        atual = front.get()[1]
        if atual.x == destino.x and atual.y == destino.y:
            print("Você chegou no seu destino (%s,%s)" % (atual.x, atual.y))
            while not front.empty():
                front.get()
            break

        for vizinho in vizinhos(atual, mapa):
            custo_atual = vizinho.peso + atual.G


            if custo_atual < mapa.mapa[vizinho.x][vizinho.y].G:
                mapa.mapa[vizinho.x][vizinho.y].veio_de_x = atual.x
                mapa.mapa[vizinho.x][vizinho.y].veio_de_y = atual.y
                mapa.mapa[vizinho.x][vizinho.y].G = custo_atual
                mapa.mapa[vizinho.x][vizinho.y].F = custo_atual + heuristica(vizinho, destino)
                front.put((mapa.mapa[vizinho.x][vizinho.y].F, mapa.mapa[vizinho.x][vizinho.y]))
    reconstruir_caminho(origem, destino, mapa)
    return destino.G


# Definição de função para sorteio de pessoa no mapa:
def sort_pessoa(mapa):
    pessoas = PriorityQueue()
    qtde_pessoas = 0

    while qtde_pessoas < 3:
        x = int(random() * TAMANHO)
        y = int(random() * TAMANHO)
        casa_x = int(random() * TAMANHO)
        casa_y = int(random() * TAMANHO)
        if not mapa.mapa[x][y].valido() or not mapa.mapa[x][y].tipo == ".":
            continue
        if not mapa.mapa[casa_x][casa_y].valido() or not mapa.mapa[casa_x][casa_y].tipo == ".":
            continue
        if casa_x == x or casa_y == y:
            continue
        mapa.mapa[casa_x][casa_y].tipo = "C"
        mapa.mapa[x][y].tipo = "P"
        pessoa = Pessoa(x, y, casa_x, casa_y)
        pessoas.put((random() * 100, pessoa))
        qtde_pessoas += 1

    qtde_pessoas = 0

    while qtde_pessoas < 3:
        x = int(random() * TAMANHO)
        y = int(random() * TAMANHO)
        casa_x = int(random() * TAMANHO)
        casa_y = int(random() * TAMANHO)
        if not mapa.mapa[x][y].valido() or not mapa.mapa[x][y].tipo == ".":
            continue
        if not mapa.mapa[casa_x][casa_y].valido() or not mapa.mapa[casa_x][casa_y].tipo == ".":
            continue
        mapa.mapa[x][y].tipo = "P"
        mapa.mapa[casa_x][casa_y].tipo = "C"
        pessoa = Pessoa(x, y, casa_x, casa_y, False)
        pessoas.put((int(random() * 100), pessoa))
        qtde_pessoas += 1
    return pessoas

# Nestas função faremos a busca pelo alcool em gel
def buscar_alcool(mapa, agente, lojas):
    loja = choice(lojas)
    print("O Agente se econtra (%s,%s) e irá buscar alcool gel na localização (%s,%s)" % (agente.x, agente.y, loja.x, loja.y))
    origem = mapa.mapa[agente.x][agente.y]
    destino = mapa.mapa[loja.x][loja.y]
    print("Custo operação : %s" % (busca_heuristica(mapa, origem, destino)))
    agente.x = loja.x
    agente.y = loja.y
    print("O Agente na localização (%d,%d) buscando alcool gel" % (agente.x, agente.y))
    mapa.mostrar_mapa()
    print("")

# Definimos a função que irá encontrar pessoas a serem auxiliadas
def busca_pessoa(mapa, agente, pessoa):
    print("O Agente está no (%d,%d) e está indo até na pessoa que está na localização (%d,%d)" % (agente.x, agente.y, pessoa.x, pessoa.y))
    origem = mapa.mapa[agente.x][agente.y]
    destino = mapa.mapa[pessoa.x][pessoa.y]
    print("Custo operação : %s" % (busca_heuristica(mapa, origem, destino)))
    agente.x = pessoa.x
    agente.y = pessoa.y
    agente.sucesso = pessoa.ajuda
    print("O Agente na posição (%d,%d) acompanhado por uma pessoa" % (agente.x, agente.y))
    mapa.mostrar_mapa()
    print("")




def reconstruir_caminho(origem, destino, mapa):
    atual = destino
    d_tipo = destino.tipo
    while atual.x != origem.x or atual.y != origem.y:
        mapa.mapa[atual.x][atual.y].tipo = "|"
        veio_de_x = mapa.mapa[atual.x][atual.y].veio_de_x
        veio_de_y = mapa.mapa[atual.x][atual.y].veio_de_y
        atual = mapa.mapa[veio_de_x][veio_de_y]
    mapa.mapa[origem.x][origem.y].tipo = "A"
    mapa.mapa[destino.x][destino.y].tipo = d_tipo


def vizinhos(atual, mapa):
    vizinhos = []
    DIRECOES = [
        Coordenada(0, -1),
        Coordenada(0, 1),
        Coordenada(1, 0),
        Coordenada(-1, 0)
    ]

    for dir in DIRECOES:
        vizinho_x = atual.x + dir.x
        vizinho_y = atual.y + dir.y
        if TAMANHO > vizinho_x >= 0 and TAMANHO > vizinho_y >= 0:
            if mapa.mapa[vizinho_x][vizinho_y].valido():
                vizinhos.append(mapa.mapa[vizinho_x][vizinho_y])
    return vizinhos


def sorteia_ponto_vendas(mapa):
    lojas = []
    numero_de_lojas = 0

    while numero_de_lojas < 3:
        x = int(random() * TAMANHO)
        y = int(random() * TAMANHO)
        if not mapa.mapa[x][y].valido() or not mapa.mapa[x][y].tipo == ".":
            continue
        mapa.mapa[x][y].tipo = "R"
        loja = Loja(x, y)
        lojas.append(loja)
        numero_de_lojas += 1

    return lojas


def acompanha_para_moradia(mapa, agente, pessoa):
    print("Posição (%d,%d) acompanhando a pessoa para casa na posição (%d,%d)" % (agente.x, agente.y, pessoa.casa_x, pessoa.casa_y))
    origem = mapa.mapa[agente.x][agente.y]
    destino = mapa.mapa[pessoa.casa_x][pessoa.casa_y]
    print("Custo da operação : %s" % (busca_heuristica(mapa, origem, destino)))
    agente.x = pessoa.casa_x
    agente.y = pessoa.casa_y
    print("Encaminhada pessoa para casa encontra-se na localização(%d,%d)" % (agente.x, agente.y) + '\33[0:0m')
    mapa.mostrar_mapa()
    print("")
