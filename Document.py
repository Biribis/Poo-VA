#Classe que representa um documento de compra
class Document:
    def __init__(self, person, value, id, date, numItems):
        self.person = person
        self.price = value
        self.id = id
        self.date =  date
        self.numItems = numItems

#Método que faz a "impressão completa" de todas as informações da comrpra inclusive do comprador
    def values(self):
        print(f"Comprador: {self.person.getName()} - {self.person.getCPF()}\nPreço total: {self.price}\nID: {self.id}\nData: {self.date}\nNúmero de itens: {self.numItems}")

    def getId(self):
        return self.id