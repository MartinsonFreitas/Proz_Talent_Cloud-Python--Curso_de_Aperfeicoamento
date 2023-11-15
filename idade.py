"""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, 
no ano atual (2023).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e 
continuará perguntando até que um valor correto seja preenchido.
"""

def calcula_idade(ano_nascimento):
    ano_atual = 2023
    idade = ano_atual - ano_nascimento
    return idade

def main():
    while True:
        nome = input('Digite seu nome completo: ')
        ano_nascimento = input('Digite seu ano de nascimento: ')
        
        try:
            ano_nascimento = int(ano_nascimento)
            if ano_nascimento < 1922 or ano_nascimento > 2022:
                raise Exception('Ano de nascimento inválido')
            break
        except:
            print('Ano de nascimento inválido')
            continue
        
    idade = calcula_idade(ano_nascimento)
    print(f'Olá {nome}, você tem {idade} anos')
    
if __name__ == '__main__':
    main()