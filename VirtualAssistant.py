from VPurchase import *
from VCommandHitoric import *
from VDocuments import *
#Classe que representa os(as) assistentes virtuais
#Em cada um(a) existe uma lista com todos os comandos disponíveis e outra com o histórico de comandos rodados
#Todos os(as) assistentes virtuais já começam com os comandos de compra, de ver documentos de compra e de histórico de comandos já cadastrados
#Por meio das palavras-chave: comprar, documneto e historico, respectivamente
class VirtualAssistant:
    def __init__(self, name):
        self.name = name
        self.commands = []
        self.historic = []
        comandInit = VPurchase("comprar")
        self.commands.append(comandInit)
        comandInit = VCommandHistoric("historico")
        self.commands.append(comandInit)
        comandInit = VDocuments("documento")
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
        try:
            return self.historic
        finally:
            self.historic.append('historico')

#Método que recebe uma fala da pessoa "ativa" e o lê a fim de identificar qual comando de voz executar
    def listen(self, person,va):
        print("Ouvindo... ")
        comando = input()
        a = 1
        for i in range(len(self.commands)):
            ll = self.commands[i].getKeyword()
            for j in range(len(ll)):
                if ll[j] in comando:
                    self.commands[i].execute(person,va)
                    self.historic.append(self.commands[i].getName())
                    self.endCommand()
                    a = 0
                    break
            if a == 0:
                break