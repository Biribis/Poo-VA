from Person import *
from VirtualAssistant import *

#Classe controladora+mundo: executa todas as interações no mundo criado
#Neste mundo existem pessoas e assistentes virtuais que interagem por meio de comandos de voz
class World:
    def __init__(self):
        self.persons = []
        self.assistants = []

#Método que gera mais pessoas por meio da classe Person, a fim de usuários diferentes interagirem com o(a) assistente virtual
    def genPerson(self,nme,cpf):
            new = Person(nme,cpf)
            self.persons.append(new)
            return new

#Método gera novos(as) assistentes virtuais
    def genVA(self,nme):
        new = VirtualAssistant(nme)
        self.assistants.append(new)
        return new