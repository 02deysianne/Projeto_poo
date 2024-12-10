import tkinter as tk
from tkinter import messagebox

# Classe que representa um fertilizante
class Fertilizante:
    def __init__(self, nome, tipo, nitrogenio, fosforo, potassio, calcio, magnesio, enxofre, ferro, manganes, zinco, cobre, boro, preco):
        # Inicializa os atributos do fertilizante
        self._nome = nome
        self._tipo = tipo
        self._nitrogenio = nitrogenio
        self._fosforo = fosforo
        self._potassio = potassio
        self._calcio = calcio
        self._magnesio = magnesio
        self._enxofre = enxofre
        self._ferro = ferro
        self._manganes = manganes
        self._zinco = zinco
        self._cobre = cobre
        self._boro = boro
        self._preco = preco

    # Getters e setters para acesso aos atributos privados
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value):
        self._preco = value

    # Método que retorna uma string com os detalhes do fertilizante
    def detalhes(self):
        return (
            f"Nome: {self.nome}\n"
            f"Tipo: {self.tipo}\n"
            f"Nutrientes (%):\n"
            f"  Nitrogênio: {self._nitrogenio}%, Fósforo: {self._fosforo}%, Potássio: {self._potassio}%\n"
            f"  Cálcio: {self._calcio}%, Magnésio: {self._magnesio}%, Enxofre: {self._enxofre}%\n"
            f"  Ferro: {self._ferro}%, Manganês: {self._manganes}%, Zinco: {self._zinco}%\n"
            f"  Cobre: {self._cobre}%, Boro: {self._boro}%\n"
            f"Preço: R$ {self._preco:.2f}"
        )

    # Método que calcula os nutrientes totais de acordo com a quantidade fornecida
    def calcular_nutrientes_totais(self, quantidade):
        return {
            "Nitrogênio": self._nitrogenio * quantidade / 100,
            "Fósforo": self._fosforo * quantidade / 100,
            "Potássio": self._potassio * quantidade / 100,
            "Cálcio": self._calcio * quantidade / 100,
            "Magnésio": self._magnesio * quantidade / 100,
            "Enxofre": self._enxofre * quantidade / 100,
            "Ferro": self._ferro * quantidade / 100,
            "Manganês": self._manganes * quantidade / 100,
            "Zinco": self._zinco * quantidade / 100,
            "Cobre": self._cobre * quantidade / 100,
            "Boro": self._boro * quantidade / 100,
        }


# Função para criar um fertilizante a partir dos dados inseridos pelo usuário
def criar_fertilizante():
    try:
        # Obtém os valores das entradas e cria um objeto Fertilizante
        nome = nome_entry.get()
        tipo = tipo_entry.get()
        nitrogenio = float(nitrogenio_entry.get())
        fosforo = float(fosforo_entry.get())
        potassio = float(potassio_entry.get())
        calcio = float(calcio_entry.get())
        magnesio = float(magnesio_entry.get())
        enxofre = float(enxofre_entry.get())
        ferro = float(ferro_entry.get())
        manganes = float(manganes_entry.get())
        zinco = float(zinco_entry.get())
        cobre = float(cobre_entry.get())
        boro = float(boro_entry.get())
        preco = float(preco_entry.get())

        # Cria uma instância do fertilizante com os valores fornecidos
        global fertilizante
        fertilizante = Fertilizante(nome, tipo, nitrogenio, fosforo, potassio, calcio, magnesio, enxofre, ferro,
                                    manganes, zinco, cobre, boro, preco)

        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Fertilizante criado com sucesso!")
    except ValueError:
        # Exibe um erro caso o usuário insira valores inválidos
        messagebox.showerror("Erro", "Por favor, insira valores válidos para os nutrientes e o preço.")


# Função para exibir os detalhes do fertilizante criado
def exibir_detalhes():
    if fertilizante:
        # Exibe os detalhes do fertilizante em uma caixa de mensagem
        detalhes = fertilizante.detalhes()
        messagebox.showinfo("Detalhes do Fertilizante", detalhes)
    else:
        # Exibe uma mensagem de aviso se nenhum fertilizante tiver sido criado
        messagebox.showwarning("Aviso", "Nenhum fertilizante criado ainda.")


# Função para calcular os nutrientes totais para uma quantidade específica
def calcular_nutrientes():
    if fertilizante:
        try:
            # Obtém a quantidade inserida pelo usuário e calcula os nutrientes totais
            quantidade = float(quantidade_entry.get())
            totais = fertilizante.calcular_nutrientes_totais(quantidade)
            # Exibe o resultado formatado
            resultado = "\n".join([f"{k}: {v:.2f} kg" for k, v in totais.items()])
            messagebox.showinfo("Nutrientes Totais", f"Nutrientes para {quantidade} kg:\n\n{resultado}")
        except ValueError:
            # Exibe um erro caso o usuário insira uma quantidade inválida
            messagebox.showerror("Erro", "Por favor, insira uma quantidade válida.")
    else:
        # Exibe uma mensagem de aviso se nenhum fertilizante tiver sido criado
        messagebox.showwarning("Aviso", "Nenhum fertilizante criado ainda.")


# Interface gráfica
root = tk.Tk()
root.title("Gerenciador de Fertilizantes")
root.geometry("800x600")

# Variável global para armazenar o fertilizante
fertilizante = None

# Cabeçalho da interface
header = tk.Frame(root, bg="#4CAF50", height=50)
header.pack(fill=tk.X, side=tk.TOP)

# Título do aplicativo
title_label = tk.Label(header, text="Gerenciador de Fertilizantes", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white")
title_label.pack(side=tk.TOP)

# Container para as entradas
container = tk.Frame(root, pady=20)
container.pack(expand=True)

# Dicionário de entradas
entries = {
    "Nome": None,
    "Tipo": None,
    "Nitrogênio (%)": None,
    "Fósforo (%)": None,
    "Potássio (%)": None,
    "Cálcio (%)": None,
    "Magnésio (%)": None,
    "Enxofre (%)": None,
    "Ferro (%)": None,
    "Manganês (%)": None,
    "Zinco (%)": None,
    "Cobre (%)": None,
    "Boro (%)": None,
    "Preço": None,
    "Quantidade (kg)": None,
}

# Cria as entradas de dados
for i, (label_text, entry_var) in enumerate(entries.items()):
    tk.Label(container, text=label_text, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
    entry_var = tk.Entry(container)
    entry_var.grid(row=i, column=1, padx=10, pady=5)
    entries[label_text] = entry_var

# Atribuindo as variáveis de entrada a cada campo
nome_entry = entries["Nome"]
tipo_entry = entries["Tipo"]
nitrogenio_entry = entries["Nitrogênio (%)"]
fosforo_entry = entries["Fósforo (%)"]
potassio_entry = entries["Potássio (%)"]
calcio_entry = entries["Cálcio (%)"]
magnesio_entry = entries["Magnésio (%)"]
enxofre_entry = entries["Enxofre (%)"]
ferro_entry = entries["Ferro (%)"]
manganes_entry = entries["Manganês (%)"]
zinco_entry = entries["Zinco (%)"]
cobre_entry = entries["Cobre (%)"]
boro_entry = entries["Boro (%)"]
preco_entry = entries["Preço"]
quantidade_entry = entries["Quantidade (kg)"]

# Criação dos botões para ações
buttons = tk.Frame(root)
buttons.pack(pady=20)

# Botões para criar fertilizante, exibir detalhes e calcular nutrientes
tk.Button(buttons, text="Criar Fertilizante", command=criar_fertilizante).grid(row=0, column=0, padx=10)
tk.Button(buttons, text="Exibir Detalhes", command=exibir_detalhes).grid(row=0, column=1, padx=10)
tk.Button(buttons, text="Calcular Nutrientes", command=calcular_nutrientes).grid(row=0, column=2, padx=10)

# Inicia a interface gráfica
root.mainloop()
