import tkinter as tk
from tkinter import messagebox
from ong_diretor import Diretor
from projeto import Projeto
from voluntario import Voluntario

class Tela_Inicial :

    def __init__(self, root):
        self.root = root
        self.configurar_janela()
        self.criar_widgets()

    def configurar_janela(self):
        self.root.title("Plataforma de Voluntariado")
        self.root.geometry("800x700")  # Define o tamanho da janela
        #self.root.resizable(False, False)  # Impede redimensionamento

    def criar_widgets(self):
        #Frame Principal 
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(expand=True)

        # Título principal
        self.title_label = tk.Label(self.main_frame, text="Bem-vindo à Plataforma de Voluntariado", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Botão para Cadastrar Diretor
        self.btn_voluntario = tk.Button(self.main_frame, text="Cadastrar Diretor", command=self.cadastrar_diretor)
        self.btn_voluntario.pack(fill=tk.X, pady=5)

         # Botão para Cadastrar Voluntário
        self.btn_voluntario = tk.Button(self.main_frame, text="Cadastrar Voluntário", command=self.cadastrar_voluntario)
        self.btn_voluntario.pack(fill=tk.X, pady=5)

        self.btn_sair = tk.Button(self.main_frame, text="Sair", command=self.root.quit)
        self.btn_sair.pack(fill=tk.X, pady=5)

    def cadastrar_diretor(self):
        messagebox.showinfo("Cadastro_Diretor", "Função de criação de diretor não implementada.")

    def cadastrar_voluntario(self):
        messagebox.showinfo("Cadastro_Volutario", "Função de cadastro de voluntário não implementada.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Tela_Inicial(root)
    root.mainloop()