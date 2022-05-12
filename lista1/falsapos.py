import math

# Variaveis que o problema nos da
a = 2
b = 3
erro = 1e-7
results = [] # Pos 0: Iteracoes, Pos 1: |f(raiz)|

# Calcula a funcao
def funcao(x):
    retorno = (x * math.log10(x)) - 1
    return retorno

# Roda o metodo da falsa posicao
def fakePos(a, b, erro):
    if funcao(a) * funcao(b) < 0:
        temp = 0
        while True:
            temp += 1
            tent = (a*funcao(b) - b*funcao(a)) / (funcao(b) - funcao(a))
            if math.fabs(funcao(tent)) < erro:
                results.append(temp)
                results.append(math.fabs(funcao(tent)))
                return tent
            else:
                if funcao(a) * funcao(tent) < 0:
                    b = tent
                else:
                    a = tent
    else:
        print('Não existe raiz no intervalo dado')
        return

raiz = fakePos(a, b, erro)
print("Levou " + str(results[0]) + " iteracoes")
print("A raiz encontrada foi: " + str(raiz))
print("|f(raiz)| = " + str(results[1]))