# Controlando a quantidade de argumentos posicionas e nomeados em funcoes
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positiona-only Parameters (/) - Tudo antes da barra deve ser ❗APENAS❗ posicional.
# PEP 570 - Python Positional-Only Parameters

# 🟢 Keyword-Only Arguments (*) - * sozinho ❗ nao suga ❗ valores.

def soma(a, b, /):  # bloquei tudo que vier antes da barra de vier como parametro nomeado
    print(sum(a, b))


def soma2(a, b,  *, c):
    print(a + b + c)


# soma(1, 3)
soma2(1, 2, c=3)  # dps do *  todos os parametros devem ser nomeados
