from VoiceCommand import *
#Classe comando de vez específico que mostra todos os documentos de compra de um(a) usuário(a)
class VDocuments(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

    def execute(self, person,va):
        ll = person.purchaseHistory()
        for i in range(len(ll)):
            print(f'{i} - {ll[i].getId()}')
        docum = int(input("Escolha o documento a ser revisado pelo índice: "))
        desejado = ll[docum]
        desejado.values()
