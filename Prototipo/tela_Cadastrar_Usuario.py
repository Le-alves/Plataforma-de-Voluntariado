import tkinter as tk
from tkinter import messagebox
from voluntario import Voluntario
from historico import ManipuladorDeDados  # Assumindo que este arquivo gerencia os dados

class TelaCadastrarVoluntario:
    def __init__(self, root, manipulador_dados):
        self.root = root
        self.manipulador_dados = manipulador_dados
        self.configurar_janela()
        self.criar_widgets()

    def configurar_janela(self):
        self.root.title("Cadastrar Voluntário")
        self.root.geometry("400x300")

    def criar_widgets(self):
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(expand=False)

         # Definindo a fonte padrão
        font_padrao = ("Arial", 10)

        self.nome_label = tk.Label(self.main_frame, text="Nome de Usuário:", font=font_padrao)
        self.nome_label.pack(anchor='w')
        self.nome_entry = tk.Entry(self.main_frame)
        self.nome_entry.pack(fill=tk.X)

        self.email_label = tk.Label(self.main_frame, text="Email:", font=font_padrao)
        self.email_label.pack(anchor='w')
        self.email_entry = tk.Entry(self.main_frame)
        self.email_entry.pack(fill=tk.X)

        self.keywords_label = tk.Label(self.main_frame, text="Interesses (separados por vírgula):", font=font_padrao)
        self.keywords_label.pack(anchor='w')
        self.keywords_entry = tk.Entry(self.main_frame)
        self.keywords_entry.pack(fill=tk.X)

        self.cadastrar_button = tk.Button(self.main_frame, text="Cadastrar", font=font_padrao, command=self.cadastrar)
        self.cadastrar_button.pack(pady=10)

    def cadastrar(self):
        nome_usuario = self.nome_entry.get()
        email = self.email_entry.get()
        keywords = self.keywords_entry.get().split(',')

        if not nome_usuario or not email:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        voluntario = Voluntario(self.manipulador_dados)
        voluntario.cadastrar(nome_usuario, email, [kw.strip() for kw in keywords])
        
        messagebox.showinfo("Sucesso", "Voluntário cadastrado com sucesso!")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    manipulador_dados = ManipuladorDeDados('data.json')
    app = TelaCadastrarVoluntario(root, manipulador_dados)
    root.mainloop()
