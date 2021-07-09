from classes.player import Player


class Mercenary(Player):
    def __init__(self, part1="", part2="", part3="", part4="", part5="", part6="", choice1="", choice2="", choice3="", choice4="", choice5=""):
        part1 = """
            Brandon é um mercenário e tem como objetivo, encontrar uma 
            espada muito valiósa feita por ossos de inocentes. O prédio 
            onde a espada se encontra está a 500 metros de sua localização 
            porém sua casa está rodeada de demônios.
            o que deseja fazer:
           """
        part2 = """
            Após abrir a porta com a água benta em mãos Brandon se 
            vê rodeado por Dêmonios.
            o que deseja fazer:
            """
        part3 = """
            Após entrar no carro, você precisa correr até o prédio pois 
            o ele está sendo cercado por demônios e não te resta muita 
            água benta.
            o que deseja fazer:
            """
        part4 = """
            Brandon vê que sua gasolina chegou ao fim e está a 15 metrôs do 
            prédio e tem apenas um pouco de água benta em mãos que.
           o que deseja fazer:
           """
        part5 = """
            Brandon entra no prédio e da de cara com um demônio enorme e logo 
            atrás dele está a espada. Ele se vê entre a vida e a morte pois 
            atrás dele está a porta e atrás dela os demônios estão tentando entrar. 
            o que deseja fazer:
            """
        part6 = """Você está morto
            """

        choice1 = "01- Ir correndo até o prédio.\n02- Pegar água benta antes de sair.\n03- Entrar em seu carro e ir até o prédio .\n"
        choice2 = "01- Usar água benta e correr até o prédio.\n02- Tentar lutar com todos os demônios.\n03- Correr até o carro utilizando apenas um pouco de sua água benta.\n"
        choice3 = "01- Usar o restante de água benta que te sobra e tentar limpar o caminho para chegar no prédio.\n02- Enfrentar os demônios e guardar o pouco de água benta que te sobra.\n03- Acelerar a tentar passar por cima de todos os demônios.\n"
        choice4 = "01- Utilizar o pouco de água benta que te sobra para abrir caminho e chegar até a porta do prédio onde a espada está localizada.\n02- Tentar chegar até porta sem usar a água benta, pois dentro do prédio pode haver demônios.\n03- - Ficar no carro esperando que os demônios se destraiam até que você possa sair.\n"
        choice5 = "01- Tenta passar pelo demônio e tentar pegar a espada para se defender.\n02- Tentar ferir o demônio e pegar a espada.\n03- Tenta sair do prédio e voltar para o carro.\n"
        super().__init__(part1, part2, part3, part4, part5,part6, choice1, choice2, choice3, choice4, choice5)

    def __str__(self):
        return ""

    def choices_History1(self, choice):
        try:
            int(choice)

            if choice == 1:
                choice = list()
                choice.extend(["Brandom tem sua cabeça dilacerada pelos demônios!", 6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["", 2])
                return choice
            else:
                choice = list()
                choice.extend(["", 3])
                return choice
        except:
            return self

    def choices_History2(self, choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["Após se livrar da primeira leva de demônios ele acaba levando um \ngolpe fatal em seu peito por um demônio que não havia sido acertado \npelo água benta.", 6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["Após deferir alguns golpes, um demonio acerta sua cabeça e ele morre.", 6])
                return choice
            else:
                choice = list()
                choice.extend(["", 3])
                return choice
        except:
            return self

    def choices_History3(self, choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["", 4])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["A água benta que usou não foi suficiente para matar todos os demônios.", 6])
                return choice
            else:
                choice = list()
                choice.extend(["O carro não consegue passar pelos demônios e ele acaba tendo que sair, \nele é atingido por diversos golpes e morre lentamente.", 6])
                return choice
        except:
            return self

    def choices_History4(self, choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["", 5])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["Tem seu corpo consumido rapidamente pelos demônios.", 6])
                return choice
            else:
                choice = list()
                choice.extend(["O carro é invadido pelos demônios e sua morte é dolorosa de sofrida.", 6])
                return choice
        except:
            return self

    def choices_History5(self, choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["O demonio retirar o coração de Brandon rapidamente.", 6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["O demônio é muito mais forte que Brandon e arraca todos os seus orgãos.", 6])
                return choice
            else:
                choice = list()
                choice.extend(["Brandon é cercado pelos demônios e morre tetando fugir.", 6])
                return choice
        except:
            return self

