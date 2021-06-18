# 01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

# lista = []
# print('Digite 0 caso queira finalizar!')

# while True:
#     valor = int(input('Digite um número!: '))
#     if valor not in lista:
#         lista.append(valor)
#     if valor == 0:
#         print('Preenchimento finalizado: ')
#         break
# print(sorted(lista))

# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

# listap = []
# listai = []
# listat = []
# print('Digite 0 caso queira finalizar!')

# while True:
#     valor = int(input('Digite um número!: '))
#     if valor % 2 == 0:
#         listap.append(valor)
#     if valor % 2 != 0:
#         listai.append(valor)
#     if valor != 0:
#         listat.append(valor)
#     if valor == 0:
#         print('Preenchimento finalizado: ')
#         break
# listap.remove(0)
# print(
#     f'Os números pares são: {listap}. Os números impares são: {listai}. E todos os os números são: {listat}.')

# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import sample

mega = []
valor = int(input('Digite a quantidade de combinações: '))
for c in range(valor):

    combinacao = sample(range(1, 60), 6)
    mega.append(combinacao)

for a in range(valor):
    print(f'{a+1}º jogo: {mega[a]}')
