from VoiceCommand import *
#Classe comando de vez específico que mostra o histórico de compras do usuário pelo id da compra
class VCommandHistoric(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

    def execute(self, person,va):
        ll = va.history()
        for i in ll:
            print(i)