#Classe mãe comando de voz genérico
#Cada comando de voz pode ter mais de uma palavra-chave que o ativa
class VoiceCommand:
    def __init__(self,name):
        self.__name = name
        self.__keyWord = []
        self.__keyWord.append(name)

    def getKeyword(self)->list:
        return self.__keyWord

#Método que adiciona uma palavra-chave nova ao comando
    def addKeyword(self):
        command = input("Adicione a palavra chave: ")
        self.__keyWord.append(command)

    def getName(self):
        return self.__name

#Método que executa a função do comando em si, para um comando de voz genérico só imprime o nome do usuário e o do comando(em caixa alta)
    def execute(self,person,va):
        print(f"{person.getName()}\n{self.__name.upper()}")
