class Clock:
    def __init__(self,timer,time,base):
        self.timer = timer
        self.time_move = time
        self.base_choices = base
#faz o tempo passar
    def passTime(self):
        self.timer -= self.time_move
#calcula tempo resposta
    def performTimeResponse(self,wait_response):
        self.timer -= self.base_choices * wait_response
