import tkinter as tk
from tkinter import messagebox
from ong_diretor import Diretor
from historico import ManipuladorDeDados

class TelaCadastrarDiretor:

    def __init__(self,root, manipulador_dados):
        self.root = root
        self.manipulador_dados = manipulador_dados
        self.configurar_janela()
        self.criar_widgets()

    def configurar_janela(self):
        self.root.title("Cadastrar Diretor (ONG)")
        self.root.geometry("400x300")

    def criar_widgets(self):
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(expand=True)

        self.nome_label = tk.Label(self.main_frame, text="Nome:")
        self.nome_label.pack(anchor='w')
        self.nome_entry = tk.Entry(self.main_frame)
        self.nome_entry.pack(fill=tk.X)

        self.email_label = tk.Label(self.main_frame, text="Email:")
        self.email_label.pack(anchor='w')
        self.email_entry = tk.Entry(self.main_frame)
        self.email_entry.pack(fill=tk.X)

        self.cadastrar_button = tk.Button(self.main_frame, text="Cadastrar", command=self.cadastrar)
        self.cadastrar_button.pack(pady=10)

    def cadastrar(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()

        if not nome or not email:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        diretor = Diretor(self.manipulador_dados)
        diretor.cadastrar(nome, email, [])
        
        messagebox.showinfo("Sucesso", "Diretor cadastrado com sucesso!")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    manipulador_dados = ManipuladorDeDados('data.json')
    app = TelaCadastrarDiretor(root, manipulador_dados)
    root.mainloop()