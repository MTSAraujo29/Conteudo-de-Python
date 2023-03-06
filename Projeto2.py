# basicamente o codigo funciona do seguinte maneira a cada letra da palavra
# selecionada pelo usuario vamos pegar o numero dela em decima fazer o calculo
# e o resultado do calculo voltar para a letra para glifo.

import random
import os

numale = random.randint(0, 999999)
print(f'Sua senha de segurança gerada é: {numale}')

# Parte do codigo responsavel pela criptografia
def crip():
    palavra = input("Escreva a mensagem para criptografa: ")
    msg = ''
    for i in palavra:
        msg = msg + chr(ord(i) + 10 - 2 + 15 - 35)  # O 'ord' ele transforma letra em numero pela tabela asci.
    print(msg)  # Já o 'chr' tranforma decimal em letra.


# Parte do codigo responsavel pela descriptografia
def des():
    senha2 = int(input('Digite sua senha gerada: '))
    if numale == senha2:
        palavra = input("Escreva a mensagem para descriptografa: ")
        msg = ''
        for i in palavra:
            msg = msg + chr(ord(i) - 10 + 2 - 15 + 35)
            print(msg)
    else:
        print('ERRO SENHA INVALIDA TENTE NOVAMENTE')
        des()

# Inicialização do codigo.
while True:
    print("Para criptografar digite 'c' e para descriptografa digite 'd'. ")
    opcao = input('O que deseja fazer? ')
    if opcao == 'c':
        crip()
    else:
        des()
    continua = input("Deseja criptografar ou descriptografa outra palavra? digite 's' ou 'n': ")
    if continua == 's':
        os.system("cls")
        print('OK VAMOS CONTINUA!! ')
    else:
        print('FIM')
        break