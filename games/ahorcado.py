import random
IMÁGENES_AHORCADO = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
palabras = {'colores': 'rojo naranja amarillo azul violeta verde marron fucsia gris blanco negro rosado'.split(),
            'formas': 'circulo cuadrado rectangulo triangulo piramide elipse rombo espiral'.split(),
            'frutas': 'banana manzana frutilla cereza kiwi melon sandia pomelo durazno uva mandarina papaya kinotos'.split(),
            'animales':'hormiga camello castor raton murcielago rinoceronte gato paloma halcon perezoso araña serpiente obeja mariposa salmon ardilla perro alce elefante tigre ave hipopotamo trucha pejerrey cigüeña tortuga cangrejo pato ganso mula burro caballo conejo pingüino lagarto leon piton foca cisne alce aguila comadreja carnero almeja llama'.split()}

def obtenerPalabraAlAzar(diccionarioDePalabras):

    claveDePalabras = random.choice(list(diccionarioDePalabras.keys()))
    índiceDePalabra = random.randint(0, len(diccionarioDePalabras[claveDePalabras]) - 1)

    return [diccionarioDePalabras[claveDePalabras][índiceDePalabra], claveDePalabras]

def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacíos = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

    for letra in espaciosVacíos:
        print(letra, end=' ')
    print()

def obtenerIntento(letrasProbadas):

    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuüvwxyz':
            print('Por favor ingresa una LETRA')
        else:
            return intento

def jugarDeNuevo():

    print('¿Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')


print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta, claveSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    print('La palabra secreta pertenece al conjunto: ' + claveSecreta)
    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)


    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento


        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('¡Si!¡La palabra secreta es "' + palabraSecreta + '" ¡Has ganado!')
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento


        if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            juegoTerminado = True


    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta, claveSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break
