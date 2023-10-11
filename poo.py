# Aprender o processo de tradução de comandos de voz de compras em documentação

from random import randint
from datetime import date

#Classe mãe comando de voz genérico
#Cada comando de voz pode ter mais de uma palavra-chave que o ativa
class VoiceCommand:
    def __init__(self,name):
        self.name = name
        self.keyWord = []
        self.keyWord.append(name)

    def getKeyword(self)->list:
        return self.keyWord

#Método que adiciona uma palavra-chave nova ao comando
    def addKeyword(self):
        command = input("Adicione a palavra chave: ")
        self.keyWord.append(command)

    def getName(self):
        return self.name

#Método que executa a função do comando em si, para um comando genérico só imprime o nome do usuário e o do comando
    def execute(self,person):
        print(f"{person.getName()}\n{self.name.upper()}")

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

#Classe comando de vez específico que mostra o histórico de compras do usuário pelo id da compra
class VPurchaseHistoric(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

    def execute(self, person):
        print(person.purchaseHistory())

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

#Classe controladora: executa todas as interações no mundo criado
class World:
    def __init__(self):
        self.persons = []
        self.assistants = []

#Método que gera mais pessoas por meio da classe Person, a fim de usuários diferentes interagirem com o(a) assistente virtual
    def genPerson(self):
            nme = input("Qual o nome do usuário? ")
            cpf = int(input("E o CPF? "))
            new = Person(nme,cpf)
            self.persons.append(new)
            return new

#Sempre, no início de cada loop, é feito a impressão de todas as opções de interações entre os objetos
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

#Método gera novos(as) assistentes virtuais
    def genVA(self):
        nme = input("Assistant name: ")
        new = VirtualAssistant(nme)
        self.assistants.append(new)
        return new

#Método que verifica todos os(as) assitentes virtuais disponíveis para interação
    def verifyAssist(self):
        for i in range(len(self.assistants)):
            print(f'{i} - {self.assistants[i].getName()}')

#Método que troca a pessoa "ativa"
    def changeUser(self):
        for i in range(len(self.persons)):
            print(f'{i} - {self.persons[i].getName()}')
        user = int(input("Digite o indice du usuário desejado: "))
        return self.persons[user]

#Método que troca o(a) assistente virtual "ativo(a)"
    def changeVA(self):
        for i in range(len(self.assistants)):
            print(f'{i} - {self.assistants[i].getName()}')
        assistant = int(input("Digite o indice du usuário desejado: "))
        return self.assistants[assistant]

#Método que nusca todos os documentos no histórico da pessoa "ativa" e imprime as informações da compra escolhida pelo índice
    def verifyDoc(self,person):
        ll = person.purchaseHistory()
        for i in range(len(ll)):
            print(f'{i} - {ll[i].getId()}')
        docum = int(input("Escolha o documento a ser revisado pelo índice: "))
        desejado = ll[docum]
        desejado.values()

#Método que acessa a lista de palavras-cahve de um comando especificado pelo índice, para que o método de adicionar palavras-chave seja executado
    def keyword(self, va):
        va.showCommands()
        key = int(input("Digite o indice do comando a ser atualizado: "))
        ll = va.getCommands()
        command = ll[key]
        command.addKeyword()

#Método que começa a execução e chama todos os outros métodos
#Existem, na sua execução, sempre dois objetos básicos iniciais: uma pessoa e um(a) assistente virtual que interagem por meio dos métodos
#Com a criação de novas pessoas e assistentes vituais se faz necessário sempre guardar quem são os que estão interagindo ou que estão "ativos"
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

#Classe que representa os(as) assistentes virtuais
#Em cada um(a) existe uma lista com todos os comandos disponíveis e outra com o histórico de comandos rodados
#Todos os(as) assistentes virtuais já começam com os comandos de compra e de histórico de compra já cadastrados
class VirtualAssistant:
    def __init__(self, name):
        self.name = name
        self.commands = []
        self.historic = []
        comandInit = VPurchase("comprar")
        self.commands.append(comandInit)
        comandInit = VPurchaseHistoric("historico")
        self.commands.append(comandInit)

#Método que adiciona novos comandos de voz genéricos
    def addCommand(self):
        nme = input("Qual o nome do novo comando? ")
        newCom = VoiceCommand(nme)
        self.commands.append(newCom)
        self.endCommand()

#Método que sinaliza o final de cada operação ordenada pelo usuário
    def endCommand(self):
        print("++++++++++++\nTarefa finalizada!!!\n++++++++++++")

#Método que lista todos os comandos disponíveis para aquele(a) asssitente
    def showCommands(self):
        for i in range(len(self.commands)):
            print(f'{i} - {self.commands[i].getName()}')

    def getCommands(self):
        return self.commands

    def getName(self):
        return self.name

#Método que imprime o histórico de comandos chamados naquele(a) assistente
    def history(self):
        print(self.historic)

#Método que recebe uma fala da pessoa "ativa" e o lê a fim de identificar qual comando de voz executar
    def listen(self, person):
        print("Ouvindo... ")
        comando = input()
        a = 1
        for i in range(len(self.commands)):
            ll = self.commands[i].getKeyword()
            for j in range(len(ll)):
                if ll[j] in comando:
                    self.commands[i].execute(person)
                    self.historic.append(self.commands[i].getName())
                    self.endCommand()
                    a = 0
                    break
            if a == 0:
                break

if __name__ == '__main__':
    Run = World()
    Run.run()