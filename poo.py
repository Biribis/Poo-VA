# Aprender o processo de tradução de comandos de voz de compras em documentação

from random import randint
from datetime import date

class VoiceCommand:
    def __init__(self,name):
        self.name = name
        self.keyWord = []
        self.keyWord.append(name)

    def getKeyword(self)->list:
        return self.keyWord

    def addKeyword(self):
        command = input("Adicione a palavra chave: ")
        self.keyWord.append(command)

    def getName(self):
        return self.name

    def execute(self,person):
        print(f"{person.getName()}\n{self.name.upper()}")

class VPurchase(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

    def execute(self,person):
        price =randint(1,5001)
        id = randint(10000000,99999999)
        dat = date.today()
        items = randint(1,51)
        new = Document(person, price, id, dat, items)
        person.addHistory(new)


class VPurchaseHistoric(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

    def execute(self, person):
        print(person.purchaseHistory())

class Document:
    def __init__(self, person, value, id, date, numItems):
        self.person = person
        self.price = value
        self.id = id
        self.date =  date
        self.numItems = numItems

    def values(self):
        print(f"Comprador: {self.person.getName()} - {self.person.getCPF()}\nPreço total: {self.price}\nID: {self.id}\nData: {self.date}\nNúmero de itens: {self.numItems}")

    def getId(self):
        return self.id

class Person:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        self.historico = []

    def getName(self):
        return self.name

    def purchaseHistory(self):
        return self.historico

    def addHistory(self,doc):
        self.historico.append(doc)

    def getCPF(self):
        return self.cpf

class World:
    def __init__(self):
        self.persons = []
        self.assistants = []

    def genPerson(self):
            nme = input("Qual o nome do usuário? ")
            cpf = int(input("E o CPF? "))
            new = Person(nme,cpf)
            self.persons.append(new)
            return new

    def Screen(self):
        print("\n\n01 - Gerar assistente Virtual")
        print("02 - Trocar assistente virtual")
        print("03 - Verificar assitentes disponiveis")
        print("04 - Adicionar usuário")
        print("05 - Trocar usuário")
        print("06 - Verificar comandos disponiveis")
        print("07 - Adicionar novo comando")
        print("08 - Adicionar nova palavra chave")
        print("09 - Dar um comando")
        print("10 - Ver documento de compra específico")
        print("11 - Finalizar programa")

    def genVA(self):
        nme = input("Assistant name: ")
        new = VirtualAssistant(nme)
        self.assistants.append(new)
        return new

    def verifyAssist(self):
        for i in range(len(self.assistants)):
            print(f'{i} - {self.assistants[i].getName()}')

    def changeUser(self):
        for i in range(len(self.persons)):
            print(f'{i} - {self.persons[i].getName()}')
        user = int(input("Digite o indice du usuário desejado: "))
        return self.persons[user]

    def changeVA(self):
        for i in range(len(self.assistants)):
            print(f'{i} - {self.assistants[i].getName()}')
        assistant = int(input("Digite o indice du usuário desejado: "))
        return self.assistants[assistant]

    def verifyDoc(self,person):
        ll = person.purchaseHistory()
        for i in range(len(ll)):
            print(f'{i} - {ll[i].getId()}')
        docum = int(input("Escolha o documento a ser revisado pelo índice: "))
        desejado = ll[docum]
        desejado.values()

    def keyword(self, va):
        va.showCommands()
        key = int(input("Digite o indice do comando a ser atualizado: "))
        ll = va.getCommands()
        command = ll[key]
        command.addKeyword()


    def run(self):
        vactive = self.genVA()
        active = self.genPerson()
        while True:
            self.Screen()
            action = int(input(f"Olá {active.getName()}\nSou {vactive.getName()}\nO que posso fazer por você? "))
            if action == 1:
                self.genVA()
            elif  action == 2:
                vactive = self.changeVA()
            elif action == 3:
                self.verifyAssist()
            elif action == 4:
                self.genPerson()
            elif action == 5:
                active = self.changeUser()
            elif action == 6:
                vactive.showCommands()
            elif action == 7:
                vactive.addCommand()
            elif action == 8:
                self.keyword(vactive)
            elif action == 9:
                vactive.listen(active)
            elif action == 10:
                 self.verifyDoc(active)
            elif action == 11:
                break
            else:
                print("Essa opção não existe\n\n")

class VirtualAssistant:
    def __init__(self, name):
        self.name = name
        self.commands = []
        self.historic = []
        comandInit = VPurchase("comprar")
        self.commands.append(comandInit)
        comandInit = VPurchaseHistoric("historico")
        self.commands.append(comandInit)

    def addCommand(self):
        nme = input("Qual o nome do novo comando? ")
        newCom = VoiceCommand(nme)
        self.commands.append(newCom)
        self.endCommand()

    def endCommand(self):
        print("++++++++++++\nTarefa finalizada!!!\n++++++++++++")

    def showCommands(self):
        for i in range(len(self.commands)):
            print(self.commands[i].getName())

    def getCommands(self):
        return self.commands

    def getName(self):
        return self.name

    def history(self):
        print(self.historic)

    def listen(self, person):
        print("Ouvindo... ")
        comando = input()
        for i in range(len(self.commands)):
            ll = self.commands[i].getKeyword()
            if comando in ll:
                self.commands[i].execute(person)
                self.historic.append(self.commands[i].getName())
                self.endCommand()
                break

if __name__ == '__main__':
    Run = World()
    Run.run()