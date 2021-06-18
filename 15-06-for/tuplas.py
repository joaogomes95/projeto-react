# Tuplas (), Listas []
# A diferença entre eles
# sorted = ordenar em ordem alfabética e alfanuméricamente
# Em lista a função em .append() adiociona valor no final da lista
# o .insert altera um valor por outro
# .pop() apaga o ultimo valor
# .remove() apaga o valor selecionado


# Exercícios Tuplas:
# 01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições.
# Dica: utilizar a biblioteca random do Python.

# from random import randint

# ale = (randint(1, 50), randint(1, 50), randint(
#     1, 50), randint(1, 50), randint(1, 50))

# print(sorted(ale))
# print(max(ale))
# print(min(ale))

# 02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.

# a1 = int(input('Digite um valor: '))

# tupla1 = a1.count(9)
# tupla2 = a1.count(3)

# print(f'O número apareceu {tupla1} vezes e o número 3 apareceu {tupla2} vezes!')

# 01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

# lista = [5, 7, 2, 9, 4, 1, 3]
# lista.sort(reverse=True)
# print(sorted(lista))
# print(lista)
# print(max(lista))
# print(min(lista))
# print(sum(lista))
# print(len(lista))

# Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".
