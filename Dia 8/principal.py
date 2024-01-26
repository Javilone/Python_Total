import numeros
from os import system

def inicio():

    
    programa = True
    while programa == True:
        system('clear')
        print("""¡Buenos días! Esta usted en Farmacia Smile!
          Seleccione para qué area quiere elegir su turno:
          1 - COSMÉTICA
          2 - FARMACIA
          3 - PERFUMERÍA""")
        turno = input("Elija area: ")
        turno = int(turno)
        if (turno > 0) & (turno < 4):
            numeros.seleccion_turno(turno)
            seguir = input("""¿Desea sacar otro turno?: 
                  1 - SI:
                  2 - NO: """)
            seguir = int(seguir)
            if seguir == 1:
                continue
            if seguir == 2:
                print("Chao! Que pase un buen día!")
                programa = False
                break
        else:
           print("Por favor elije una sección")
           
inicio()