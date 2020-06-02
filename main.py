"""
Aplicação.

"""

from functions import *
from models import Mapa

frasco = 0   # começa com nenhum frasco de alcool gel

mapa = Mapa(matriz)

mapa.mostrar_mapa()

pessoas_aux = 0

pessoas = sort_pessoa(mapa)

lojas = sorteia_ponto_vendas(mapa)

qtde_pessoas = 0

agente = Agente(21, 25, mapa)


while pessoas_aux < 3:
    qtde_pessoas += 1

    print("Pessoa %s"%(qtde_pessoas))

    buscar_alcool(mapa, agente, lojas)
    mapa.reset_mapa(agente, lojas, pessoas)
    frasco +=1  # Agente compra um frasco na loja
    pessoa = pessoas.get()[1]
    busca_pessoa(mapa, agente, pessoa)
    mapa.reset_mapa(agente, lojas, pessoas)

    if agente.sucesso:
        mapa.mapa[pessoa.x][pessoa.y].tipo = "P"
        mapa.mapa[pessoa.casa_x][pessoa.casa_y].tipo = "C"
        acompanha_para_moradia(mapa, agente, pessoa)
        mapa.reset_mapa(agente, lojas, pessoas)
        pessoas_aux += 1
    else:
        frasco -= 1  # Diminui um frasco do agente
        print('O agente nao convenceu a pessoa a ir para casa, mas a pessoa aceitou o frasco de alcool gel')