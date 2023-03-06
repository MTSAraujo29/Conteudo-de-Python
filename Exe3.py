i = 0
vlr = 100
port = 10
vlr = vlr * 100
print(f'Valor de 1° mês é: {vlr}')
for i in range(8,90):
    vlr = vlr + vlr * 0.02
    i += 1
print(f'Valor no 10° mês foi de: {vlr:.2f}')