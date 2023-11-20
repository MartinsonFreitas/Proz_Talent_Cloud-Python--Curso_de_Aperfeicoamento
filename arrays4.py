"""
A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente! 
Dessa vez, eles precisam que você atualize o array de produtos. 
Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções. 
Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos. 
Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

Como desafio, adicione dois novos produtos da sua escolha à lista. 

Trabalhe esse código no Google Colab, e compartilhe o link do projeto no campo ao lado para que outros 
desenvolvedores possam analisá-lo.   
"""
import time

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

lista_produtos[1] = 'rímel'
lista_produtos[4] = 'cremes hidratantes'
lista_produtos.remove('delineadores')

for produto in lista_produtos:
    print(f'Temos {produto} à venda!')
    time.sleep(1)

print('')
print('Adicionando novos produtos...\n')
lista_produtos.append('sabonetes íntimos')
lista_produtos.append('shampoo para bebês')
time.sleep(2)

for produto in lista_produtos:
    print(f'Temos {produto} à venda!')
    time.sleep(1)

print('')