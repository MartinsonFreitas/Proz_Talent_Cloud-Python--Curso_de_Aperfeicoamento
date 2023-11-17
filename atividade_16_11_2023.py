"""
1 - Fazer uma finção que receba um número positivo menor que 100 e trate os erros e exceções
2 - Verificar se o número é divisivel por 2 e 3, tratar os erros e exceções
"""

def divisivel_por_2_e_3():
    numero_valido = False
    # Enquanto o número não for válido, o programa vai pedir para digitar um número
    while (numero_valido==False):
        numero = int(input('Digite um número: '))
        # Trata os erros e exceções
        try:
            # Verifica se o número é maior que 0 e menor que 100
            if numero > 0 and numero< 100:
                # Verifica se o número é divisivel por 2 e 3
                if numero % 2 == 0 and numero % 3 == 0:
                    print(f'O número {numero} é divisivel por 2 e 3')
                    numero_valido = True
                # Se o número não for divisivel por 2 e 3, o programa vai pedir para digitar outro número    
                else:
                    print(f'O número {numero} não é divisivel por 2 e 3')
            # Se o número não for maior que 0 e menor que 100, o programa vai pedir para digitar outro número        
            else:
                print('O número deve ser maior que 0 e menor que 100')
        # Se o valor digitado não for um número inteiro, o programa vai pedir para digitar outro número
        except ValueError:
            print('O valor digitado deve ser um número inteiro')        

# Chama a função principal    
def main():
    try:
        divisivel_por_2_e_3()
    except ValueError:
        print('O valor digitado deve ser um número inteiro')

# Chama a função main        
if __name__ == '__main__':      
    main()