import random
from Discord import Discord

###Classe que representa cada servidor criado###

class Servidor():
    def __init__(self,nome,foto):
        self.__nome = nome
        self.__foto = foto
        self.__link = 'discord.com/'
        self.__canais_de_voz = []
        self.__canais_de_texto = []
        self.__membros = []

    @property
    def nome(self):
        return self.__nome

    @property
    def foto(self):
        return self.__foto

    @property
    def link(self):
        if(self.__link == 'discord.com/'):
            self.gerador_de_link()
            return self.__link
        else:
            return self.__link

    @property
    def canais_de_voz(self):
        return self.__canais_de_voz

    @property
    def canais_de_texto(self):
        return self.__canais_de_texto

    @property
    def membros(self):
        return self.__membros

    def adicionar_membros(self,membro):
        try:
            self.__membros.append(membro)
            return True
        except:
            return False

    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome

    @foto.setter
    def foto(self,nova_foto):
        self.__foto = nova_foto

    #função acessa a variavel estatica links da classe Discord para evitar gerar links repetitivos
    def gerador_de_link(self):
        sorteado = random.randint(1000, 9999)
        if(('discord.com/'+str(sorteado)) not in Discord.links()):
            self.__link += str(sorteado)
            return self.__link
        else:
            self.gerador_de_link()






