

def construir_menu(lista):
    '''
    esta funcion recibe una lista y la enumerara para crear un menu
    '''
    for ind, opt in enumerate(lista):
        print(f'{ind + 1}. {opt}')



def sol_ans():
    '''
    
    '''
    resp = input('ingresa una opcion: ')
    return resp