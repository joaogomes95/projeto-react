# Funções
# Como boas práticas fazer as funções antes de iniciar a escrever o código
# Escopo: espaço(dentro) da nossa função
# def '' seria definr uma função
# 1. (    )
# 2. (**)
# 3. (*) (/) (//) (%)
# 4. (+) (-)

# def soma():
#     soma = 2 + 3
#     print(soma)


# soma()
# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

# def voto(ano):
#     from datetime import date
#     atual = date.today().year
#     idade = atual - ano
#     if idade < 16:
#         return f'com {idade} anos o voto é NEGADO'
#     elif 16 <= idade < 18 or idade >= 70:
#         return f'Com a {idade} anos o voto é OPCIONAL'
#     else:
#         return f'Com {idade} anos voto é OBRIGATÓRIO'


# nasc = int(input('Digite seu ano de nascimento: '))
# print(voto(nasc))

# Faça um programa, com uma função que necessite de um parametro.
# A função retorna o valor de caractere ‘P’, se seu parametro for positivo, e ‘N’, se seu parametro for zero ou negativo.

# def verificar(n1):
#     if n1 <= 0:
#         return f'N'
#     else:
#         return f'P'


# numero = float(input('Digite um número: '))
# print(verificar(numero))
# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.

def somar(n1, n2, n3):
    res = n1+n2+n3
    return res


def media(soma):
    med = soma / 3
    return f'A média é {med:.2f}'


def menu():
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    print(media(somar(nota1, nota2, nota3)))


menu()
