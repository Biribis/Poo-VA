from VoiceCommand import *
#Classe comando de voz específico que adiciona novos comandos de voz para o(a) assistente virtual ativo(a)
class VNewCommand(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

    def execute(self, person,va):
        nme = input("Qual o nome do novo comando? ")
        newCom = VoiceCommand(nme)
        va.commands.append(newCom)