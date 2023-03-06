n1 = int (input("Digite o número de ínicio: "))
n2 = int (input("Digite o número de fim: ")) 
ini = n1
fim = n2
resto = ini - fim
for cont in range (resto):
    fim += 1
    ini = ini + fim
    cont = cont + 1
print(f'A soma do intervalo de {n1} e {n2} é {ini}')