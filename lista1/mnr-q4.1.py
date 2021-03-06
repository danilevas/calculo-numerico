import math
import numpy as np

# Variaveis que o problema nos da
a = 2
b = 3
x_0 = 2
erro = 1e-7
results = [] # Pos 0: Iteracoes, Pos 1: |f(raiz)|

# Calcula a funcao
def funcao(x):
    retorno = (x * math.log10(x)) - 1
    return retorno

# Calcula a derivada
def derivada(x):
    deriv = math.log10(x) + 1 / np.log(10)
    return deriv

# Roda o metodo de Newton-Raphson
def newton_raphson(x_0, erro):
    x = x_0
    temp = 0
    while True:
        temp += 1
        x_subs = x - (funcao(x) / derivada(x_0))
        if math.fabs(funcao(x_subs)) <= erro:
            results.append(temp)
            results.append(math.fabs(funcao(x_subs)))
            return x_subs
        x = x_subs

raiz = newton_raphson(x_0, erro)
print("Levou " + str(results[0]) + " iteracoes")
print("A raiz encontrada foi: " + str(raiz))
print("|f(raiz)| = " + str(results[1]))