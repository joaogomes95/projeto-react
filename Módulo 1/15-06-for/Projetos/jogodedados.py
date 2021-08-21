
from random import randint
from operator import itemgetter
from time import sleep
# Aqui definifimos brevemente as vitórias de cada jogador como 0, para mais abaixo acrescentar as vitórias dependendo do resultado da partida.
vitoria_player1 = 0
vitoria_player2 = 0
vitoria_player3 = 0
vitoria_player4 = 0
resultado = list()
# Aqui iremos solicitar ao usuário quantas rodadas ele deseja realizar.
rodadas = int(input('Digite quantas rodadas deseja realizar: '))

# Este for servirá para que o programa faça a validação de quantas rodadas o usuário solicitou.
for c in range(0, rodadas):
    print(f'Os valores sorteados na {c+1}º rodada foram: ')
    # Neste bloco fizemos com que os jogadores gerem resultados aleatórios utilizando o randint.
    jogadas = {'jogador1': randint(1, 6), 'jogador2': randint(
        1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6), }
    print('-='*30)
    # Neste bloco utilizamos o for pegando os dados da key e do value para apresentar os valores tirados pelos dados.
    for k, v in jogadas.items():
        print(f'{k} tirou {v} no dado \U0001f3b2')
        sleep(1)
        print()
    # No enunciado do projeto pede que os resultados dos dados sejam ordenados, e para fazer isto utilizaremos o comando itemgetter da biblioteca 'operator'.
    resultado = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
    print()
    print('     == Classificação da Rodada == ')
    print()
    sleep(1)

    for i, v in enumerate(resultado):

        print(f'    {i+1}º lugar foi o jogador: {v[0]} com {v[1]}.')
        print()
        sleep(1)

    # Neste bloco iremos atribuir os valores de vitórias e tembém contabilizar os empates das rodadas.
    if (jogadas['jogador3'] < jogadas['jogador1'] > jogadas['jogador2']) and jogadas['jogador1'] > jogadas['jogador4']:
        vitoria_player1 += 1
    elif (jogadas['jogador3'] < jogadas['jogador2'] > jogadas['jogador1']) and jogadas['jogador2'] > jogadas['jogador4']:
        vitoria_player2 += 1
    elif (jogadas['jogador2'] < jogadas['jogador3'] > jogadas['jogador1']) and jogadas['jogador3'] > jogadas['jogador4']:
        vitoria_player3 += 1
    elif (jogadas['jogador3'] < jogadas['jogador4'] > jogadas['jogador2']) and jogadas['jogador4'] > jogadas['jogador1']:
        vitoria_player4 += 1
    empates = rodadas - (vitoria_player1 + vitoria_player2 +
                         vitoria_player3 + vitoria_player4)
# Neste bloco após colher as informações de vitórias das rodadas podemos definir quem será o campeão ou se houve empate.
if (vitoria_player2 < vitoria_player1 > vitoria_player3) and vitoria_player1 > vitoria_player4:
    print(
        f'Parabéns jogador 1, você ganhou as rodadas com {vitoria_player1} vitórias \U0001F44F')
elif (vitoria_player3 < vitoria_player2 > vitoria_player1) and vitoria_player2 > vitoria_player4:
    print(
        f'Parabéns jogador 2, você ganhou as rodadas com {vitoria_player2} vitórias \U0001F44F')
elif (vitoria_player2 < vitoria_player3 > vitoria_player1) and vitoria_player3 > vitoria_player4:
    print(
        f'Parabéns jogador 3, você ganhou as rodadas com {vitoria_player3} vitórias \U0001F44F')
elif (vitoria_player2 < vitoria_player4 > vitoria_player1) and vitoria_player4 > vitoria_player3:
    print(
        f'Parabéns jogador 4, você ganhou as rodadas com {vitoria_player4} vitórias \U0001F44F')
else:
    print('Tivemos um EMPATE')
# Aqui mostramos quantas rodadas foram solicitadas pelo usuário.
print(f'foram jogadas {rodadas} rodadas')
print('-='*40)
# Neste print mostramos ao usuário quantas vitórias cada jogador teve, e apresentamos o resultado de empate caso ele ocorra.
print(f'''
O jogador 1 ganhou: {vitoria_player1} vezes!
O jogador 2 ganhou: {vitoria_player2} vezes!
O jogador 3 ganhou: {vitoria_player3} vezes!
O jogador 4 ganhou: {vitoria_player4} vezes!
O jogo empatou {empates} vezes!
''')
