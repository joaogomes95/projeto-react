# Exercicios:

# #01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:

# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ]

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# #02 - Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna.
#    C) O maior valor da segunda linha.


vmatriz = list()

for c in range(3):
    matriz = list()
    matriz.append(input('Digite o primeiro número: '))
    matriz.append(input('Digite o segundo número: '))
    matriz.append(input('Digite o terceiro número: '))
    vmatriz.append(matriz[:])
    if vmatriz % 2 == 0:
        print(vmatriz)

print(f'{vmatriz[c-2]}\n{vmatriz[c-1]}\n{vmatriz[c]}')

#     print(f'{a+1}º jogo: {mega[a]}')
