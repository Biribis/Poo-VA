from VoiceCommand import *
from Document import *
from random import randint
from datetime import date

#Classe comando de voz especificado para realizar compras
class VPurchase(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

#Método de execução específico que gera números aleatórios para os dados da compra
    def execute(self,person):
        price =randint(1,5001)
        id = randint(10000000,99999999)
        dat = date.today()
        items = randint(1,51)
        new = Document(person, price, id, dat, items)
        person.addHistory(new)