from classes.player import Player
class Ghost(Player):
    def __init__(self,part1="",part2="",part3="",part4="",part5="",part6="",choice1="",choice2="",choice3="",choice4="",choice5=""):
        part1 = """
            A História de Jamie e Liza.
            Liza é uma mulher de 37 anos e médica, está em missão missionária
            á quase um ano na guerra entre os paises de Tadjiquistão e Quirguistão, 
            e está á procura de seu filho Jamie, desaparecido á dois meses, nas 
            suas buscam pelo Jamie ela descobriu uma pista de seu filho, em um 
            ‘predio’ no centro do estopim da guerra, então ela vai rapidamente até 
            o predio e entra sem pensar duas vezes, na procura de seu amado filho.
            
            Seu nome é Jamie, você é um fantasma que foi morto pelo demônio que ronda
            o predio, sua alma e muitas outras almas de inocentes estava em constante
            agonia, e jamais teria paz, quando você sente a presença de sua amada mãe 
            Liza ao entrar no predio a sua procura e sente medo pela mãe, pode acabar
            sendo morta pelo demônio.

            O que você faz?

           """
        part2 = """
        
            Você acaba encontrando sua mãe subindo as escadas, perto de você tem uma 
            cadeira de madeira velha com teias de aranhas em cima, logo em seguida você
            começa a sentir a presença do demônio. Então você pensa: “ele deve está bem
            perto, pra eu conseguir senti-lo”.

            O que você faz?

            """
        part3 = """
            Sua mãe não conseguiu te notar, você entra em desespero por vê-la e não 
            consegui tocá-la, abraça-lá, ou ao menos “dizer” adeus. Você então pensa em
            desistir, e ouve sua mãe chamar por você, e logo tem uma lembrança de sua
            mãe que ao longo de sua vida sempre fez o máximo dela pra te fazer feliz,
            e no presente ela esteve ajudando á dezenas de pessoas na guerra. Então você 
            continua tentando chamar á atenção de sua mãe, mas sem sucesso,
            quando...

            Você e sua doce mãe escutam um barulho vindo do sótão, sua mãe
            inocentemente caminha na direção do corredor que dá acesso ao sótão.

            O que você faz?
            """
        part4 = """
            Sua mãe se assusta e cai sentada, sentindo um calafrio e derrepente o demônio 
            aparece no fim do corredor. Ela está prestes a ser atacada pelo demônio.

            O que você faz?
           """
        part5 = """
            O demônio se esquiva e consegui fugir de seu alcance. Então novamente o demônio 
            tenta atacá-la.

            O que você faz?

            """
        part6 = """
            Seu corpo entra em contato com o demônio e acaba o possuindo. Neste momento você
            toma posse dos poderes e do corpo do demônio, dando o poder de salvar sua mãe e
            todas as almas que jaziam ali em constante sofrimento. Apos salvar a todos você 
            usa os poderes do proprio  demônio para matá-lo.

            FIM.
            """
        


        choice1 = "1- procurar a Liza!\n2- procurar o demônio? Antes que ele a encontre!\n3- encontrar uma saída para a Liza fugir.\n"
        choice2 = "1- você vai até a sua mãe rapidamente e tenta tocá-la.\n2- grita bem alto para sua mãe te notar.\n3- tenta movimentar a cadeira perto de você, para chamar atenção de sua mãe.\n"
        choice3 = "1- Tenta impedir que sua mãe avance, empurrando ela.\n2- Você tenta assustar sua mãe jogando a cadeira contra a parede.\n3 -Tenta mais uma vez falar com sua mãe.\n"
        choice4 = "1- Tenta tirar sua mãe do caminho do demônio.\n2- Tenta barrar o demônio com seu corpo.\n3- Tenta possuir o demônio.\n"
        choice5 = "1- Tenta possuir o demônio novamente.\n2- Tenta jogar a cadeira no demônio.\n3- Tenta barrar o demônio com seu corpo.\n"
        super().__init__(part1,part2,part3,part4,part5,part6,choice1,choice2,choice3,choice4,choice5)
    def __str__(self):
        return ""
    def choices_History1(self,choice):
        try:
            int(choice)

            if choice == 1:
                choice = list()
                choice.extend(["",2])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["você acaba esbarrando  com o demônio...",6])
                return choice
            else:
                choice = list()
                choice.extend(["você á encontra e tenta fazer contato com ela mas...",3])
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
                choice.extend(["",4])
                return choice
            else:
                choice = list()
                choice.extend(["",4])
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
                choice.extend(["",4])
                return choice
            else:
                choice = list()
                choice.extend(["você se prepara para tentar falar com sua mãe, porem o demônio aparece e você tenta segura-lo...",5])
                return choice
        except:
            return self
    def choices_History4(self,choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["você tira sua mãe do caminho porem o demônio acaba te atingindo...",6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",6])
                return choice
            else:
                choice = list()
                choice.extend(["",5])
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
                choice.extend(["ao jogar a cadeira você acaba se esbarrando no demônio...",6])
                return choice
            else:
                choice = list()
                choice.extend(["",6])
                return choice
        except:
            return self
  