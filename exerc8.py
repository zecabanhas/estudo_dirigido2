qntCD = int(input("Digite a quantidade de CDs: "))
print("")

a = 0
vTotal = 0

for x in range(qntCD):
	vCD = eval(input("Digite o valor do CD: "))
	vTotal = vTotal + vCD
	vMedio = vTotal / qntCD
	a = a + 1

print("")
print("O valor total pago foi: R$", vTotal)
print("O valor médio pago por cada CD foi de: R$", vMedio)
