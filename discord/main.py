# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *

janela = Tk()
janela.title('Discord')
janela.geometry('600x400')
janela['bg'] = '#404EED'

lemail = Label(text='Email')
eemail = Entry(fg='black', bg='gray', width=50)
lsenha = Label(text='Senha')
esenha = Entry(fg='black', bg='gray', width=50)
btn_enviar = Button(text='Entrar', width=25, bg="blue", fg="white")

lemail.pack()
eemail.pack()
lsenha.pack()
esenha.pack()
btn_enviar.pack()

janela.mainloop()
