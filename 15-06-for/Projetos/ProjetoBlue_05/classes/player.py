from time import sleep
import os

class Player:
    def __init__(self,part1="",part2="",part3="",part4="",part5="",part6="",choice1="",choice2="",choice3="",choice4="",choice5=""):
        #here are all historys parts
        #aqui estão todas as partes das histórias
        self._part0_history = """
            ###################
            #       ####      #
            ###   ########  ###
            ###   ########  ###
            ###   ########  ###
            ###.  .######. ####
            #####:       !#####
            ################ma guerra sovietica iniciou-se durante um período de fome
                            e miséria nos paises de Tadjiquistão e quirguistão pois os
                            mesmos sofriam com saqueamentos continuos por saqueadores
                            dos paises bálticos, o que pode -se levar como o estopin da
                            guerra em questão. Uma guerra que permeou pelo tempo até os
                            dias de hoje."""
        self._part1_history = part1
        self._part2_history = part2
        self._part3_history = part3
        self._part4_history = part4
        self._part5_history = part5
        self._part6_history = part6
        # here are all choices
        # aqui estão as escolhas
        self._choice1 = choice1
        self._choice2 = choice2
        self._choice3 = choice3
        self._choice4 = choice4
        self._choice5 = choice5

    def __str__(self):
        return "Valor incorreto!!"
        #metodo de epera
        #wait method
    def wait(self,timewait):
        waiting = ""
        for i in range(timewait):    
            waiting += "● "
            print(waiting)
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
    def sequence_History(self,sequence):
        try:
            int(sequence)
            historys = list([self.history1,self.history2,self.history3,self.history4,self.history5,self.history6])
            historys = historys[sequence-1]
            return historys
        except:
            return self
    def sequence_choices(self,sequence):
        try:
            int(sequence)
            choices = list([self.choice1,self.choice2,self.choice3,self.choice4,self.choice5])
            choices = choices[sequence-1]
            return choices
        except:
            return self
    
    # Get property methods for parts of history
    # metodos proprietários de get para partes da historia
    @property
    def history0(self):
        return self._part0_history
    @property
    def history1(self):
        return self._part1_history
    @property
    def history2(self):
        return self._part2_history
    @property
    def history3(self):
        return self._part3_history
    @property
    def history4(self):
        return self._part4_history
    @property
    def history5(self):
        return self._part5_history
    @property
    def history6(self):
        return self._part6_history

    #Get property methods for the options
    #metodos proprietarios de get para as opções
    @property
    def choice1(self):
        return self._choice1
    @property
    def choice2(self):
        return self._choice2
    @property
    def choice3(self):
        return self._choice3
    @property
    def choice4(self):
        return self._choice4
    @property
    def choice5(self):
        return self._choice5
    

