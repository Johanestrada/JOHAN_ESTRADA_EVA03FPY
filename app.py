from modules.construccion import construir_menu, sol_ans
from modules.data import menup, j_file, c_file
from modules.agregar import agregar
from modules.ver_listado import ver_listado
from modules.buscar import buscar
import os

print('pinturas acliricas')
print('-'*25)
print('M A N D A R I N A')
print('-'*25)

while True:
    construir_menu(menup)
    ans = sol_ans()
    os.system('cls')
    if ans == '1':
        ver_listado(j_file)
    elif ans == '2':
        buscar(j_file)
    elif ans == '3':
        os.system('cls')
        agregar(j_file)
    elif ans == '4':
        pass