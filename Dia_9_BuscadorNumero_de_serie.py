# Import de módulos para expresiones regulares
# módulo os para usar walk y recorrer rutas de carpetas
# time y datetime para obtener tiempo y fecha
# pathlib para Path (directorios y rutas)
import re
import os
import time
import datetime
from pathlib import Path
import math


inicio = time.time()
ruta = '/Users/javilone/Desktop/Python Total Udemy/Codigo/Dia 9/Proyecto Dia 9/Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
nros_encontrados = []
archivos_encontrados = []

# Esta función será usada dentro de la función crear_listas.
# Abre todos los archivos indicados posteriormente y busca dentro y devuelve el patrón dado.
def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

# Esta función creará las listas de los archivos donde encontró los patrones
# y los agregará a las listas declaradsa al comienzo archivos_encontrados y nros_encontrados
# Buscando en archivos dentro de carpetas/subcarpetas usando os.walk(ruta)
# por cada archivo dentro de una de ellas, añadirá a la lista si no es una cadena vacía.
def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a), mi_patron)
            if resultado != '':
                nros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())


# Construcción de la tabla con formato
def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f'{a}\t{nros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Números encotrados: {len(nros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


crear_listas()
mostrar_todo()
