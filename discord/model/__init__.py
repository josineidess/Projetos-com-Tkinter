from Usuario import Usuario
from Servidor import Servidor
from Membro import Membro
from Discord import Discord


josineide = Usuario(1234,'Josineide','josineide@gmail.com','234576','14/02/2000','imagem.com','Hi! meu nome é josi')

print(josineide.nome)
print(josineide.email)
print(josineide.status)
josineide.status = 'estou ocupada'
print(josineide.status)