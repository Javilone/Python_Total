# GENERADORES
def g_cosmetica():
    turno = 0
    while True:
        yield turno
        turno += 1
    
def g_farmacia():
    turno = 0
    while True:
        yield turno
        turno += 1
    
def g_perfumeria():
    turno = 0
    while True:
        yield turno
        turno += 1

cosmetica = g_cosmetica()
farmacia = g_farmacia()
perfumeria = g_perfumeria()

# DECORADOR
def seleccion_turno(num):
    if num == 1:
        print ("Su turno para COSMÉTICA es C-" + str(next(cosmetica)) + ". Aguarde su turno")
    if num == 2:
        print("Su turno para FARMACIA es F-" + str(next(farmacia)) + ". Aguarde su turno")
    if num == 3:
        print("Su turno para PERFUMERÍA es P-" + str(next(perfumeria)) + ". Aguarde su turno")

#turno = int(input("Elije turno: "))
#seleccion_turno(turno)
#seleccion_turno(turno)