# Projeto 04 - Simulador de votação:
# Crie um programa que simule um sistema de votação, ele deve receber votos até
# que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
# duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições. ok
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):
# ● 1, 2 ou 3 - Votos para os respectivos candidatos
# ● 4- Voto Nulo
# ● 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# ● O total de votos para cada candidato;
# ● O total de votos nulos;
# ● O total de votos em branco;
# ● Qual candidato venceu a votação


import os  # Biblioteca importada para limpeza do código.
# Função sleep importada para pausar a exibição dos dados no console.
from time import sleep

# Neste bloco iremos fazer a verificação da idade da pessoa:


def autoriza_voto():
    # Usamos o today.year para pegar o ano e fazer o calculo da data de nascimento.
    from datetime import date
    ano = date.today().year
    nascimento = int(
        input('Digite o ano do seu nascimento informando os 4 digitos: '))
    idade = ano - nascimento

    if idade < 16:
        return F'Voto negado'
    elif 16 >= idade < 18 and idade > 70:
        return f'Voto Opcional'
    else:
        return f'Voto Obrigatório'

# Função que definirá se o usuário pode votar segundo sua idade,
# e caso não possa, iremos pedir uma data de nascimento válida.


def votacao(voto):
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    brancos = 0
    nulos = 0
    continuar = ''

    while True:
        while True:
            if autoriza_voto() == 'Voto negado':
                print('Você não pode votar, digite uma data de nascimento válida')
            else:
                break

        voto = int(input('''
        1 - Bozo
        2 - Luladão
        3 - Terceira Via (Mais aconcelhado)
        4 - Voto em Branco (Não aconcelhado)
        5 - NULO (Não faça isso)
        Digite a opção desejada: '''))
        # Neste bloco iremos fazer a contagem do votos.
        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        elif voto == 4:
            nulos += 1
        elif voto == 5:
            brancos += 1
        elif 1 < voto > 5:
            print('Opção Inválida!')

        continuar = input(
            'Deseja continuar a votação? [S/N]').upper().capitalize()[0]
        os.system("cls")
        if continuar == 'N':
            break
    os.system("cls")  # Limpeza do console.
    print('Computando Votos!')
    sleep(3)
    # Neste bloco iremos mostrar ao usuário os votos recebidos por cada candidato e também os votos brancos e nulos.
    print(f'''
    O Bozo recebeu {candidato1} voto(s)!
    Luladão recebeu {candidato2} voto(s)!
    A Terceira Via recebeu {candidato3} voto(s)!
    Tivemos {brancos} voto(s) em branco!
    Tivemos {nulos} voto(s) nulos!
    ''')
    sleep(2)
    # Aqui fazemos a validação de quem foi o candidato eleito. E caso não haja campeão iremos exibir no console.
    if candidato2 < candidato1 > candidato3:
        return f'O Bozo foi eleito e estamos lascados novamente!'
    elif candidato3 < candidato2 > candidato1:
        return f'O Luladão foi eleito e estamos lascados novamente!'
    elif candidato1 < candidato3 > candidato2:
        return f'A terceira via foi eleita, e agora talvez as coisas melhorem............'
    else:
        return f'Os candidatos não receberam votos suficientes para serem eleitos. '


# Chamando a função votação.
print(votacao(autoriza_voto))
