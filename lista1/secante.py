import math
import numpy as np

# Variaveis que o problema nos da
a = 2
b = 3
erro = 1e-7
results = [] # Pos 0: Iteracoes, Pos 1: |f(raiz)|

# Calcula a funcao
def funcao(x):
    retorno = (x * (math.log10(x))) - 1
    return retorno

# Calcula a derivada
def derivada(x):
    deriv = math.log10(x) + 1 / np.log(10)
    return deriv

# Roda o metodo da secante
def secante(x_0, x_1, erro):
    temp = 0
    if math.fabs(funcao(x_0)) <= erro:
        return x_0
    if math.fabs(funcao(x_1)) <= erro:
        return x_1
    while True:
        temp += 1
        x_2 = x_1 - funcao(x_1) * ((x_1 - x_0) / (funcao(x_1) - funcao(x_0)))
        if math.fabs(funcao(abs(x_2))) <= erro:
            results.append(temp)
            results.append(math.fabs(funcao(x_2)))
            return x_2
        x_0 = x_1
        x_1 = x_2

raiz = secante(a, b, erro)
print("Levou " + str(results[0]) + " iteracoes")
print("A raiz encontrada foi: " + str(raiz))
print("|f(raiz)| = " + str(results[1]))