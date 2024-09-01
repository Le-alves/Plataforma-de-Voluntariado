import tkinter as tk
from tkinter import messagebox
from ong_diretor import Diretor
from projeto import Projeto
from voluntario import Voluntario
from tela_Cadastrar_Diretor import TelaCadastrarDiretor
from tela_Cadastrar_Usuario import TelaCadastrarVoluntario
from tela_Cadastrar_Projeto import TelaCadastrarProjeto
from historico import ManipuladorDeDados

class Tela_Inicial :

    def __init__(self, root):
        self.root = root
        self.manipulador_dados = ManipuladorDeDados('data.json')
        self.configurar_janela()
        self.criar_widgets()

    def configurar_janela(self):
        self.root.title("Plataforma de Voluntariado")
        self.root.geometry("800x700")  # Define o tamanho da janela
        #self.root.resizable(False, False)  # Impede redimensionamento

    def criar_widgets(self):
        #Frame Principal 
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(expand=False)

        # Título principal
        self.title_label = tk.Label(self.main_frame, text="Bem-vindo à Plataforma de Voluntariado", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Botão para Cadastrar Diretor
        self.btn_voluntario = tk.Button(self.main_frame, text="Cadastrar Diretor",font=("Arial", 13) , command=self.cadastrar_diretor)
        self.btn_voluntario.pack(fill=tk.X, pady=25)

         # Botão para Cadastrar Voluntário
        self.btn_voluntario = tk.Button(self.main_frame, text="Cadastrar Voluntário",font=("Arial", 13) , command=self.cadastrar_voluntario)
        self.btn_voluntario.pack(fill=tk.X, pady=25)

        # Botão para Cadastrar Projeto
        self.btn_projeto = tk.Button(self.main_frame, text="Cadastrar Projeto", font=("Arial", 13), command=self.cadastrar_projeto)
        self.btn_projeto.pack(fill=tk.X, pady=25)

        self.btn_sair = tk.Button(self.main_frame, text="Sair", font=("Arial", 13), command=self.root.quit)
        self.btn_sair.pack(fill=tk.X, pady=25)

    def cadastrar_diretor(self):
        nova_janela = tk.Toplevel(self.root)
        TelaCadastrarDiretor(nova_janela, self.manipulador_dados)

    def cadastrar_voluntario(self):
        nova_janela = tk.Toplevel(self.root)
        TelaCadastrarVoluntario(nova_janela, self.manipulador_dados)

    def cadastrar_projeto(self):
        nova_janela = tk.Toplevel(self.root)
        TelaCadastrarProjeto(nova_janela, self.manipulador_dados)

if __name__ == "__main__":
    root = tk.Tk()
    app = Tela_Inicial(root)
    root.mainloop()