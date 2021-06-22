# dict()

# (tuplas) [Listas] {Dicionários}
# get = pegar = ele não retorna error se chave não existir. Ele retorna None
# None é um nulo
# getdefault

# values() = São os valroes do dicionário
# Keys = Acessa as chaves
# itens = acessa todos os itens do dicionário

# pessoas = dict()
# povo = list()

# for c in range(0, 3):
#     pessoas['nome'] = input('Digite um nome: ')
#     pessoas['idade'] = input('Digite a idade: ')
#     povo.append(pessoas.copy())
#     print(pessoas)

# for p in povo:
#     print(p['nome'])
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# aluno = dict()
# aluno['nome'] = str(input('Nome: '))
# aluno['media'] = float(input(f'Média do {aluno["nome"]} é: '))

# if aluno['media'] >= 7:
#     aluno['situacao'] = 'Aprovado'
# elif 5 >= aluno['media'] < 7:
#     aluno['situacao'] = 'Recuperacao'
# else:
#     aluno['situacao'] = 'Reprovado'

# for k, v in aluno.items():
#     k = k.title()
#     print(f'{k} é igual a {v}')
#
# 1.    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

pessoa = dict()
pessoa['nome'] = str(input('Digite seu nome: '))
pessoa['anonasc'] = int(input('Digite seu ano de nascimento: '))
pessoa['CTPS'] = float(input('Digite o número da sua carteira de trabalho: '))
pessoa['idade'] = int(input('Digite sua idade: '))

if pessoa['CTPS'] != 0:
    pessoa['anoc'] = int(input('digite seu ano de contratação: '))
    pessoa['anoc'] -= 2021 - 35
    print(f'Você vai se aposentar com {pessoa["anoc"]} de idade!')
