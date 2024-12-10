import tkinter as tk
from tkinter import messagebox

# Classe Aplicacao - Definição de uma classe
class Aplicacao:
    def __init__(self, cultura, fertilizante, propriedade, quantidade, data):
        # Atributos da classe, encapsulando os dados da aplicação
        self.cultura = cultura  # Objeto da classe Cultura
        self.fertilizante = fertilizante  # Objeto da classe Fertilizante
        self.propriedade = propriedade  # Objeto da classe Propriedade
        self.quantidade = quantidade  # Tipo de dado primitivo (int ou float)
        self.data = data  # Tipo de dado primitivo (string)

    def calcular_custo(self):
        # Método de classe que calcula o custo da aplicação, encapsulando a lógica
        return self.fertilizante.preco * self.quantidade

    def resumo(self):
        # Método de classe que gera um resumo da aplicação
        return (f"Aplicação:\n"
                f"Cultura: {self.cultura.nome}\n"  # Acesso ao atributo da classe Cultura
                f"Fertilizante: {self.fertilizante.nome}\n"  # Acesso ao atributo da classe Fertilizante
                f"Propriedade: {self.propriedade.nome}\n"  # Acesso ao atributo da classe Propriedade
                f"Quantidade: {self.quantidade} kg\n"
                f"Data: {self.data}\n"
                f"Custo Total: R$ {self.calcular_custo():.2f}")

    def verificar_viabilidade(self):
        # Verifica se o fertilizante possui os nutrientes necessários para a cultura
        for nutriente, necessidade in self.cultura.necessidade.items():
            if self.fertilizante.composicao.get(nutriente, 0) < necessidade:
                return False  # Polimorfismo: comportamento diferente dependendo dos objetos envolvidos
        return True


# Funções para a interface gráfica
def criar_aplicacao():
    try:
        # Obtém valores inseridos no formulário
        cultura_nome = cultura_entry.get()
        fertilizante_nome = fertilizante_entry.get()
        propriedade_nome = propriedade_entry.get()
        quantidade = float(quantidade_entry.get())
        data = data_entry.get()

        # Mock de objetos das classes (Instância de objetos, ou seja, criação de instâncias de classes)
        cultura = Cultura(cultura_nome, {"Nitrogênio": 10, "Fósforo": 5}, 10)  # Objeto da classe Cultura
        fertilizante = Fertilizante(fertilizante_nome, {"Nitrogênio": 15, "Fósforo": 10}, 50)  # Objeto da classe Fertilizante
        propriedade = Propriedade(propriedade_nome, "Localização X", Solo("Arenoso"))  # Objeto da classe Propriedade

        global aplicacao  # Objeto global da classe Aplicacao
        aplicacao = Aplicacao(cultura, fertilizante, propriedade, quantidade, data)  # Instância da classe Aplicacao

        messagebox.showinfo("Sucesso", "Aplicação criada com sucesso!")  # Exibe mensagem de sucesso
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")  # Exibe mensagem de erro

def exibir_resumo():
    if aplicacao:
        resumo = aplicacao.resumo()  # Chama o método da classe Aplicacao
        messagebox.showinfo("Resumo da Aplicação", resumo)  # Exibe o resumo
    else:
        messagebox.showwarning("Aviso", "Nenhuma aplicação criada ainda.")  # Caso não tenha aplicação

def verificar_viabilidade():
    if aplicacao:
        if aplicacao.verificar_viabilidade():  # Chama o método de verificação de viabilidade
            messagebox.showinfo("Viabilidade", "A aplicação é viável.")
        else:
            messagebox.showinfo("Viabilidade", "A aplicação não é viável.")
    else:
        messagebox.showwarning("Aviso", "Nenhuma aplicação criada ainda.")  # Caso não tenha aplicação


# Classes auxiliares (mock para a aplicação)

# Classe Cultura - Define o comportamento da cultura
class Cultura:
    def __init__(self, nome, necessidade, area):
        self.nome = nome  # Atributo da classe
        self.necessidade = necessidade  # Atributo da classe
        self.area = area  # Atributo da classe

# Classe Fertilizante - Define o comportamento do fertilizante
class Fertilizante:
    def __init__(self, nome, composicao, preco):
        self.nome = nome  # Atributo da classe
        self.composicao = composicao  # Atributo da classe
        self.preco = preco  # Atributo da classe

# Classe Propriedade - Define o comportamento da propriedade
class Propriedade:
    def __init__(self, nome, localizacao, solo):
        self.nome = nome  # Atributo da classe
        self.localizacao = localizacao  # Atributo da classe
        self.solo = solo  # Atributo da classe

# Classe Solo - Define o tipo de solo da propriedade
class Solo:
    def __init__(self, tipo):
        self.tipo = tipo  # Atributo da classe

# Interface gráfica
root = tk.Tk()
root.title("Gerenciador de Aplicações")
root.geometry("500x450")

aplicacao = None  # Inicializa o objeto global aplicacao como None

# Cabeçalho
header = tk.Frame(root, bg="#4CAF50", pady=10)
header.pack(fill="x")
tk.Label(header, text="Gerenciador de Aplicações", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white").pack()

# Container para entradas
container = tk.Frame(root, pady=10)
container.pack(expand=True)

# Entradas de dados
tk.Label(container, text="Cultura:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=10, pady=5)
cultura_entry = tk.Entry(container)
cultura_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(container, text="Fertilizante:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=10, pady=5)
fertilizante_entry = tk.Entry(container)
fertilizante_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(container, text="Propriedade:", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=10, pady=5)
propriedade_entry = tk.Entry(container)
propriedade_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(container, text="Quantidade (kg):", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=10, pady=5)
quantidade_entry = tk.Entry(container)
quantidade_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(container, text="Data (DD/MM/AAAA):", font=("Arial", 12)).grid(row=4, column=0, sticky="e", padx=10, pady=5)
data_entry = tk.Entry(container)
data_entry.grid(row=4, column=1, padx=10, pady=5)

# Botões
buttons = tk.Frame(root, pady=20)
buttons.pack()

tk.Button(buttons, text="Criar Aplicação", command=criar_aplicacao, font=("Arial", 12)).grid(row=0, column=0, padx=10)
tk.Button(buttons, text="Exibir Resumo", command=exibir_resumo, font=("Arial", 12)).grid(row=0, column=1, padx=10)
tk.Button(buttons, text="Verificar Viabilidade", command=verificar_viabilidade, font=("Arial", 12)).grid(row=0, column=2, padx=10)

root.mainloop()
