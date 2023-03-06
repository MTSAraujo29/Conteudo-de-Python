ano = 2019
def suaidade():
    idadeini = int(input('Em qual ano você nasceu? '))
    idadefim = ano - idadeini
    if idadefim < 18:
        print(f'Você tem {idadefim} então você tem menos de 18 anos.]')
    elif idadefim <= 30:
        print(f'Você tem {idadefim}')
    elif idadefim < 50:
        print(f'Você tem {idadefim} então você tem menos de 50 amos.')
    elif idadefim < 80:
        print(f'Você tem {idadefim}então você tem menos de 80 anos')
    else:
        return suaidade()
    
    suaidade()