#Classe que representa a pessoa que interage com o(a) assistente virtual
#Na criação de um objeto existe a criação deuma lista em que se temas compras feitas por aquela pessoa em específico
class Person:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        self.historico = []

    def getName(self):
        return self.name

    def purchaseHistory(self):
        return self.historico

#Método que adiciona o objeto documento gerado após o objeto comando de voz de compra utilizar o método execute()
    def addHistory(self,doc):
        self.historico.append(doc)

    def getCPF(self):
        return self.cpf
