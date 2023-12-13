import tkinter as tk

def calcular():
    try:
        first_number = int(entry_first.get())
        second_number = int(entry_second.get())
        operador = operator_var.get()

        if operador == '+':
            resultado.set(f'{first_number} + {second_number} = {first_number + second_number}')
        elif operador == '*':
            resultado.set(f'{first_number} * {second_number} = {first_number * second_number}')
        elif operador == '-':
            resultado.set(f'{first_number} - {second_number} = {first_number - second_number}')
        elif operador == '/':
            resultado.set(f'{first_number} / {second_number} = {first_number / second_number}')
        elif operador == '**':
            resultado.set(f'{first_number} ** {second_number} = {first_number ** second_number}')

    except ValueError:
        resultado.set('Erro nos números')

# Criar a janela principal
janela = tk.Tk()
janela.title('Calculadora dos FOdoes')

# Criar variáveis para os números e o resultado
entry_first = tk.Entry(janela)
entry_second = tk.Entry(janela)
resultado = tk.StringVar()

# Criar variável para o operador
operator_var = tk.StringVar()
operator_var.set('+')

# Criar widgets
label_first = tk.Label(janela, text='Digite o primeiro número:')
label_second = tk.Label(janela, text='Digite o segundo número:')
label_operator = tk.Label(janela, text='Escolha o operador:')
label_resultado = tk.Label(janela, textvariable=resultado)

button_calcular = tk.Button(janela, text='Calcular', command=calcular)

option_menu = tk.OptionMenu(janela, operator_var, '+', '*', '-', '/', '**')

# Posicionar widgets na janela
label_first.grid(row=0, column=0)
entry_first.grid(row=0, column=1)
label_second.grid(row=1, column=0)
entry_second.grid(row=1, column=1)
label_operator.grid(row=2, column=0)
option_menu.grid(row=2, column=1)
button_calcular.grid(row=3, column=0, columnspan=2)
label_resultado.grid(row=4, column=0, columnspan=2)

# Iniciar a janela
janela.mainloop()
