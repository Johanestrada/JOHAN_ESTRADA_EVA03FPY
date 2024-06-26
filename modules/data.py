from pathlib import Path

home = Path(__file__).parent.parent

j_file = (home/'base.json')
c_file = (home/'export.json')

menup = ['Ver Listado de Pinturas',
         'Buscar Pintura',
         'Agregar Pintura',
         'Eliminar Pintura',
         'Exportar Pinturas']

