
class Discord(object):
    __servidores = []
    __usuarios = []
    def __init__(self):
        pass

    @staticmethod
    def servidores():
        return Discord.__servidores

    @staticmethod
    def links():
        lista = []
        for server in Discord.__servidores:
            lista.append(server.link)
        return lista

    @staticmethod
    def add_usuarios(user):
        return Discord.__usuarios.append(user)


