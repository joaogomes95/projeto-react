# 01 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

# senha = '147852369'

# while senha != 147852369:
#     senha = int(input('Digite sua senha númerica: '))

#     if senha == 147852369:
#         print('Você digitou a senha correta')
#     else:
#         print('Tente novamente')


sexo = ''
sexo = str(input('Digite seu sexo biológico: ')).upper().strip()

while sexo not in 'MF':
    sexo = str(input('Digite seu sexo biológico novamente: ')).upper().strip()
print(f'Seu sexo é {sexo}')
