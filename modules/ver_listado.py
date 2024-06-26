import json
from pathlib import Path
def ver_listado(jfile):
    '''
    esta funcion hara el proceso de agregar pintura en un archivo json

    jfile = ruta hacia un archivo json
    '''
    if not jfile.exists():
     print('el archivo no existe, ¡no hay pinturas!')
     
    if jfile.stat().st_size == 0:
       print('el archivo esta vacio, ¡no hay pinturas!')
    else:
       with open(jfile, mode='r') as stream:
          json_file = json.load(stream)
          if json_file:
             print('listado de pintutas: ')
             for ind, pintrura in enumerate(json_file).stat == 1:
                print(f'nombre: {pintrura}')
                print(f'valor {pintrura}')
                print(f'stock{ind[pintrura]}')
              
          else:
             print('no hay pinturas asociadas')
             

                