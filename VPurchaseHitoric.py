from VoiceCommand import *
#Classe comando de vez específico que mostra o histórico de compras do usuário pelo id da compra
class VPurchaseHistoric(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

    def execute(self, person):
        print(person.purchaseHistory())