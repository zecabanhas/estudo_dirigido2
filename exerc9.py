lista = []
count = 0

quant = int(input("Digite a quantidades de numeros que deseja: "))
while quant != count:
    num = float(input("Digite um número: "))

    while num > 1000 or num < 0:
        num = float(input("Digite um número[erro]: "))

    lista.append(num)
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))