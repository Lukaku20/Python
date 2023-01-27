"""Bagels, por Al Sweigart al@inventwithpython.com. Es un
juego de lógica deductiva donde debes intentar adivinar un
número basándote en pistas. Este código esta disponible en
https://nostarch.com/big-book-smal-python-programming. La
version original del juego es compartida en el libro, "In-
venta tus propios juegos de computadora con Python"
Tags.. short, game, puzzle"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main(): #'main' es el nombre del entorno en el cual se ejecuta
    #codigo de maximo nivel. Primer modulo especifico donde empieza
    #a ejecutarse. Importa todos los demas modulos que necesita el
    #programa.
    print('''Bagels, es un juego de logica deductiva. Por
Al Sweigart.
    Yo estoy pensando en un numero de {}-digitos sin digitos repetidos.
    Intenta adivinar cuál es. Sigue estas pistas:
    Cuando digo:     Quiero decir:
    Pico             Un digito es correcto pero esta en la posicion equivocada.
    Ferne            Un digito es correcto y esta bien ubicado.
    Bagels           Ninguno es correcto.

    Por ejemplo, si el numero secreto era 248 y tu dijiste 843, la pista sería
    'Ferne Pico.'''.format(NUM_DIGITS))

    while True: #Principal loop del juego
        secretNum = getSecretNum()
        print('Yo tengo ideado un numero.')
        print('Tienes {} intentos para adivinarlo.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Intento #{}: '.format(numGuesses))
                guess = input('> ')

                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

                if guess == secretNum:
                    break #Es correcto, entocnes se sale del loop
                if numGuesses > MAX_GUESSES:
                    print('Se terminaron tus oportunidades')
                    print('El numero era {}.'.format(secretNum))
        print('¿Quieres volver a intentarlo? (si o no)')
        if not input('> ').lower().startswith('s'):
            break
    print('Gracias por estar jugando')

def getSecretNum():
    """Devuelve una cadena compuesto de NUM_DIGITS unir digitos aleatorios."""
    numbers = list('0123456789') #crea una lista de digitos del 0 al 9
    random.shuffle(numbers) #mezclarlas en el orden

    # obtener los primeros digitos en la lista de los numeros secretos
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess,secretNum):
    if guess == secretNum:
        return 'Lo adivinaste'
        
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Ferne')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
