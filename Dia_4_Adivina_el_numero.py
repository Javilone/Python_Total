from random import randint

nombre = input("Hola! Introduce tu nombre: ")
print("¡Tendrás que adivinar un número del 1 al 100!")

numero = randint(1, 101)

vidas = 8
intentos = 0

adivina = int(input("Escribe un número del 1 al 100: "))
juego = True
while juego:
    try:
        if (adivina < 1) or (adivina > 100):
            print("Ese número no está entre 1 y 100")
            adivina = int(input("Escribe un número del 1 al 100: "))
        else:
            while vidas >= 0:
                if adivina < numero:
                    print("Ese número es MENOR al que he pensado.")
                    vidas = vidas - 1
                    intentos = intentos + 1
                    adivina = int(input("Escribe un número del 1 al 100: "))
                if adivina > numero:
                    print("Ese número es MAYOR que el que he pensado.")
                    vidas = vidas - 1
                    intentos = intentos + 1
                    adivina = int(input("Escribe un número del 1 al 100: "))
                if adivina == numero:
                    print("¡Felicidades! ¡Has dado en el clavo!")
                    print(f"Te ha llevado {intentos} intentos acertar.")
                    juego = False
                    break
                if vidas == 0:
                    print("Lo siento, te has quedado sin más intentos.")
                    break
    except ValueError:
        print("Ese número no está entre 1 y 100")
        adivina = int(input("Escribe un número del 1 al 100: "))

