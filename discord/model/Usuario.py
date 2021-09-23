from Discord import Discord

class Usuario():
    def __init__(self, id, nome, email, senha, data_nascimento, avatar, status):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__data_nascimento = data_nascimento
        self.__avatar = avatar
        self.__status = status
        self.__mensagens = []

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    @property
    def status(self):
        return self.__status

    @property
    def avatar(self):
        return self.__avatar

    @property
    def mensagens(self):
        return self.__mensagens

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @email.setter
    def email(self, novo_email):
        self.__email = novo_email

    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha

    @avatar.setter
    def avatar(self, novo_avatar):
        self.__avatar = novo_avatar

    @status.setter
    def status(self, novo_status):
        self.__status = novo_status

    def enviar_mensagem_direta(self,destinatario,mensagem):


    def receber_mensagem(self,mensagem):
        self.__mensagens.append(mensagem)
