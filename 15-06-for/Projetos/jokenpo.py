from random import randint


pjogador = 0
pcomputador = 0
jogada = ['Pedra', 'Papel', 'Tesoura']
empate = 0

while True:

    rodadas = int(input('Digite quantas rodadas você quer jogar: '))
    for c in range(1, rodadas+1):
        computador = randint(0, 2)
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print("""
        Suas opções são:
        [0] Pedra
        [1] Papel
        [2] Tesoura                    
                    """)
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        jogador = int(input('Digite a opção selecionada: '))
        print(f'o jogador escolheu {jogada[jogador]}')
        print(f'O computador escolheu: {jogada[computador]}')
        if computador == 0:  # Preda
            if jogador == 1:
                pjogador += 1
                print('Você ganhou')
            elif jogador == 0:
                empate += 1
                print('Você empatou')
            elif jogador == 2:
                pcomputador += 1
                print('Você perdeu esta rodada!')

        elif computador == 1:  # papel
            if jogador == 2:
                pjogador += 1
                print('Você ganhou')
            elif jogador == 1:
                empate += 1
                print('Você empatou')
            elif jogador == 0:
                pcomputador += 1
                print('Você perdeu esta rodada!')

        elif computador == 2:  # tesoura
            if jogador == 0:
                pjogador += 1
                print('Você ganhou')
            elif jogador == 2:
                empate += 1
                print('Você empatou')
            elif jogador == 1:
                pcomputador += 1
                print('Você perdeu esta rodada!')

    continuar = input('Deseja continuar? [S/N]: ').upper()
    if continuar != "S":
        break


print("Placar do Jogo:")
print(f'Pontos do Jogador: {pjogador}')
print(f'Pontos do Computador: {pcomputador}')
print(f'Empates: {empate}.')

if pjogador > pcomputador:
    print("Você venceu.")
elif pcomputador > pjogador:
    print("Você perdeu.")
else:
    print("O jogo terminou em empate.")
