"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, 
um de cada. Depois precisa executar a operação e mostrar o resultado na tela. 
Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto 
no campo ao lado para que outros desenvolvedores possam analisá-lo.
"""

def menu():
    print('\n\tCalculadora: escolha a operação abaixo:')
    print('\t\t1: Soma')
    print('\t\t2: Subtração')
    print('\t\t3: Multiplicação')
    print('\t\t4: Divisão')
    print('\t\t0: Sair')
    
def operacoes(n1, n2, op):
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
    while True:
        menu()
        op = int(input('\n\tDigite o número da operação: '))
        if op == 0:
            break
        elif op > 4:
            print('\tEssa opção não existe')
            continue
        n1 = int(input('\tDigite o primeiro número: '))
        n2 = int(input('\tDigite o segundo número: '))
        resultado = operacoes(n1, n2, op)
        print(f'\tO resultado da operação é {resultado:,.2f}')
        
if __name__ == '__main__':
    main()