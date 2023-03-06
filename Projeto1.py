# alfabeto e valores constantes

alfabeto = ['a','A','@', 'b','B','Ô', '$', 'c','C', '#', 'd','D','á','í','$','Í',
            'e','E', '%', 'f','F', 'Ï', 'g','G', '&', 'h','H', '*', 'i',
            'I','(', 'j','J', ')', 'k','K','-','é','ê','ë','ù','Á','É',
            'l','L', '/', ':','ã', 'm','M','î', '[', 'n','N', ']', 'o','O', '=',
            'p','P','â', '+', 'q','û','Q','ì', 'ü', 'r','R','Ê','^', 's','S','ú','Ó',
            't','T', '"', 'u','U', 'ä', 'v','ÿ','Õ','V', 'w','W','x','X','ó', 'y',
            'Y', 'z','Z','Î','Û', '0', '|', '1','Ã', '~', '2', '3','ô', '4', '>','5','Ú',
            '6', '<', '7', '8','õ', '9', '_', ',', '.', '?', '!', ' ','Â']

valormud = 9
n = len(alfabeto)

#FUNCAO CRIPTOGRAFAR

def criptografia():
    mensagem = input("Digite a Mensagem para criptografar:\n")
    cripto = ""

    for letra in mensagem:
        indice = alfabeto.index(letra)
        substituicaoletra = alfabeto[(indice + valormud) % n]

        cripto = cripto + substituicaoletra



    print('A sua mensagem critpografada é:',cripto)
    continuacao()



#FUNCAO DESCRIPTOGRAFAR

def descriptografia():
    mensagem = input("Digite a Mensagem para descriptografar:\n")
    descripto = ""

    for letra in mensagem:

        indice = alfabeto.index(letra)
        substituicaoletra = alfabeto[(indice - valormud) % n]

        descripto = descripto + substituicaoletra


    print('A sua mensagem criptografada é:',descripto)
    continuacao()

#FUNÇAO COMEÇAR O PROGRAMA

def comeco():

    print("Para criptografar digite 'c' para descriptografar digite 'd' ou digite 'f' para finalizar o uso.\n")
    opcao = input('O que deseja fazer?\n')
    if opcao == 'c':
       criptografia()
    elif opcao == 'd':
      descriptografia()
    elif opcao == 'f':
      print("\n Obrigado por utilizar o nosso sistema de criptografia!")

    else:
      print("Opção Invalida!\n")
      continuacao()

#FUNCAO CONTINUAR EXECUTANDO PROGRAMA

def continuacao():

    continuar = input("Deseja continuar?\nDigite s para continuar e n para não continuar.\n")
    if continuar == 's':
      print('Ok, vamos continuar!')
      comeco()
    elif continuar == 'n':
      print('Ok, finalizamos por aqui!\nObrigado por utilizar o nosso sistema de criptografia!\n')

    else:
       print('Opção invalida! Tente novamente.\n')
       continuacao()


#INICIALIZAÇÃO DO CODIGO

print('Olá Seja bem vindo a nossa APS')
print('Trazemos um programa de Criptografia e Descriptografia')
print('Faça um bom aproveito do programa.\n')
comeco()