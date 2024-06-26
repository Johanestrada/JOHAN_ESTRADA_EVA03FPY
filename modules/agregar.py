import json
import os
from pathlib import Path

def agregar(jfile):
    '''
    esta funcion hara el proceso de agregara una nueva pintura al inventario

    json_file = ruta hacia un archivo json
    '''
    if not jfile.exists():
        jfile.touch()
        print('la base de datos estava vacia, pero ha sido creda')
    if jfile.stat().st_size == 0:
        codp = 380560
        json_file = []
    else:
     with open(jfile, mode='r') as stream:
      json_file = json.load(stream)
     codp = []
     for prenda in json_file:
        codp.append(prenda['codigo'])
        codp = codp.max + 1
     while True:
        nombres = input('ingresa el nombre de la pintura: ')
        ans = input(f'el nombre de la pintura es: - {nombres} - es correcto? \n1(SI)\n2(NO)')
        if ans == '1':
           break
        else:
           os.system('cls')
    while True:
        tipo = input('ingresa el tipo de pintura: ')
        ans = input(f'el tipo de pintura es: - {tipo} - es correcto? \n1(SI)\n2(NO)\n')
        if ans == '1':
           break
        else:
           os.system('cls')
    while True:
       valor = input('ingresa el valor de la pintura: ')
       ans = input(f'el valor de la pintura es: - {valor} - es correcto? \n1(SI)\n2(NO)\n')
       if ans == '1' and ans.isnumeric():
          break
       else:
          print('solo se pueden agregar numeros')
    while True:
       stock = input('ingresa el stock disponibles de la pintura')
       ans = input(f'el stock de la pintura es: - {stock} - es correcto? \n1(SI)\n2(NO)\n')
       if ans == '1'and ans.isnumeric():
          break
       else:
          print('solo puedes ingresar numeros')
    data = {
       'nombre' : nombres,
       'tipo' : tipo,
       'valor' : valor,
       'stock' : stock
    }
    json_file.append(data)
    with open(json_file, mode='w') as stream:
     json_file = json.dump(stream)
     print('La pintura se agrego correctamente')
