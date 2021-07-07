from serie import Serie
from filme import Filme

# filme = Filme('Guerra do Amanhã', 2021, 160)
# serie = Serie('Young Sheldon', 2017, 3)
catalogo = list()
while True:

    cadastro = input(
        'O que você quer cadastrar?: Filme/Serie').strip().upper()[0]
    while cadastro not in 'FS':
        cadastro = input(
            'O que você quer cadastrar?: Filme/Serie').strip().upper()[0]

    if cadastro == 'F':
        filme = Filme(
            input('Nome: '),
            int(input('Ano: ')),
            int(input('Duração: '))
        )
        catalogo.append(filme)
    elif cadastro == 'S':
        serie = Serie(
            input('Nome: '),
            int(input('Ano: ')),
            int(input('Duração: '))
        )
    catalogo.append(serie)
    continua = input('Você quer continuar: [S/N]')
    while continua not in 'SN':
        continua = input('Digite S ou N: ')

    if continua == 'N':
        break

for i in catalogo:
    print(i)
    like = input('Você quer dar o like nesse item? [S/N] ').strip().upper()[0]
    while continua not in 'SN':
        like = input(
            'Você quer dar o like nesse item? [S/N] ').strip().upper()[0]

    if like == 'S':
        i.dar_like()
        print('Você curtiu esse conteúdo')

    else:
        print('Ok!')


for i in catalogo:
    print(i)
