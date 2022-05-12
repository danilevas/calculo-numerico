import math

# Variaveis que o problema nos da
a = 2
b = 3
erro = 1e-7

# Calcula a funcao
def funcao(x):
    retorno = (x * math.log10(x)) - 1
    return retorno

# Roda o metodo da bissecao
def bissecao(a, b, erro):
    temp = 0
    if funcao(a)*funcao(b) < 0: # Testando para ver se há raiz entre a e b
        while math.fabs(b-a)/2 > erro:
            temp += 1
            x = (a + b) / 2
            if funcao(x) == 0:
                print('A raiz eh: ', x)
                return x
            else:
                if funcao(a)*funcao(x) < 0: # Testando para ver se há raiz entre a e x ou b e x
                    b = x
                else:
                    a = x
        fx = math.fabs(funcao(x))
        print("Levou " + str(temp) + " iteracoes")
        print("A raiz encontrada foi: " + str(x))
        print("|f(raiz)| = " + str(fx))
        return
    else:
        print('Não existe raiz no intervalo dado')
        return
    
raiz = bissecao(a, b, erro)