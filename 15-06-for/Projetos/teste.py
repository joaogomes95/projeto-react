from random import randint

rodadas = 0
pontos_jogador = 0
pontos_computador = 0
empates = 0

while True:
    rodadas += 1

    print("Rodada {}".format(rodadas))

    jogada_usuario = input(
        "Digite a sua jogada (Pedra, Papel ou Tesoura) ou 'sair' para sair do jogo: ").lower()

    if (jogada_usuario == "pedra" or
        jogada_usuario == "papel" or
            jogada_usuario == "tesoura"):

        print("Você jogou {}.".format(jogada_usuario))

        jogada_computador = randint(0, 2)

        if jogada_computador == 0:
            jogada_computador = "pedra"
        elif jogada_computador == 1:
            jogada_computador = "papel"
        else:
            jogada_computador = "tesoura"

        print("Computador jogou {}.".format(jogada_computador))

        vitoria = False
        empate = False

        if jogada_usuario == "pedra":
            if jogada_computador == "tesoura":
                print("Pedra quebra Tesoura.")
                vitoria = True
            elif jogada_computador == "papel":
                print("Papel embrulha Pedra.")
            else:
                print("Nada acontece.")
                empate = True
        elif jogada_usuario == "papel":
            if jogada_computador == "pedra":
                print("Papel embrulha Pedra.")
                vitoria = True
            elif jogada_computador == "tesoura":
                print("Pedra quebra Tesoura.")
            else:
                print("Nada acontece.")
                empate = True
        elif jogada_usuario == "tesoura":
            if jogada_computador == "papel":
                print("Tesoura corta Papel.")
                vitoria = True
            elif jogada_computador == "pedra":
                print("Pedra quebra Tesoura.")
            else:
                print("Nada acontece.")
                empate = True

        if empate:
            print("Rodada terminou em empate.")
            empates += 1
        elif vitoria:
            print("Você venceu a rodada.")
            pontos_jogador += 1
        else:
            print("Você perdeu a rodada.")
            pontos_computador += 1

        print("Rodada {} finalizada.".format(rodadas))
    elif jogada_usuario == "sair":
        break
    else:
        print("Insira uma jogada válida.")
        rodadas -= 1
    print()


print("Placar do Jogo:")
print("Pontos do Jogador: {}".format(pontos_jogador))
print("Pontos do Computador: {}".format(pontos_computador))
print("Empates: {}".format(empates))

if pontos_jogador > pontos_computador:
    print("Você venceu.")
elif pontos_computador > pontos_jogador:
    print("Você perdeu.")
else:
    print("O jogo terminou em empate.")
