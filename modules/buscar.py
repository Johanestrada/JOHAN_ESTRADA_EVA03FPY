import json
from pathlib import Path

def buscar(jfile):
    '''
    esta funcion buscara en un archivo json pinturas

    json = ruta hacia
    '''
    if not jfile.exists():
        print('elarchivo esta vacio, no se puede realizar la busqueda')
    if jfile.stat().st_size == 0:
        print('el archivo esta vacio, no hay pinturas')

    else:
        with open(jfile, mode= 'r') as stream:
            jfile = json.load(stream)
        while True:
            busqueda = input('ingresa el nombre o codigo de la pintura ha buscar')
            
