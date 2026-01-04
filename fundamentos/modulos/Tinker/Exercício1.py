import tkinter as tk
from tkinter import messagebox


def comparar_numeros():
    try:
        # Pega os valores digitados
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())

        # Faz a comparação
        if num1 > num2:
            resultado = f"{num1} é MAIOR que {num2}"
            cor = "#4CAF50"  # Verde
            simbolo = ">"
        elif num1 < num2:
            resultado = f"{num1} é MENOR que {num2}"
            cor = "#FF5722"  # Vermelho
            simbolo = "<"
        else:
            resultado = f"{num1} é IGUAL a {num2}"
            cor = "#2196F3"  # Azul
            simbolo = "="

        # Exibe o resultado
        label_resultado.config(text=resultado, fg=cor, font=("Arial", 14, "bold"))
        label_simbolo.config(text=simbolo, fg=cor, font=("Arial", 40, "bold"))

    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite apenas números válidos!")
        limpar_campos()


def limpar_campos():
    entrada_num1.delete(0, tk.END)
    entrada_num2.delete(0, tk.END)
    label_resultado.config(text="")
    label_simbolo.config(text="")
    entrada_num1.focus()


# Criar a janela principal
janela = tk.Tk()
janela.title("Comparador de Números")
janela.geometry("400x450")
janela.resizable(False, False)
janela.config(bg="#f0f0f0")

# Título
titulo = tk.Label(
    janela,
    text=" Comparador de Números",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="#333"
)
titulo.pack(pady=20)

# Frame para os campos de entrada
frame_entradas = tk.Frame(janela, bg="#f0f0f0")
frame_entradas.pack(pady=10)

# Primeiro número
label_num1 = tk.Label(
    frame_entradas,
    text="Primeiro número:",
    font=("Arial", 12),
    bg="#f0f0f0"
)
label_num1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entrada_num1 = tk.Entry(
    frame_entradas,
    font=("Arial", 14),
    width=15,
    justify="center",
    relief="solid",
    bd=2
)
entrada_num1.grid(row=0, column=1, padx=10, pady=10)
entrada_num1.focus()

# Segundo número
label_num2 = tk.Label(
    frame_entradas,
    text="Segundo número:",
    font=("Arial", 12),
    bg="#f0f0f0"
)
label_num2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entrada_num2 = tk.Entry(
    frame_entradas,
    font=("Arial", 14),
    width=15,
    justify="center",
    relief="solid",
    bd=2
)
entrada_num2.grid(row=1, column=1, padx=10, pady=10)

# Frame para os botões
frame_botoes = tk.Frame(janela, bg="#f0f0f0")
frame_botoes.pack(pady=15)

# Botão Comparar
botao_comparar = tk.Button(
    frame_botoes,
    text="⚖️ Comparar",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=12,
    height=2,
    relief="raised",
    bd=3,
    cursor="hand2",
    command=comparar_numeros
)
botao_comparar.grid(row=0, column=0, padx=10)

# Botão Limpar
botao_limpar = tk.Button(
    frame_botoes,
    text="🗑️ Limpar",
    font=("Arial", 12, "bold"),
    bg="#FF9800",
    fg="white",
    width=12,
    height=2,
    relief="raised",
    bd=3,
    cursor="hand2",
    command=limpar_campos
)
botao_limpar.grid(row=0, column=1, padx=10)

# Área de resultado - Símbolo
label_simbolo = tk.Label(
    janela,
    text="",
    font=("Arial", 40, "bold"),
    bg="#f0f0f0"
)
label_simbolo.pack(pady=10)

# Área de resultado - Texto
label_resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 14, "bold"),
    bg="#f0f0f0",
    wraplength=350
)
label_resultado.pack(pady=10)

# Permitir tecla Enter para comparar
entrada_num1.bind("<Return>", lambda event: entrada_num2.focus())
entrada_num2.bind("<Return>", lambda event: comparar_numeros()) 