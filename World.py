from Person import *
from VirtualAssistant import *

#Classe controladora+mundo: executa todas as interações no mundo criado
#Neste mundo existem pessoas e assistentes virtuais que interagem por meio de comandos de voz
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
        print("10 - Finalizar programa")

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

#Método que acessa a lista de palavras-cahve de um comando especificado pelo índice, para que o método de adicionar palavras-chave seja executado
    def keyword(self, va):
        va.showCommands()
        key = int(input("Digite o indice do comando a ser atualizado: "))
        list = va.getCommands()
        command = list[key]
        command.addKeyword()
        va.endCommand()

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
                vactive.listen(active,vactive)
            elif action == 10:
                break
            else:
                print("Essa opção não existe\n\n")


if __name__ == '__main__':
    Run = World()
    Run.run()