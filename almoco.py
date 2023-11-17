# Criar um algoritmo que salve as informacoes de 
# uma refeicao e informe se tenho dinheiro ou nao suficiente. 
# Considere se tem o bom amigo ou não, caso nao tenha dinheiro para pagar a conta.
# Informar o troco
# Informar o valor da gorjeta

almoco_favorito = input("Informe o seu almoço favorito: ")
almoco_preco = float(input("Informe o preço do seu almoço favorito: "))
almoco_amigo = input("Seu amigo está cntigo? (S/N): ").upper()
almoco_dinheiro = float(input("Informe o dinheiro que você tem: "))
almoco_gorjeta = float(input("Informe o valor da gorjeta: "))
gorjeta = almoco_preco * almoco_gorjeta / 100
total = almoco_preco + gorjeta

# print(almoco_favorito)
if almoco_dinheiro >= total:
    troco = almoco_dinheiro - total
    print("Você pode pagar o seu %s." % almoco_favorito)
    #
    print("O valor total é %.2f e da gorjeta é de R$ %.2f " % (total, gorjeta))
    print("Seu troco é de R$ %.2f" % troco)
# elif almoco_dinheiro >= almoco_preco and almoco_amigo == "S":    
elif almoco_amigo == "S":
    print("Seu almoço está garantido!")
    print("Não esqueça da gorjeta de R$ %.2f do garçom!" % gorjeta)
else:  
    print("Você não pode pagar o seu almoço.")
    print("Vai ter que lavar pratos!")