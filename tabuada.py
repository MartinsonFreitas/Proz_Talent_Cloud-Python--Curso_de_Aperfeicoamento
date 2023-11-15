def tabuada(num1):
    
    for i in range(11):
        try:
            print(f'{num1} x {i} = {num1 * i}')
        except (ValueError):
            # Manipular tipo incorreto
            print("Você deve digitar apenas números!")            
            main() # Chama a função main novamente    
        
def main():
    #num1 = int(input('Digite um número: '))
    num1 = input('Digite um número: ')
    
    if num1.isnumeric():
        num1 = int(num1)
        tabuada(num1)
    else:
        print('Você deve digitar apenas números!')
        main()
    
if __name__ == "__main__":
    main()
    #tabuada(9)