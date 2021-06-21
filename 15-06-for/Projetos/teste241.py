from random import randint

jogada_jogador = str(
    input('Digite sua opção(Papel, pedra ou tesoura): '))

rodadas = 0
vitoria = 0
vitoria_maquina = 0
empate = 0

while True:
    rodadas += 1

    print(rodadas)
    if (jogada_jogador == "pedra" or jogada_jogador == "papel" or jogada_jogador == "tesoura"):
        print(f'Você escolheu: {jogada_jogador}')

        # Neste neste bloco fiz com que os valores aleatórios gerados pelo randint fossem transformados em (PEDRA, PAPEL ou TESOURA) e no final exibimos o que o computudor escolheu.

        computador = randint(0, 2)

        if computador == 0:
            computador = "pedra"

        elif computador == 1:
            computador = "papel"

        else:
            computador = "tesoura"

        print(f'O computador escolheu {computador}')

        vitoria = False
        empate = False
        # Papel
        if jogada_jogador == "papel":
            if computador == "pedra":
                print('Papel sufoca pedra')
                vitoria = True
            elif computador == "tesoura":
                print('Você foi cortado')
            else:
                print('Você foi empatado')
                empate = True
        # Pedra
        elif jogada_jogador == "pedra":
            if computador == "tesoura":
                print('Você foi quebrado')
                vitoria = True
            elif computador == "papel":
                print('Você foi embrulhado')
            else:
                print('Você foi empatado')
                empate = True
        # Tesoura
        elif jogada_jogador == "tesoura":
            if computador == "papel":
                print('Você foi picotado')
                vitoria = True
            elif computador == "pedra":
                print('Te quebrei!')
            else:
                print('Você foi empatado')
                empate = True

        if empate:
            print('Rolou um empate')
            empate += 1
        elif vitoria:
            print('Boa, você ganhou')
            vitoria += 1
        else:
            print('Moio, a máquina ganhou')
            vitoria_maquina += 1

        print('Chegamos ao fim!')
    elif jogada_jogador == "Sair":
        print('Você saiu do jogo!')
        break
    else:
        print('Jogada inválida! Jogue novamente')
        rodadas -= 1
    print()
print("Placar do Jogo:")
print(f'jogador ganho {vitoria} rodadas! ')
print(f'O computador ganhou {vitoria_maquina} vezes!')
print(f'O empate aconteceu em {empate} vezes')

if jogada_jogador > computador:
    print(f'Você ganhou')
elif computador > jogada_jogador:
    print('Você perdeu')
else:
    print('O jogo empatou')
