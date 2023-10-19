from VoiceCommand import *
#Classe comando de vez específico que mostra todos os documentos de compra de um(a) usuário(a)
class VDocuments(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

    def execute(self, person,va):
        list = person.purchaseHistory()
        for i in range(len(list)):
            print(f'{i} - {list[i].getId()}')
        docum = int(input("Escolha o documento a ser revisado pelo índice: "))
        desejado = list[docum]
        desejado.values()
