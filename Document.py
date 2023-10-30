#Classe que representa um documento de compra
class Document:
    def __init__(self, person, value, id, date, numItems):
        self.__person = person
        self.__price = value
        self.__id = id
        self.__date =  date
        self.__numItems = numItems

#Método que faz a "impressão completa" de todas as informações da comrpra inclusive do comprador
    def values(self):
        print(f"Comprador: {self.__person.getName()} - {self.__person.getCPF()}\nPreço total: {self.__price}\nID: {self.__id}\nData: {self.__date}\nNúmero de itens: {self.__numItems}")

    def getId(self):
        return self.__id