# La consigna es la siguiente: vas a crear un programa que primero le pida al usuario
# que ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo,
# una frase, un poema, lo que quiera. Luego, el programa le va a pedir al usuario que
# también ingrese tres letras a su elección y a partir de ese momento nuestro código
# va a procesar esa información para hacer cinco tipos de análisis y devolverle al
# usuario la siguiente información:

texto = input("Introduce un poco de texto: ")
textominus = texto.lower()
print("Ahora te voy a pedir escribir 3 letras")
letra1 = input("Primera letra: ")
letra2 = input("Segunda letra: ")
letra3 = input("Tercera letra: ")

lista_letras = [letra1.lower(), letra2.lower(), letra3.lower()]

# Primero: ¿cuántas veces aparece cada una de las letras que eligió?
print("La letra " + letra1 + " se repite " + str(textominus.count(lista_letras[0])) + " veces")
print("La letra " + letra2 + " se repite " + str(textominus.count(lista_letras[1])) + " veces")
print("La letra " + letra3 + " se repite " + str(textominus.count(lista_letras[2])) + " veces")

# Segundo: le vas a decir al usuario cuántas palabras hay a lo largo del texto entero
palabras = texto.split()
print("En tu texto hay " + str(len(palabras)) + " palabras")

# Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última.
print("La primera letra del texto es " + texto[0] + ". Y la última es " + texto[-1] + ".")

# Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
palabras.reverse()
print("Tu texto leído con las palabras del revés quedaría así: ")
print(palabras)

# Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del texto.
python = "python" in textominus
print("¿Se encuentra 'python' en tu texto?: " + str(python))
