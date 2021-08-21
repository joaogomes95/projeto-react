from classes.player import Player
class Hunter(Player):
    def __init__(self,part1="",part2="",part3="",part4="",part5="",part6="",choice1="",choice2="",choice3="",choice4="",choice5=""):
        part1 = """
            Máthius , é seu nome e você é um caçador de monstros .Neste
            momento acaba de acordar em meio a um prédio selado por 
            demônios onde as almas de vários inocentes jazem em agonia
            constante."""
        part2 = """
            Você se levanta e anda até a escadaria onde se depara com 
            um problema:existe um buraco em frente a escadaria.
            (O que você fará?)"""
        part3 = """
            você encontra uma arma feita com ossos de inocentes, neste
            momento o prédio entra em tremor, as almas antes em
            desespero entram em euforia. repentinamente o demonio 
            aparece em frente a porta da saída. 
            (O que voce faz?)"""
        part4 = """
            O demônio momentaneamente se abaixa por causa de seu golpe.
            Você percebe uma brecha: 
            (o que fará?)"""
        part5 = """
            O demônio desvia e te ataca se posicionando ao seu lado
            (o que fará?)"""
        part6 = """
            O demônio te acerta pelas costas e você morre!"""
        
        choice1 = "01- Procurar o demônio.\n02- Encontrar uma possivel arma.\n03- Encontrar uma saída.\n"
        choice2 = "01- Pular o buraco.\n02- Desistir e ir para o salão ao lado.\n03- Ir para o outro lado e entrar em uma sala de vigilancia.\n"
        choice3 = "01- Ataca o demônio.\n02- Da meia volta e corre.\n03- Tenta fugir passando pelo demônio.\n"
        choice4 = "01- corre e tenta passar pelo demônio.\n02- acerta outro golpe.\n03- da meia volta e se distancia.\n"
        choice5 = "01- corre para a porta a sua frente.\n02- tenta acertar outro golpe.\n03- se abaixa tentando evitar sua morte.\n"
        super().__init__(part1,part2,part3,part4,part5,part6,choice1,choice2,choice3,choice4,choice5)
    def __str__(self):
        return "Você escolheu viver a vida de um caçador:"
    def choices_History1(self,choice):
        try:
            int(choice)

            if choice == 1:
                choice = list()
                choice.extend(["",6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",2])
                return choice
            else:
                choice = list()
                choice.extend(["",3])
                return choice
        except:
            return self
    def choices_History2(self,choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["voce se prepara para pular e .. ",6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["o demonio aparece e ..",6])
                return choice
            else:
                choice = list()
                choice.extend(["",3])
                return choice
        except:
            return self
    def choices_History3(self,choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["",4])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",6])
                return choice
            else:
                choice = list()
                choice.extend(["",6])
                return choice
        except:
            return self
    def choices_History4(self,choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["",6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",5])
                return choice
            else:
                choice = list()
                choice.extend(["",6])
                return choice
        except:
            return self
    def choices_History5(self,choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["",6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",6])
                return choice
            else:
                choice = list()
                choice.extend(["",6])
                return choice
        except:
            return self
  
       
       
   