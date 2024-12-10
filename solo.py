import tkinter as tk
from tkinter import messagebox


class Solo:
    def __init__(self, tipo, ph, nitrogenio, fosforo, potassio, calcio, magnesio, enxofre, ferro, manganes, zinco, cobre, boro, molibdenio):
        self._tipo = tipo
        self._ph = ph
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
        self._molibdenio = molibdenio

    # Propriedade para 'tipo'
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._tipo = valor
        else:
            raise ValueError("O tipo deve ser uma string não vazia.")

    # Propriedade para 'ph'
    @property
    def ph(self):
        return self._ph

    @ph.setter
    def ph(self, valor):
        if isinstance(valor, (int, float)) and 0 <= valor <= 14:
            self._ph = valor
        else:
            raise ValueError("O pH deve ser um número entre 0 e 14.")

    # Getter e Setter para nutrientes (sem restrição mínima de 1)
    @property
    def nitrogenio(self):
        return self._nitrogenio

    @nitrogenio.setter
    def nitrogenio(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:  # Aceita valores maiores ou iguais a 0, sem restrição mínima de 1
            self._nitrogenio = valor
        else:
            raise ValueError("O valor de Nitrogênio deve ser um número não negativo.")

    # Propriedades para os outros nutrientes (sem restrição mínima de 1)
    @property
    def fosforo(self):
        return self._fosforo

    @fosforo.setter
    def fosforo(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._fosforo = valor
        else:
            raise ValueError("O valor de Fósforo deve ser um número não negativo.")

    @property
    def potassio(self):
        return self._potassio

    @potassio.setter
    def potassio(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._potassio = valor
        else:
            raise ValueError("O valor de Potássio deve ser um número não negativo.")

    @property
    def calcio(self):
        return self._calcio

    @calcio.setter
    def calcio(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._calcio = valor
        else:
            raise ValueError("O valor de Cálcio deve ser um número não negativo.")

    @property
    def magnesio(self):
        return self._magnesio

    @magnesio.setter
    def magnesio(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._magnesio = valor
        else:
            raise ValueError("O valor de Magnésio deve ser um número não negativo.")

    @property
    def enxofre(self):
        return self._enxofre

    @enxofre.setter
    def enxofre(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._enxofre = valor
        else:
            raise ValueError("O valor de Enxofre deve ser um número não negativo.")

    @property
    def ferro(self):
        return self._ferro

    @ferro.setter
    def ferro(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._ferro = valor
        else:
            raise ValueError("O valor de Ferro deve ser um número não negativo.")

    @property
    def manganes(self):
        return self._manganes

    @manganes.setter
    def manganes(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._manganes = valor
        else:
            raise ValueError("O valor de Manganês deve ser um número não negativo.")

    @property
    def zinco(self):
        return self._zinco

    @zinco.setter
    def zinco(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._zinco = valor
        else:
            raise ValueError("O valor de Zinco deve ser um número não negativo.")

    @property
    def cobre(self):
        return self._cobre

    @cobre.setter
    def cobre(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._cobre = valor
        else:
            raise ValueError("O valor de Cobre deve ser um número não negativo.")

    @property
    def boro(self):
        return self._boro

    @boro.setter
    def boro(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._boro = valor
        else:
            raise ValueError("O valor de Boro deve ser um número não negativo.")

    @property
    def molibdenio(self):
        return self._molibdenio

    @molibdenio.setter
    def molibdenio(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._molibdenio = valor
        else:
            raise ValueError("O valor de Molibdênio deve ser um número não negativo.")

    def verificar_deficiencia(self):
        """Retorna nutrientes com níveis abaixo de 1%."""
        deficiencias = []
        atributos_nutrientes = [
            "nitrogenio", "fosforo", "potassio", "calcio", "magnesio", 
            "enxofre", "ferro", "manganes", "zinco", "cobre", "boro", "molibdenio"
        ]
        for nutriente in atributos_nutrientes:
            if getattr(self, nutriente) < 1:
                deficiencias.append(nutriente.capitalize())
        return deficiencias

    def atualizar_nutrientes(self, nutrientes):
        """Atualiza os níveis de nutrientes do solo com um dicionário de nutrientes fornecido."""
        for nutriente, valor in nutrientes.items():
            if hasattr(self, nutriente.lower()):
                setattr(self, nutriente.lower(), valor)
        return f"Nutrientes atualizados: {', '.join(nutrientes.keys())}"


# Funções para interação com a interface gráfica
def criar_solo():
    try:
        tipo = entries["Tipo"].get()
        ph = float(entries["PH"].get())
        nitrogenio = float(entries["Nitrogênio"].get())
        fosforo = float(entries["Fósforo"].get())
        potassio = float(entries["Potássio"].get())
        calcio = float(entries["Cálcio"].get())
        magnesio = float(entries["Magnésio"].get())
        enxofre = float(entries["Enxofre"].get())
        ferro = float(entries["Ferro"].get())
        manganes = float(entries["Manganês"].get())
        zinco = float(entries["Zinco"].get())
        cobre = float(entries["Cobre"].get())
        boro = float(entries["Boro"].get())
        molibdenio = float(entries["Molibdênio"].get())

        global solo
        solo = Solo(tipo, ph, nitrogenio, fosforo, potassio, calcio, magnesio, enxofre, ferro, manganes, zinco, cobre, boro, molibdenio)
        messagebox.showinfo("Sucesso", "Solo criado com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para os dados.")


def verificar_deficiencia():
    if solo:
        deficiencias = solo.verificar_deficiencia()
        if deficiencias:
            messagebox.showinfo("Deficiências", f"Nutrientes deficientes: {', '.join(deficiencias)}")
        else:
            messagebox.showinfo("Deficiências", "Não há deficiências detectadas.")
    else:
        messagebox.showwarning("Aviso", "Nenhum solo criado ainda.")


def abrir_atualizar_nutrientes():
    if solo:
        atualizar_window = tk.Toplevel(root)
        atualizar_window.title("Atualizar Nutrientes")
        atualizar_window.geometry("400x300")

        nutrientes = ["Nitrogênio", "Fósforo", "Potássio", "Magnésio"]
        atualizar_entries = {}

        for i, nutriente in enumerate(nutrientes):
            tk.Label(atualizar_window, text=nutriente, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(atualizar_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            atualizar_entries[nutriente] = entry

        def atualizar():
            try:
                novos_nutrientes = {n: float(atualizar_entries[n].get()) for n in atualizar_entries}
                resultado = solo.atualizar_nutrientes(novos_nutrientes)
                messagebox.showinfo("Atualização", resultado)
                atualizar_window.destroy()
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira valores válidos.")

        tk.Button(atualizar_window, text="Atualizar", command=atualizar).grid(row=len(nutrientes), columnspan=2, pady=10)
    else:
        messagebox.showwarning("Aviso", "Nenhum solo criado ainda.")


# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Gerenciador de Solo")
root.geometry("600x700")

# Cabeçalho
header = tk.Frame(root, bg="#4CAF50", height=60)
header.pack(fill=tk.X)
title_label = tk.Label(header, text="Gerenciador de Solo", font=("Arial", 20, "bold"), bg="#4CAF50", fg="white")
title_label.pack(pady=15)

solo = None

# Entradas para os dados do solo
container = tk.Frame(root, pady=20)
container.pack(expand=True)

labels = [
    "Tipo", "PH", "Nitrogênio", "Fósforo", "Potássio", "Cálcio", "Magnésio", "Enxofre", "Ferro", "Manganês",
    "Zinco", "Cobre", "Boro", "Molibdênio"
]
entries = {}
for i, label_text in enumerate(labels):
    tk.Label(container, text=label_text, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(container)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label_text] = entry

# Botões
buttons = tk.Frame(root)
buttons.pack(pady=20)

tk.Button(buttons, text="Criar Solo", command=criar_solo).grid(row=0, column=0, padx=10)
tk.Button(buttons, text="Verificar Deficiência", command=verificar_deficiencia).grid(row=0, column=1, padx=10)
tk.Button(buttons, text="Atualizar Nutrientes", command=abrir_atualizar_nutrientes).grid(row=0, column=2, padx=10)

root.mainloop()
