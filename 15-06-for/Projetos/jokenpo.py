# Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha
# de quantidade de rodadas, se não finalize o programa.


from random import randint

rodadas = 0
jogada_jogador = 0
vitoria = 0
vitoria_computador = 0
empate = 0
while True:
    # Neste bloco vamos iniciar o as solicitações de rodadas e escolha do jogador.
    rodadas = input('Digite o número de rodadas que você deseja realizar: ')
    print(f'Você irá jogar {rodadas} rodadas contra o computador')
    # Neste bloco solicitamos que o jogador escolha entre as opções (PEDRA, PAPEL ou TESOURA) e vamos exibir a opção escolhida.

    jogada_jogador = str(
        input('Digite sua opção(Papel, pedra ou tesoura): ')).upper

    if jogada_jogador == "PEDRA":
        print(f'Você escolheu: {jogada_jogador}')
    if jogada_jogador == "PEPEL":
        print(f'Você escolheu: {jogada_jogador} ')
    if jogada_jogador == "TESOURA":
        print(f'Você escolheu: {jogada_jogador} ')

# Neste neste bloco fiz com que os valores aleatórios gerados pelo randint fossem transformados em (PEDRA, PAPEL ou TESOURA) e no final exibimos o que o computudor escolheu.

        computador = randint(0, 2)

        if computador == 0:
            computador = "PEDRA"

        elif computador == 1:
            computador = "PAPEL"

        else:
            computador = "TESOURA"
        print(f'O computador escolheu {computador}')
        # Aqui defini que vitoria, derrota(Será nossos pontos do computador) e empate são FALSE, e quando for adicionado TRUE iremnos adicionar os pontos.
        vitoria = False
        empate = False
        vitoria_computador = False
        if jogada_jogador == "PAPEL":
            if computador == "PEDRA":
                vitoria = True
            # PAPEL
            elif jogada_jogador == "PAPEL":
                if computador == "PEPEL":
                    empate = True

            elif jogada_jogador == "PAPEL":
                if computador == "TESOURA":
                    vitoria_computador = True
            # PEDRA
        elif jogada_jogador == "PEDRA":
            if computador == "TESOURA":
                vitoria = True

            elif jogada_jogador == "PEDRA":
                if computador == "PEDRA":
                    empate = True

            elif jogada_jogador == "PEDRA":
                if computador == "PAPEL":
                    vitoria_computador = True
            # TESOURA
        elif jogada_jogador == "TESOURA":
            if computador == "PAPEL":
                vitoria = True

            elif jogada_jogador == "TESOURA":
                if computador == "TESOURA":
                    empate = True

            elif jogada_jogador == "TESOURA":
                if computador == "PEDRA":
                    vitoria_computador = True
