
class Canal(object):
    def __init__(self,nome):
        self.__nome = nome
        self.__ativos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def ativos(self):
        return self.__ativos

    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome

    def entrar_no_canal(self,membro):
        if(membro not in self.__ativos):
            self.__ativos.append(membro)
            return True
        else:
            return False

    def sair_do_canal(self,membro):
        if(membro in self.__ativos):
            for e in range(len(self.__ativos)):
                if(self.__ativos[e] == membro):
                    del(self.__ativos[e])
                    return True
        return False

    