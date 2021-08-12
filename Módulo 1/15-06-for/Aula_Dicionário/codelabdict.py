# 1 - Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6,
# 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes
# aos quadrados desses números.
# {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}

# lista = dict()

# for c in range(1, 10):
#     if c == 2 or c == 3 or c == 8:
#         continue
#     lista[c] = c ** 2
# print(lista)

# 2 - Crie um dicionário em que suas chaves correspondem a números
# inteiros entre [1, 10] e cada valor associado é o número ao quadrado.
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# numero = dict()

# for c in range(1, 11):
#     numero[c] = c**2
# print(numero)

# 3 - Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado.

# lista = dict()
# lista['nome'] = input('Digite seu nome: ')
# lista['nota'] = float(input('Digite sua nota: '))

# if lista['nota'] >= 7:
#     print(
#         f'A nota do aluno {lista["nome"]} foi {lista["nota"]} e ele foi aprovado!')
# elif lista['nota'] >= 5 < 7:
#     print(
#         f'A nota do aluno {lista["nome"]} foi {lista["nota"]} e ele esta de recuperação!')
# elif lista['nota'] <= 5:
#     print(
#         f'A nota do aluno {lista["nome"]} foi {lista["nota"]} e ele foi reprovado!')

# 4-    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
# anoatual = 2021
# pessoa = dict()
# pessoa['nome'] = str(input('Digite seu nome: '))
# pessoa['anonasc'] = int(input('Digite seu ano de nascimento: '))
# pessoa['CTPS'] = float(input('Digite o número da sua carteira de trabalho: '))
# pessoa['idade'] = int(input('Digite sua idade: '))

# if pessoa['CTPS'] != 0:
#     pessoa['anoc'] = int(input('digite seu ano de contratação: '))
#     pessoa['anoc'] += 35 - pessoa['anonasc']
#     print(f'Você vai se aposentar com {pessoa["anoc"]} de idade!')
# else:
# print('Você ainda não iniciou sua carreira!')

# else:
# print('Você ainda não iniciou sua carreira!')

# 5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não

povo = list()

pessoa = dict()
povo = list()
pessoa['nome'] = input('Digite seu nome: ')
pessoa['SexoBiologico'] = input('Digite seu sexo biológico [F/M]: ')
pessoa['idade'] = int(input('Digite sua idade: '))
