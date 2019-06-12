entrada = int(input("Digite um numero positivo real qualquer: "))
if entrada <=0:
   finalizar = raw_input('Numero invalido, pressione qualquer tecla para continuar...')
   exit()

# i sera nosso divisor inicial
div_ini = 1
# j sera nosso contador de ocorrências
j = 0

#Nenhum numero real vai ser divisivel por um numero maior do que sua metade
entrada1 = int(entrada/2)

while div_ini <= entrada:
    if (entrada % div_ini==0):1
    print("-> É divisivel por", div_ini, "<-""-> É divisivel por", div_ini, "<-")
    i = div_ini+1
    j = j+1

   if div_ini >= entrada1:
      # damos a i, o valor da variavel entrada, pois o próximo divisor sera o próprio número
      i = entrada
      print("--> É divisivel por",i,"<--")
      div_ini = i+1
      j = j+1

   else:
       div_ini = div_ini+1
if(j==2):
   print("O número requisitado é primo!")

else:
   print("Numero não é primo, possui",j,"divisores.")