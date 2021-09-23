from Usuario import Usuario

###classe que representa cada membro ao entrar em um servidor###

class Membro(Usuario):
    def __init__(self,user):
        super().__init__(user.id,user.nome,user.email,user.data_nascimento,user.avatar,user.status)
        self.__cargo = ''
        self.__nome_display = user.nome

    @property
    def cargo(self):
        return self.__cargo

    @property
    def nome_display(self):
        return self.__nome_display

    @cargo.setter
    def cargo(self,novo_cargo):
        self.__cargo = novo_cargo

    @nome_display.setter
    def nome_display(self,novo_nome_display):
        self.__nome_display = novo_nome_display

