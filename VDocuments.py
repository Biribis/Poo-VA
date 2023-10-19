from VoiceCommand import *
#Classe comando de vez específico que mostra o histórico de compras do usuário pelo id da compra
class VDocuments(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

    def execute(self, person):
        ll = person.purchaseHistory()
        for i in range(len(ll)):
            print(f'{i} - {ll[i].getId()}')
        docum = int(input("Escolha o documento a ser revisado pelo índice: "))
        desejado = ll[docum]
        desejado.values()
