# 01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foio maior e o menor peso lidos.

"""maior = 200
menor = 0


for c in range(0, 5):
    peso = int(input('Digite seu peso: '))

    if peso < maior:
        maior = peso
    if peso > menor:
        menor = peso

print(f'o maior peso foi {menor} e o menor peso foi {maior}')"""

# 02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.

# tabuada = int(input('Digite o número que deseja a tabuada: '))

# for c in range(10):
#     print("%d x %d = %d" % (tabuada, c+1, tabuada*(c+1)))

# 03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# menor = 0
# maior = 0
# for c in range(7):
#     idade = int(input('Digite sua idade: '))

#     if idade < 18:
#         menor += 1
#     if idade > 18:
#         maior += 1
# print(f'{maior} já são maiores de idade,  e {menor} ainda são menores de idade!')

# 04 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados.

# par = 0
# qpar = 0

# for c in range(6):
#     num = int(input('Digite um número: '))

#     if num % 2 == 0:
#         par += num
#     if num % 2 == 0:
#         qpar += 1
# print(f'A soma dos números pares é: {par}! E a quantidade de números pares inseridos são: {qpar}')

"""#01 - Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
sem break)"""
# stop = 5
# n1 = int(input('Digite um valor: '))
# n2 = int(input('Digite o segundo valor: '))

# while stop == 5:
#     print("""
# Digite a opção desejada:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa)""")
#     opcao = int(input('Digite a opção desejada: '))
#     if opcao == 1:
#         stop = 0
#         print(f'{n1} + {n2} = {n1 + n2}')
#     elif opcao == 2:
#         stop = 0
#         print(f'{n1} * {n2} = {n1 * n2}')
#     elif opcao == 3:
#         stop = 0
#         if n1 > n2:
#             print(n1)
#         else:
#             print(n2)
#     elif opcao == 4:
#         n1 = int(input('Digite um valor: '))
#         n2 = int(input('Digite o segundo valor: '))
#     elif opcao == 5:
#         stop = 0
#         print('Você saiu do programa! ')

# 02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

idade = int(input('Digite sua idade: '))
sexo = str(input('Digite seu sexo[F/M]: ')).upper

while True:
    opcao = int(input('Digite 1 para continuar e 2 para sair: '))
    if opcao == 1:
        idade = int(input('Digite sua ideida: '))
        sexo = str(input('Digite seu sexo: ')).upper
    else:
        print('Você saiu do progama!')
    if idade > 18:
        idade += 1
        print(f'{idade} pessoas tem mais que 18 anos')
    if sexo == 'M':
        sexo = + 1
        print(f'{sexo} Homens foram cadastrados!')
    if sexo == 'F':
        idade < 20
        idade += 1
        print(f'São {idade} mulheres com menos de 20 anos! ')
    else:
        break
