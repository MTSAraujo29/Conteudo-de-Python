invini = int(input('Valor do investimento ínicial: '))
tempodura = int(input('Tempo de duração do investimento: '))
juros = 10
res = invini
for cont in range(tempodura):
    res = res + (res * 10 / 100)
    cont += 1
print(f'Em {tempodura} meses o valor do investimento ínicial do R$ {invini} reais.')
print(f'Rendeu o valor final foi de R${res:.2f} reais.')