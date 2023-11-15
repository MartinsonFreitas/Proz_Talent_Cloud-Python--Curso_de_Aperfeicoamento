"""
Precisamos imprimir um número para cada andar de um hotel de 20 andares. 
Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto 
no campo ao lado para que outros desenvolvedores possam analisá-lo.

"""
import time

andares = 20

def imprimir_andares_com_for(andares):
    print("Imprimindo com a estrutura for: \n")
    
    for andar in range(andares):
        if andar != 13:
            print(f"O andar é {andar}")
            time.sleep(1)
            
def imprimir_andares_com_while(andares):
    andar = 0
    
    print("Imprimindo com a estrutura while: \n")
    
    while andar < andares:
        if andar != 13:
            print(f"O andar é {andar}")
            time.sleep(1)
        andar += 1
        
def imprimir_andares_com_for_decrescente(andares):
    print("Imprimindo com a estrutura for decrescente: \n")
    
    for andar in range(andares, 0, -1):
        if andar != 13:
            print(f"O andar é {andar}")
            time.sleep(1)
            
def imprimir_andares_com_while_decrescente(andares):
    print("Imprimindo com a estrutura while decrescente: \n")
    
    andar = andares
    while andar > 0:
        if andar != 13:
            print(f"O andar é {andar}")
            time.sleep(1)
        andar -= 1
        
def imprimir_andares_com_for_pares(andares):
    print("Imprimindo com a estrutura for pares: \n")
    
    for andar in range(0, andares, 2):
        if andar != 13:
            print(f"O andar é {andar}")
            time.sleep(1)
            

def escolher_impressao():
    while True:
        print("Escolha uma opção:")
        print("1 - For")
        print("2 - While")
        print("3 - For decrescente")
        print("4 - While decrescente")
        print("5 - For pares")
        print("0 - Sair")
        
        opcao = int(input("Digite a opção: "))
        
        if opcao == 1:
            imprimir_andares_com_for(andares)
        elif opcao == 2:
            imprimir_andares_com_while(andares)
        elif opcao == 3:
            imprimir_andares_com_for_decrescente(andares)
        elif opcao == 4:
            imprimir_andares_com_while_decrescente(andares)
        elif opcao == 5:
            imprimir_andares_com_for_pares(andares)
        elif opcao == 0:
            break
        else:
            print("Opção inválida")
        
def main():
    escolher_impressao()
    
if __name__ == "__main__":
    main()