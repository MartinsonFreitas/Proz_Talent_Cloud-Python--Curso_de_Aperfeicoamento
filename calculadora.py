"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números 
da operação e o terceiro será a entrada que definirá a operação a ser executada. 

Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto 
no campo ao lado para que outros desenvolvedores possam analisá-lo.

"""

def calculadora(n1, n2, op):
    if op == 1:
        return n1 + n2
    elif op == 2:
        return n1 - n2
    elif op == 3:
        return n1 * n2
    elif op == 4:
        return n1 / n2
    else:
        return 0
    
def main():
    print('Calculadora')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    
    print('Escolha a operação: ')
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    op = int(input('Digite o número da operação: '))
    
    resultado = calculadora(n1, n2, op)
    print(f'O resultado da operação é {resultado}')    
    
if __name__ == '__main__':
    main()