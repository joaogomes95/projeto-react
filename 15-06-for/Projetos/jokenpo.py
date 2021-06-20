# Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha
# de quantidade de rodadas, se não finalize o programa.


from random import randint


# Neste if fiz com que os valores aleatórios gerados pelo randint fossem transformados em (PEDRA, PAPEL ou TESOURA)
computador = randint(0, 2)

if computador == 0:
    computador = "PEDRA"

elif computador == 1:
    computador = "PAPEL"

else:
    computador = "TESOURA"


# if selec == 'PEDRA':
#     selec == 1
# elif selec == 'PAPEL':
#     selec == 2
# elif selec == 'TESOURA':
#     selec == 3
