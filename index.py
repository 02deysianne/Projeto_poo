import tkinter as tk
import subprocess

# Funções para redirecionar para os arquivos Python
def abrir_cadastro_propriedade():
    subprocess.Popen(["python", "propriedade.py"])  # Abre a página do cadastro de solo

def abrir_cadastro_solo():
    subprocess.Popen(["python", "solo.py"])  # Abre a página do cadastro de cultura

def abrir_cadastro_cultura():
    subprocess.Popen(["python", "cultura.py"])  # Abre a página do cadastro de propriedade

def abrir_cadastro_fertilizantes():
    subprocess.Popen(["python", "fertilizantes.py"])  # Abre a página do cadastro de aplicação

def abrir_cadastro_aplicacao():
    subprocess.Popen(["python", "aplicacao.py"])  # Abre a página do cadastro de fertilizante

# Função para a tela principal
def tela_principal():
    # Janela principal
    root = tk.Tk()
    root.title("Página Principal")
    root.geometry("400x350")

    # Define cor de fundo para a janela principal
    root.configure(bg="#D9EEDB")  

    # Cabeçalho
    titulo_frame = tk.Frame(root, bg="#553d2a", height=60)  
    titulo_frame.pack(fill=tk.X)

    titulo = tk.Label(
        titulo_frame,
        text="Selecione o que deseja cadastrar",
        font=("Arial", 16, "bold"),
        fg="white",  # Texto branco
        bg="#553d2a"  # Fundo igual ao frame
    )
    titulo.pack(pady=15)

    # Botões para escolher qual cadastro fazer
    botao_solo = tk.Button(root, text="Cadastro de Propriedade", width=20, command=abrir_cadastro_propriedade, bg="#553d2a", fg="white")
    botao_solo.pack(pady=10)

    botao_cultura = tk.Button(root, text="Cadastro de Solo", width=20, command=abrir_cadastro_solo, bg="#553d2a", fg="white")
    botao_cultura.pack(pady=10)

    botao_propriedade = tk.Button(root, text="Cadastro de Cultura", width=20, command=abrir_cadastro_cultura, bg="#553d2a", fg="white")
    botao_propriedade.pack(pady=10)

    botao_aplicacao = tk.Button(root, text="Cadastro de Fertilizante", width=20, command=abrir_cadastro_fertilizantes, bg="#553d2a", fg="white")
    botao_aplicacao.pack(pady=10)

    botao_fertilizante = tk.Button(root, text="Cadastro de Aplicação", width=20, command=abrir_cadastro_aplicacao, bg="#553d2a", fg="white")
    botao_fertilizante.pack(pady=10)

    # Iniciar o loop principal da interface gráfica
    root.mainloop()

# Chama a tela principal ao rodar o programa
if __name__ == "__main__":
    tela_principal()
