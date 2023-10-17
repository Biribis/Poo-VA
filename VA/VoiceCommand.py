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
