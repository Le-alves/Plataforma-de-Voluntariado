import tkinter as tk
from tkinter import messagebox
from projeto import Projeto
from historico import ManipuladorDeDados

class TelaCadastrarProjeto:

    def __init__(self, root, manipulador_dados):
        self.root = root
        self.manipulador_dados = manipulador_dados
        self.configurar_janela()
        self.criar_widgets()

    def configurar_janela(self):
        self.root.title("Cadastrar Projeto")
        self.root.geometry("400x400")

    def criar_widgets(self):
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(expand=False)

        # Definindo a fonte padrão
        font_padrao = ("Arial", 10)

        # Campo para o título do projeto
        self.titulo_label = tk.Label(self.main_frame, text="Título do Projeto:", font=font_padrao)
        self.titulo_label.pack(anchor='w')
        self.titulo_entry = tk.Entry(self.main_frame, font=font_padrao, width=40)
        self.titulo_entry.pack(fill=tk.X)

        # Campo para a descrição do projeto
        self.descricao_label = tk.Label(self.main_frame, text="Descrição do Projeto:", font=font_padrao)
        self.descricao_label.pack(anchor='w')
        self.descricao_entry = tk.Entry(self.main_frame, font=font_padrao, width=40)
        self.descricao_entry.pack(fill=tk.X)

        # Campo para as palavras-chave do projeto
        self.keywords_label = tk.Label(self.main_frame, text="Palavras-chave (separadas por vírgula):", font=font_padrao)
        self.keywords_label.pack(anchor='w')
        self.keywords_entry = tk.Entry(self.main_frame, font=font_padrao, width=40)
        self.keywords_entry.pack(fill=tk.X)

        # Campo para selecionar o organizador (ONG)
        self.organizador_label = tk.Label(self.main_frame, text="Organizador (ONG):", font=font_padrao)
        self.organizador_label.pack(anchor='w')
        self.organizador_entry = tk.Entry(self.main_frame, font=font_padrao, width=40)
        self.organizador_entry.pack(fill=tk.X)

        # Botão de Cadastrar Projeto
        self.cadastrar_button = tk.Button(self.main_frame, text="Cadastrar", font=font_padrao, command=self.cadastrar)
        self.cadastrar_button.pack(pady=20)

    def cadastrar(self):
        titulo = self.titulo_entry.get()
        descricao = self.descricao_entry.get()
        keywords = self.keywords_entry.get().split(',')
        organizador_id = self.organizador_entry.get()

        if not titulo or not descricao or not organizador_id:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        projeto = Projeto(self.manipulador_dados)
        projeto.criar_projeto(titulo, descricao, organizador_id, [kw.strip() for kw in keywords])
        
        messagebox.showinfo("Sucesso", "Projeto cadastrado com sucesso!")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    manipulador_dados = ManipuladorDeDados('data.json')
    app = TelaCadastrarProjeto(root, manipulador_dados)
    root.mainloop()
