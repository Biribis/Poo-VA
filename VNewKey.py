from VoiceCommand import *
#Classe comando de vez específico que mostra todos os documentos de compra de um(a) usuário(a)
class VNewKey(VoiceCommand):
    def __init__(self,name):
        super().__init__(name)

# Método que acessa a lista de palavras-cahve de um comando especificado pelo índice, para que o método de adicionar palavras-chave seja executado
    def execute(self, person,va):
        va.showCommands()
        key = int(input("Digite o indice do comando a ser atualizado: "))
        list = va.getCommands()
        command = list[key]
        command.addKeyword()
