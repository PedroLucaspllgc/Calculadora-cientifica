import math

def calcular(expressao):
    expressao = expressao.replace('+','+')
    expressao = expressao.replace('-', '-')
    expressao = expressao.replace('x', '*')
    expressao = expressao.replace('/', '/')
    expressao = expressao.replace('^', '**')
    expressao = expressao.replace('yx', '**')
    expressao = expressao.replace('√', 'math.sqrt')
    expressao = expressao.replace('ex', 'math.exp')
    expressao = expressao.replace('sin', 'math.sin')
    expressao = expressao.replace('cos', 'math.cos')
    expressao = expressao.replace('tan', 'math.tan')
    expressao = expressao.replace('π', 'math.pi')
    
    try:
        resultado = eval(expressao)
        return resultado
    except Exception as e:
        return "Erro: " + str(e)

print("Bem-vindo à Calculadora Científica!")
print("Operações suportadas: ^, yx, √, ex, sin, cos, tan, (-), (), π")
print("Digite 'mode' para alternar entre graus e radianos.")
print("Digite 'exit' para sair.")

modo = 'graus'

while True:
    expressao = input("Digite a expressão a ser calculada: ")

    if expressao.lower() == 'exit':
        print("Obrigado por usar a calculadora!")
        break
    elif expressao.lower() == 'mode':
        modo = 'radianos' if modo == 'graus' else 'graus'
        print(f"Modo alterado para {modo}.")
    else:
        resultado = calcular(expressao)
        print("Resultado:", resultado)
