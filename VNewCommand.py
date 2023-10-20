from VoiceCommand import *
#Classe comando de vez específico que mostra todos os documentos de compra de um(a) usuário(a)
class VNewCommand(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

# Método que adiciona novos comandos de voz genéricos
    def execute(self, person,va):
        nme = input("Qual o nome do novo comando? ")
        newCom = VoiceCommand(nme)
        va.commands.append(newCom)