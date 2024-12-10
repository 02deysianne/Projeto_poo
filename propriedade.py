import tkinter as tk
from tkinter import messagebox

# Classe Solo: Representa o tipo de solo de uma propriedade
class Solo:
    def __init__(self, tipo):
        self._tipo = tipo  # Inicializa o tipo de solo

    # Getter e Setter para o tipo de solo
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        self._tipo = novo_tipo  # Atualiza o tipo de solo


# Classe Propriedade: Representa uma propriedade rural com nome, localização e tipo de solo
class Propriedade:
    def __init__(self, nome, localizacao, solo):
        self._nome = nome  # Nome da propriedade
        self._localizacao = localizacao  # Localização da propriedade
        self._solo = solo  # Tipo de solo da propriedade

    # Getters e Setters para os atributos da propriedade
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome  # Atualiza o nome da propriedade

    @property
    def localizacao(self):
        return self._localizacao

    @localizacao.setter
    def localizacao(self, nova_localizacao):
        self._localizacao = nova_localizacao  # Atualiza a localização da propriedade

    @property
    def solo(self):
        return self._solo

    @solo.setter
    def solo(self, novo_solo):
        self._solo = novo_solo  # Atualiza o tipo de solo da propriedade

    # Método que retorna os detalhes da propriedade em formato de string
    def detalhes(self):
        return f"Nome: {self._nome}\nLocalização: {self._localizacao}\nTipo de Solo: {self._solo.tipo}"

    # Método para alterar o tipo de solo
    def alterar_solo(self, novo_tipo):
        self._solo.tipo = novo_tipo  # Altera o tipo de solo
        return f"Tipo de solo da propriedade {self._nome} alterado com sucesso para {novo_tipo}!"


# Funções para interação com o usuário na interface gráfica
def criar_propriedade():
    try:
        # Obtém os dados inseridos pelo usuário
        nome = nome_entry.get()
        localizacao = localizacao_entry.get()
        tipo_solo = tipo_solo_entry.get()

        # Cria o objeto Solo e Propriedade
        solo = Solo(tipo_solo)
        global propriedade  # Declara a variável como global para poder usá-la em outras funções
        propriedade = Propriedade(nome, localizacao, solo)

        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Propriedade criada com sucesso!")
    except ValueError:
        # Exibe uma mensagem de erro se os dados não forem válidos
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")


def alterar_tipo_solo():
    if propriedade:  # Verifica se a propriedade foi criada
        try:
            # Obtém o novo tipo de solo inserido pelo usuário
            novo_tipo = tipo_solo_entry.get()
            resultado = propriedade.alterar_solo(novo_tipo)  # Altera o tipo de solo
            # Exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", resultado)
        except ValueError:
            # Exibe mensagem de erro se o tipo de solo não for válido
            messagebox.showerror("Erro", "Por favor, insira um tipo de solo válido.")
    else:
        # Se não houver uma propriedade criada, exibe um aviso
        messagebox.showwarning("Aviso", "Nenhuma propriedade criada ainda.")


def exibir_detalhes():
    if propriedade:  # Verifica se a propriedade foi criada
        detalhes = propriedade.detalhes()  # Obtém os detalhes da propriedade
        # Exibe os detalhes da propriedade em uma mensagem
        messagebox.showinfo("Detalhes da Propriedade", detalhes)
    else:
        # Se não houver uma propriedade criada, exibe um aviso
        messagebox.showwarning("Aviso", "Nenhuma propriedade criada ainda.")


# Interface gráfica usando tkinter
root = tk.Tk()
root.title("Gerenciador de Propriedades")  # Título da janela
root.geometry("500x450")  # Tamanho da janela

propriedade = None  # Variável para armazenar a propriedade

# Cabeçalho
header = tk.Frame(root, bg="#4CAF50", pady=10)
header.pack(fill="x")
tk.Label(header, text="Gerenciador de Propriedades", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white").pack()

# Criando um container para as informações
container = tk.Frame(root, pady=10)
container.pack(expand=True)

# Entradas para os dados da propriedade (nome, localização, tipo de solo)
tk.Label(container, text="Nome da Propriedade:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=10, pady=5)
nome_entry = tk.Entry(container)  # Caixa de texto para o nome
nome_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(container, text="Localização:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=10, pady=5)
localizacao_entry = tk.Entry(container)  # Caixa de texto para a localização
localizacao_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(container, text="Tipo de Solo:", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=10, pady=5)
tipo_solo_entry = tk.Entry(container)  # Caixa de texto para o tipo de solo
tipo_solo_entry.grid(row=2, column=1, padx=10, pady=5)

# Botões para criar propriedade, alterar tipo de solo e exibir detalhes
buttons = tk.Frame(root, pady=20)
buttons.pack()

tk.Button(buttons, text="Criar Propriedade", command=criar_propriedade, font=("Arial", 12)).grid(row=0, column=0, padx=10)
tk.Button(buttons, text="Alterar Tipo de Solo", command=alterar_tipo_solo, font=("Arial", 12)).grid(row=0, column=1, padx=10)
tk.Button(buttons, text="Exibir Detalhes", command=exibir_detalhes, font=("Arial", 12)).grid(row=0, column=2, padx=10)

# Inicializa o loop da interface gráfica
root.mainloop()
