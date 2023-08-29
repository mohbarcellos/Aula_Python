from tkinter import *
janela = Tk() #Abrir a janela
janela.title("Aula 5") #Titulo
janela.geometry("500x500+700+200") # Largura X Altura + distancia esquerda + distancia topo
janela.wm_resizable(width= False , height= False) #travar o tamanho da tela
janela.iconbitmap('C:/Projeto/Icone.ico') #trocar o icone

texto = Label(janela,text="Login") #Texto 
texto.pack() #Localização do texto

txtlogin = Entry() # Caixa
txtlogin.pack()


textosenha = Label(janela,text="Senha")
textosenha.pack()

txtsenha = Entry()
txtsenha.pack()

btentrar = Button(janela,text="Entrar",command="")
btentrar.pack()
 def clique_buton():
    btentrar.configure(text="Botão Cliclado")
janela.mainloop() #manter a janela aberta

