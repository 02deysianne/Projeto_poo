import tkinter as tk
from tkinter import messagebox

# Classe da Cultura
class Cultura:
    def __init__(self, nome, necessidade, area):
        self.nome = nome  # Atributo público para armazenar o nome da cultura
        self.necessidade = necessidade  # Dicionário que armazena as necessidades nutricionais da cultura
        self.area = area  # Atributo para armazenar a área da cultura

    def calcular_demanda(self):
        """Calcula a demanda nutricional com base na área."""  # Método para calcular a demanda nutricional
        demanda = {nutriente: valor * self.area for nutriente, valor in self.necessidade.items()}  # Calcula a demanda por nutriente
        return demanda  # Retorna o dicionário com as demandas por área

    def verificar_suficiencia(self, solo):
        """Verifica se o solo atende às necessidades da cultura."""  # Método para verificar a suficiência do solo
        insuficientes = []  # Lista que armazenará os nutrientes insuficientes
        for nutriente, valor in self.necessidade.items():  # Itera pelas necessidades nutricionais
            if hasattr(solo, nutriente.lower()):  # Verifica se o solo tem o atributo referente ao nutriente
                nivel_solo = getattr(solo, nutriente.lower())  # Obtém o nível de nutriente no solo
                if nivel_solo < valor:  # Verifica se o nível do solo é inferior à necessidade
                    insuficientes.append(nutriente)  # Adiciona o nutriente à lista de insuficientes
        return insuficientes  # Retorna a lista de nutrientes insuficientes

# Funções para a interface gráfica
def criar_cultura():
    try:
        nome = nome_entry.get()  # Obtém o nome da cultura inserido pelo usuário
        area = float(area_entry.get())  # Obtém a área da cultura convertida para float

        # Coleta as necessidades nutricionais com base nas opções selecionadas
        necessidade = {}  # Dicionário para armazenar as necessidades nutricionais
        if nitrogenio_var.get():  # Verifica se o usuário selecionou Nitrogênio
            necessidade["Nitrogênio"] = float(nitrogenio_cultura_entry.get())  # Adiciona a necessidade de Nitrogênio
        if fosforo_var.get():  # Verifica se o usuário selecionou Fósforo
            necessidade["Fósforo"] = float(fosforo_cultura_entry.get())  # Adiciona a necessidade de Fósforo
        if potassio_var.get():  # Verifica se o usuário selecionou Potássio
            necessidade["Potássio"] = float(potassio_cultura_entry.get())  # Adiciona a necessidade de Potássio
        if calcio_var.get():  # Verifica se o usuário selecionou Cálcio
            necessidade["Cálcio"] = float(calcio_cultura_entry.get())  # Adiciona a necessidade de Cálcio
        if magnesio_var.get():  # Verifica se o usuário selecionou Magnésio
            necessidade["Magnésio"] = float(magnesio_cultura_entry.get())  # Adiciona a necessidade de Magnésio
        if enxofre_var.get():  # Verifica se o usuário selecionou Enxofre
            necessidade["Enxofre"] = float(enxofre_cultura_entry.get())  # Adiciona a necessidade de Enxofre
        if ferro_var.get():  # Verifica se o usuário selecionou Ferro
            necessidade["Ferro"] = float(ferro_cultura_entry.get())  # Adiciona a necessidade de Ferro
        if manganes_var.get():  # Verifica se o usuário selecionou Manganês
            necessidade["Manganês"] = float(manganes_cultura_entry.get())  # Adiciona a necessidade de Manganês
        if zinco_var.get():  # Verifica se o usuário selecionou Zinco
            necessidade["Zinco"] = float(zinco_cultura_entry.get())  # Adiciona a necessidade de Zinco
        if cobre_var.get():  # Verifica se o usuário selecionou Cobre
            necessidade["Cobre"] = float(cobre_cultura_entry.get())  # Adiciona a necessidade de Cobre
        if boro_var.get():  # Verifica se o usuário selecionou Boro
            necessidade["Boro"] = float(boro_cultura_entry.get())  # Adiciona a necessidade de Boro

        global cultura  # Declara a variável cultura globalmente
        cultura = Cultura(nome, necessidade, area)  # Cria a instância da classe Cultura com os dados coletados

        messagebox.showinfo("Sucesso", "Cultura criada com sucesso!")  # Exibe mensagem de sucesso
    except ValueError:  # Caso ocorra erro na conversão dos dados
        messagebox.showerror("Erro", "Por favor, insira valores válidos para os dados.")  # Exibe mensagem de erro

def calcular_demanda():
    if cultura:  # Verifica se a cultura foi criada
        demanda = cultura.calcular_demanda()  # Calcula a demanda nutricional com base na cultura
        demanda_str = "\n".join([f"{nutriente}: {valor}" for nutriente, valor in demanda.items()])  # Formata a demanda para exibição
        messagebox.showinfo("Demanda Nutricional", f"Demanda por área:\n{demanda_str}")  # Exibe a demanda nutricional
    else:
        messagebox.showwarning("Aviso", "Nenhuma cultura criada ainda.")  # Exibe mensagem de aviso caso a cultura não tenha sido criada

def verificar_suficiencia():
    if cultura:  # Verifica se a cultura foi criada
        if solo:  # Verifica se o solo foi criado
            insuficientes = cultura.verificar_suficiencia(solo)  # Verifica os nutrientes insuficientes no solo
            if insuficientes:  # Se houver nutrientes insuficientes
                messagebox.showinfo("Nutrientes Insuficientes", f"Solo insuficiente em: {', '.join(insuficientes)}")  # Exibe quais nutrientes estão insuficientes
            else:
                messagebox.showinfo("Suficiência", "O solo atende às necessidades da cultura.")  # Exibe mensagem de suficiência
        else:
            messagebox.showwarning("Aviso", "Nenhum solo criado ainda.")  # Exibe mensagem de aviso caso o solo não tenha sido criado
    else:
        messagebox.showwarning("Aviso", "Nenhuma cultura criada ainda.")  # Exibe mensagem de aviso caso a cultura não tenha sido criada

# Interface gráfica com Tkinter
root = tk.Tk()  # Cria a janela principal
root.title("Gerenciador de Cultura")  # Define o título da janela
root.geometry("600x800")  # Define o tamanho da janela

# Cabeçalho
header = tk.Frame(root, bg="#4CAF50", height=60)  # Cria um frame para o cabeçalho
header.pack(fill=tk.X)  # Preenche a largura da janela com o cabeçalho
title_label = tk.Label(header, text="Gerenciador de Cultura", font=("Arial", 20, "bold"), bg="#4CAF50", fg="white")  # Cria o título
title_label.pack(pady=15)  # Adiciona o título no cabeçalho

cultura = None  # Inicializa a variável cultura como None
solo = None  # Inicializa a variável solo como None

# Entradas para os dados da cultura
container = tk.Frame(root, pady=20)  # Cria um container para os campos de entrada
container.pack(expand=True)  # Expande o container

# Labels e Entries para o nome da cultura e área
tk.Label(container, text="Nome da Cultura", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)  # Label para nome
nome_entry = tk.Entry(container)  # Entry para o nome da cultura
nome_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(container, text="Área (hectares)", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)  # Label para a área
area_entry = tk.Entry(container)  # Entry para a área
area_entry.grid(row=1, column=1, padx=10, pady=5)

# Checkboxes para marcar as necessidades nutricionais
tk.Label(container, text="Necessidades Nutricionais", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, columnspan=2)  # Título para as necessidades nutricionais

# Variáveis para os checkboxes
nitrogenio_var = tk.BooleanVar()  # Variável para Nitrogênio
fosforo_var = tk.BooleanVar()  # Variável para Fósforo
potassio_var = tk.BooleanVar()  # Variável para Potássio
calcio_var = tk.BooleanVar()  # Variável para Cálcio
magnesio_var = tk.BooleanVar()  # Variável para Magnésio
enxofre_var = tk.BooleanVar()  # Variável para Enxofre
ferro_var = tk.BooleanVar()  # Variável para Ferro
manganes_var = tk.BooleanVar()  # Variável para Manganês
zinco_var = tk.BooleanVar()  # Variável para Zinco
cobre_var = tk.BooleanVar()  # Variável para Cobre
boro_var = tk.BooleanVar()  # Variável para Boro

# Checkboxes
tk.Checkbutton(container, text="Nitrogênio", variable=nitrogenio_var).grid(row=3, column=0, padx=10, pady=5, sticky="w")  # Checkbox para Nitrogênio
tk.Checkbutton(container, text="Fósforo", variable=fosforo_var).grid(row=4, column=0, padx=10, pady=5, sticky="w")  # Checkbox para Fósforo
tk.Checkbutton(container, text="Potássio", variable=potassio_var).grid(row=5, column=0, padx=10, pady=5, sticky="w")  # Checkbox para Potássio
tk.Checkbutton(container, text="Cálcio", variable=calcio_var).grid(row=6, column=0, padx=10, pady=5, sticky="w")  # Checkbox para Cálcio
tk.Checkbutton(container, text="Magnésio", variable=magnesio_var).grid(row=7, column=0, padx=10, pady=5, sticky="w")  # Checkbox para Magnésio
tk.Checkbutton(container, text="Enxofre", variable=enxofre_var).grid(row=8, column=0, padx=10, pady=5, sticky="w")  # Checkbox para Enxofre
tk.Checkbutton(container, text="Ferro", variable=ferro_var).grid(row=9, column=0, padx=10, pady=5, sticky="w")  # Checkbox para Ferro
tk.Checkbutton(container, text="Manganês", variable=manganes_var).grid(row=10, column=0, padx=10, pady=5, sticky="w")  # Checkbox para Manganês
tk.Checkbutton(container, text="Zinco", variable=zinco_var).grid(row=11, column=0, padx=10, pady=5, sticky="w")  # Checkbox para Zinco
tk.Checkbutton(container, text="Cobre", variable=cobre_var).grid(row=12, column=0, padx=10, pady=5, sticky="w")  # Checkbox para Cobre
tk.Checkbutton(container, text="Boro", variable=boro_var).grid(row=13, column=0, padx=10, pady=5, sticky="w")  # Checkbox para Boro

# Entradas para as necessidades nutricionais
nitrogenio_cultura_entry = tk.Entry(container)  # Entry para Nitrogênio
nitrogenio_cultura_entry.grid(row=3, column=1, padx=10, pady=5)  # Grid para Nitrogênio
fosforo_cultura_entry = tk.Entry(container)  # Entry para Fósforo
fosforo_cultura_entry.grid(row=4, column=1, padx=10, pady=5)  # Grid para Fósforo
potassio_cultura_entry = tk.Entry(container)  # Entry para Potássio
potassio_cultura_entry.grid(row=5, column=1, padx=10, pady=5)  # Grid para Potássio
calcio_cultura_entry = tk.Entry(container)  # Entry para Cálcio
calcio_cultura_entry.grid(row=6, column=1, padx=10, pady=5)  # Grid para Cálcio
magnesio_cultura_entry = tk.Entry(container)  # Entry para Magnésio
magnesio_cultura_entry.grid(row=7, column=1, padx=10, pady=5)  # Grid para Magnésio
enxofre_cultura_entry = tk.Entry(container)  # Entry para Enxofre
enxofre_cultura_entry.grid(row=8, column=1, padx=10, pady=5)  # Grid para Enxofre
ferro_cultura_entry = tk.Entry(container)  # Entry para Ferro
ferro_cultura_entry.grid(row=9, column=1, padx=10, pady=5)  # Grid para Ferro
manganes_cultura_entry = tk.Entry(container)  # Entry para Manganês
manganes_cultura_entry.grid(row=10, column=1, padx=10, pady=5)  # Grid para Manganês
zinco_cultura_entry = tk.Entry(container)  # Entry para Zinco
zinco_cultura_entry.grid(row=11, column=1, padx=10, pady=5)  # Grid para Zinco
cobre_cultura_entry = tk.Entry(container)  # Entry para Cobre
cobre_cultura_entry.grid(row=12, column=1, padx=10, pady=5)  # Grid para Cobre
boro_cultura_entry = tk.Entry(container)  # Entry para Boro
boro_cultura_entry.grid(row=13, column=1, padx=10, pady=5)  # Grid para Boro

# Botões para as funcionalidades
button_frame = tk.Frame(root)  # Frame para os botões
button_frame.pack(pady=20)  # Adiciona o frame dos botões

# Botões para criar a cultura, calcular demanda e verificar suficiência
tk.Button(button_frame, text="Criar Cultura", command=criar_cultura).grid(row=0, column=0, padx=10)  # Botão para criar cultura
tk.Button(button_frame, text="Calcular Demanda", command=calcular_demanda).grid(row=0, column=1, padx=10)  # Botão para calcular demanda
tk.Button(button_frame, text="Verificar Suficiência", command=verificar_suficiencia).grid(row=0, column=2, padx=10)  # Botão para verificar suficiência

# Inicia a interface gráfica
root.mainloop()
