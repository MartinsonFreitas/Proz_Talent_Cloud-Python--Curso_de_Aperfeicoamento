"""
    Declare dois arrays, cada um com um mínimo de cinco elementos, e imprima eles no terminal usando o 
    comando print(). O primeiro array deve conter os produtos de uma loja da sua escolha 
    (loja de comida, materiais de construção, música, etc). 
    
    O segundo array deve conter os anos de nascimento de familiares e amigos seus. 
    
    Lembre-se de usar nomes descritivos para nomear cada variável, e de usar o tipo de dado apropriado 
    para cada lista (strings, booleanos, números inteiros, floats).

    Trabalhe esse código no Google Colab, e compartilhe o link do projeto no campo ao lado para que 
    outros desenvolvedores possam analisá-lo. 
"""

lista_produtos = ['arroz', 'feijão', 'macarrão', 'carne', 'frango']
birthday = [1980, 1981, 1982, 1983, 1984]

def menu():
    print('''
    1 - Lista de produtos
    2 - Lista de aniversários
    3 - Sair
    ''')

    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        print(lista_produtos)
    elif opcao == 2:
        print(birthday)
    elif opcao == 3:
        exit()
    else:
        print('Opção inválida')
        
def main():
    while True:
        menu()
        
if __name__ == '__main__':
    main()