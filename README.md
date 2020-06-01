Busca Heurística
===============================================

## Autores

  | [<img src="https://avatars1.githubusercontent.com/u/46221221?s=460&u=0d161e390cdad66e925f3d52cece6c3e65a23eb2&v=4" width=115><br><sub>Jackson Magnabosco</sub>](https://github.com/jacksonn455) | [<img src="https://scontent.ferm2-1.fna.fbcdn.net/v/t1.0-1/p160x160/22491625_1445244322239553_4539298653893602379_n.jpg?_nc_cat=108&_nc_sid=dbb9e7&_nc_ohc=UtKMf_FuUb4AX8yje8o&_nc_ht=scontent.ferm2-1.fna&_nc_tp=6&oh=bbda905374f89388b3bbb13e40636e22&oe=5EFBFB89" width=115><br><sub>Alvaro Costa</sub>](https://pt-br.facebook.com/alvaroluis.costa) |
  | :---: | :---: |
--------------------

- Com a pandemia do Covid-19, a tarefa mais difícil está em convencer as pessoas a ficarem em casa,
especialmente se elas não possuírem álcool gel. A fim de evitar um número maior de pessoas na rua,
você se prontificou a ajudar, entregando álcool gel e convencendo 3 pessoas na rua a ir para casa.

- No entanto, nem todas as pessoas se convencem da importância de ficar em casa e, não importa o
quanto você tente convencê-la, ela não irá aceitar sua ajuda. Só que, mesmo não aceitando sua
ajuda, ela aceitou o álcool gel que você a entregou e não irá devolver.

- Para essa tarefa, você não poderá carregar mais de um álcool gel por vez, nem levar mais de uma
pessoa por vez para casa. Para facilitar sua tarefa, você irá conhecer de antemão a localização de
todos os pontos de venda que ainda possuem álcool gel, e de todas as pessoas no cenário.

- Portanto, o Trabalho consiste em implementar um agente capaz de locomover-se pela cidade, buscar
o álcool gel, dirigir-se até as pessoas, e levá-las para casa (caso aceitem). Para isso, você deve utilizar
o algoritmo de busca heurística A*.

- O agente deve ser capaz de calcular automaticamente a melhor rota até um ponto de venda, pessoa,
e casa da pessoa.

- O mapa da região é mostrado na figura a seguir

--------------------
 ![](https://github.com/jacksonn455/busca-heuristica/blob/master/img.png)
--------------------

- O mapa é formado por 5 tipos de terrenos: asfalto (região cinza escuro), paralelepípedo (região cinza
claro), edifício (região laranja), grama (região verde) e terra (região marrom).
Os custos para passar por cada tipo de terreno são os seguintes:

- Asfalto: +1
- Paralelepípedo: +3
- Terra: +6
- Grama: +10

- Você nunca pode passar por região de edifício (região laranja).
- Você inicia sua jornada do ponto vermelho (posição [21, 25] no mapa), e termina após convencer e
- levar 3 pessoas até suas casas. A melhor rota para cumprir essa missão é a rota de menor custo
levando em consideração o terreno.
--------------------

Informações adicionais
=======================

- O mapa deve ser representado por uma matriz 42 x 42 (igual à mostrada na Figura).
- O agente sempre inicia no ponto vermelho do mapa
- O agente não pode andar na diagonal, somente na vertical e na horizontal.
- O programa deve sortear as posições dos locais de venda de álcool gel, das pessoas e de suas
residências (nenhuma pode estar em um ponto laranja, nem no mesmo lugar de outra
pessoa/ponto de venda).
- Serão 3 pontos de venda de álcool gel (assuma que o estoque é infinito). Você também deve
sortear o local de 6 pessoas, sendo que apenas 3 dessas aceitarão sua ajuda (o programa não
pode saber quais aceitarão).
- Para tentar convencer uma pessoa, você precisa, obrigatoriamente, estar com álcool gel.
Antes de tentar convencer uma pessoa, você deve entregar o álcool gel a ela.
- Após convencer a pessoa, ela lhe dará a posição de sua casa (gerada aleatoriamente), e você
deverá levá-la até lá.
- As pessoas podem ser convencidas em qualquer ordem. Porém, ordens diferentes vão
resultar em custos totais diferentes. Além disso, este é um problema não-determinístico,
onde não é possível prever se a pessoa vai ser convencida ou não.
- Devem existir somente 3 pessoas que irão ser convencidas. As indicações de quais pessoas
vão aceitar devem ser sorteadas na inicialização do programa, porém o programa não pode
ter acesso a essa informação durante o processo de busca.
- Deve existir uma maneira de visualizar os movimentos do agente, mesmo que a interface
seja bem simples. Podendo até mesmo ser uma matriz desenhada e atualizada no console.
- O mapa deve ser configurável, ou seja, deve ser possível modificar o tipo de terreno em cada
local. O mapa pode ser lido de um arquivo de texto ou deve ser facilmente editável no código.
- O programa deve exibir o custo do caminho percorrido pelo agente enquanto ele se
movimenta pelo mapa e também o custo final ao terminar a execução.
- O programa pode ser implementado em qualquer linguagem.
- O trabalho pode ser feito individualmente ou em duplas.
- O programa deve ser apresentado durante a aula por todos os membros do grupo. Se algum
dos membros do grupo não comparecer ou não souber explicar nada sobre a implementação
receberá nota zero.
--------------------

Dicas:
=======================

- Como o agente não sabe quais pessoas irão ser convencidas, assuma que, no pior caso,
vai ter que encontrar com todas as pessoas.
- Implemente a função de busca de uma forma genérica, pois será necessário executá-la
múltiplas vezes para diferentes destinos.
