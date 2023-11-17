numeroCorreto = False

while (numeroCorreto == False):

   print("Insira um número par")

   try:

       numero = int(input())

       if (numero%2 == 0):

           numeroCorreto = True

           print("Você digitou um numero par !")

       else :

           print("Você digitou um número impar")

   except:

       print("Caracter inválido, por favor digite um número par")