"""
License: MIT
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    # CORRECCIÓN: Se elimina el argumento 'nuevo'
    return sorted(items, reverse=(not ascending))

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    
    # 1. MANEJO DE ARGUMENTOS: Acepta 1 (archivo) o 2 (archivo y orden)
    ascending = True
    if len(sys.argv) in [2, 3]:
        filename = sys.argv[1]
        
        # PROCESA EL TERCER ARGUMENTO PARA EL ORDEN
        if len(sys.argv) == 3 and sys.argv[2].lower() == 'desc':
            ascending = False
    
    # MANEJO DE ERRORES DE ARGUMENTOS
    elif len(sys.argv) > 3:
        print("Número de argumentos incorrecto. Uso: script.py <fichero> [asc/desc]")
        sys.exit(1)
    else:
        print("Se debe indicar el fichero como primer argumento")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    
    word_list = [] # Se inicia la lista vacía aquí
    if os.path.isfile(file_path):
        # 2. CORRECCIÓN: Se elimina el reinicio a [33]
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    # 3. LLAMADA A LA FUNCIÓN: Se pasa el parámetro 'ascending'
    print(sort_list(word_list, ascending))
