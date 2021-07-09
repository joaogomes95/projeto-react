from classes.player import Player
class Nephilim(Player):
    def __init__(self,part1="",part2="",part3="",part4="",part5="",part6="",choice1="",choice2="",choice3="",choice4="",choice5=""):
        part1 = """
            Zeican é o seu nome, filho de um nephilim com uma humana, 
            nascido sem poderes, e ensinado ao longo das gerações pelo 
            seu tio a nutrir um ódio mortal por tudo que é sobrenatural. 
            Depois de estar desmaiado você acorda em um hospital no centro 
            da cidade, onde escuta as almas inocentes gritando por socorro.
           """
        part2 = """
            Você passou para o corredor do hospital e começou a gritar 
            (tem alguém ai, onde estou?), involuntariamente você acabou 
            chamando a atenção do demonio. O que você fará?
            """
        part3 = """
            Você abriu a porta e viu um corpo jogado no chão, destrossado.
            Ao chegar perto viu que era um policial e correu para encontrar
            a arma dele, uma pistola.  Ao pegar a arma e virar, você percebe
             que o demonio está atrás de você. (Qual sua reação?).
            """
        part4 = """
            Graças ao seu tirona cara do demonio ele se afasta 2 passos para
             trás: (o que fará)
           """
        part5 = """
            O demonio continuou recuando após seus tiros, porém sua arma 
            descarregou: (o que fará)
            """
        part6 = """
            O demonio acertou um golpe em você, você não resistiu. 
              YOU´RE DEAD!!!
            """
        
        choice1 = "01 procurar uma saida\n 02 Procurar um sobrevivente.\n03 chamar por seu pai."
        choice2 = "01 Sem reação\n 02 Pegar o extintor e tentar atacar o demonio \n 03  ir para o outro lado e entrar em uma sala de vigilancia   "
        choice3 = "1 corre de volta para a porta\n 2 acerta o tiro \n 3 tenta se afastar "
        choice4 = "1 corre de volta para a porta\n 2 Continua atirando \n 3 Tenta se afastar "
        choice5 = "1 corre de volta para a porta \n 3 tenta procurar mais munição \n 3 Tenta se afastar "
        super().__init__(part1,part2,part3,part4,part5,part6,choice1,choice2,choice3,choice4,choice5)
    def __str__(self):
        return "Você escolheu viver a vida de um Nephilim:"
    def choices_History1(self,choice):
        try:
            int(choice)

            if choice == 1:
                choice = list()
                choice.extend(["Você fez muito barulho...",6])
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
                choice.extend(["Você fez muito barulho...",6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",6])
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
  