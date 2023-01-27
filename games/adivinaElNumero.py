# Este es el juego de adivinar el número.
import random

intentosRealizados = 0

print('¡Hola! ¿Cómo te llamas?')
miNombre = input()

número = random.randint(1, 10)
print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 10.')
print('Intenta adivinar.')
while intentosRealizados < 3:
     #Hay cuatro espacios delante de print
    estimación = input()
    estimación = int(estimación)

    intentosRealizados += 1
    
    if estimación < número:
        print('Es un número muy bajo.') # Hay ocho espacios delante de print.

    if estimación > número:
        print('Es un número muy alto.')

    if estimación == número:
        break

if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print('¡Enhorabuena, ' + miNombre + '¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')
    
   

if estimación != número:
    número = str(número)
    print('¡Que mala suerte! El número que estaba pensando era el ' + número)
    
