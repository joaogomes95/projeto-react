from classes.player import Player
class Soldier(Player):
    def __init__(self,part1="",part2="",part3="",part4="",part5="",part6="",choice1="",choice2="",choice3="",choice4="",choice5=""):
        part1 = """
            Urizen é seu nome, um soldado solitário altamente
            treinado em cenários de guerra. Personagem  Propenso
            à violência por causa da tortura que sofreu na guerra. 
            Após ser capturado e sedado ele acorda em meio aos 
            escombros de uma base que foi atacada restando de pé 
            apenas prédio abandonado de onde vinham sons demoníacos.
           """
        part2 = """ 
            Imediatamente você se levanta escuta sons de
            uma revoada de centenas de morcegos e oberva 
            uma porta ao seu lado (O que você fará?)
            """
        part3 = """
            Imediatamente você lança mão em sua faca 
            pontiaguda, se aproxima de uma pequena porta lateral...
            ao empurrar essa porta a mesma emite um som intrigante....
            (O que você faz?)
            """
        part4 = """
            Você acerta e fere o demônio com seu golpe,
            mas não é suficiente para matá-lo.
            De repente você percebe uma saida: 
            (o que fará?)
           """
        part5 = """ 
            O demônio desvia e te ataca se posicionando
            ao seu lado.
            (o que fará?)
            """
        part6 = """O demônio te acerta pelas costas e você morre!
            """
        
        choice1 = "01- Procurar o demônio.\n02- Pegar a sua arma.\n03- Vai de encontro ao prédio abandonado.\n"
        choice2 = "01- Abrir a porta.\n02- Desistir e ir para o salão ao lado.\n03- Ir para o outro lado, em meio aos escombros.\n"
        choice3 = "01- Inicia um  ataque ao demônio.\n02- Recua e tenta se esconder .\n03- Tenta fugir passando pelo demônio.\n"
        choice4 = "01- Corre e tenta passar pelo demônio.\n02- acerta outro golpe.\n03- Espera e distancia.\n"
        choice5 = "01- corre para a porta a sua frente.\n02- tenta acertar outro golpe.\n03- se abaixa tentando evitar sua morte.\n"
        super().__init__(part1,part2,part3,part4,part5,part6,choice1,choice2,choice3,choice4,choice5)
    def __str__(self):
        return "valor incorreto"
    def choices_History1(self,choice):
        try:
            int(choice)

            if choice == 1:
                choice = list()
                choice.extend(["",2])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",3])
                return choice
            else:
                choice = list()
                choice.extend(["",2])
                return choice
        except:
            return self
    def choices_History2(self,choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["",3])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["Você acaba dando de frente com o demônio",4])
                return choice
            else:
                choice = list()
                choice.extend(["",6])
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
  
       
       
   