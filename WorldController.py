from World import *
class WorldController:
# Método que começa a execução e chama todos os outros métodos
# Existem, na sua execução, sempre dois objetos básicos iniciais: uma pessoa e um(a) assistente virtual que interagem por meio dos métodos
# Com a criação de novas pessoas e assistentes vituais se faz necessário sempre guardar quem são os que estão interagindo ou que estão "ativos"
    def run(self):
        world = World()
        vactive = self.genVA(world)
        active = self.genPerson(world)
        while True:
            self.Screen()
            action = int(input(f"Olá {active.getName()}\nSou {vactive.getName()}\nO que posso fazer por você? "))
            if action == 1:
                self.genVA(world)
            elif  action == 2:
                vactive = self.changeVA(world)
            elif action == 3:
                self.verifyAssist(world)
            elif action == 4:
                self.genPerson(world)
            elif action == 5:
                active = self.changeUser(world)
            elif action == 6:
                vactive.showCommands()
            elif action == 7:
                vactive.listen(active,vactive)
            elif action == 8:
                break
            else:
                print("Essa opção não existe\n\n")


#Método que gera mais pessoas por meio da classe Person, a fim de usuários diferentes interagirem com o(a) assistente virtual
    def genPerson(self,ww):
        nme = input("Qual o nome do usuário? ")
        cpf = int(input("E o CPF? "))
        person = ww.genPerson(nme,cpf)
        return person

# Sempre, no início de cada loop, é feito a impressão de todas as opções de interações entre os objetos
    def Screen(self):
        print("\n\n01 - Gerar assistente Virtual")
        print("02 - Trocar assistente virtual")
        print("03 - Verificar assitentes disponiveis")
        print("04 - Adicionar usuário")
        print("05 - Trocar usuário")
        print("06 - Verificar comandos disponiveis")
        print("07 - Dar um comando")
        print("08 - Finalizar programa")

#Método gera novos(as) assistentes virtuais
    def genVA(self,ww):
        nme = input("Assistant name: ")
        va = ww.genVA(nme)
        return va

#Método que verifica todos os(as) assitentes virtuais disponíveis para interação
    def verifyAssist(self,ww):
        for i in range(len(ww.assistants)):
            print(f'{i} - {ww.assistants[i].getName()}')

#Método que troca a pessoa "ativa"
    def changeUser(self,ww):
        for i in range(len(ww.persons)):
            print(f'{i} - {ww.persons[i].getName()}')
        user = int(input("Digite o indice du usuário desejado: "))
        return ww.persons[user]

#Método que troca o(a) assistente virtual "ativo(a)"
    def changeVA(self,ww):
        for i in range(len(ww.assistants)):
            print(f'{i} - {ww.assistants[i].getName()}')
        assistant = int(input("Digite o indice du usuário desejado: "))
        return ww.assistants[assistant]

if __name__ == '__main__':
    Run = WorldController()
    Run.run()