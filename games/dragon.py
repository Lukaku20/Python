import random 
import time

def mostrarIntroducción():
    print('Estas en una tierra llena de dragones. Frente a tí')
    print('hay dos cuevas y en cada una un dragón.  En una de ellas, el dragón es generoso')
    print('y amiglable y compartirá su tesoro contigo. Pero en la otra')
    print('es hay un dragón hambriento y te fulminará inmediatamente.')
    print()

def elegirCueva():
    cueva = ''
    while cueva != '1' and cueva != '2':
        print('¿A qué cueva quieres entrar? (1 o 2)')
        cueva = input()

    return cueva

def explorarCueva(cuevaElegida):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('¡Un dragón aparece súbitamente frente a tí, y abre sus fauces...')
    print()
    time.sleep(2)

    cuevaAmigable = random.randint(1, 2)

    if cuevaElegida == str(cuevaAmigable):
        print('¡El dragón se convierte en tu amigo y comparte su tesoro!')
    else:
        print('¡El dragón es violento, escupe fuego y te liquida en el acto!')

jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 's':

    mostrarIntroducción()

    númeroDeCueva = elegirCueva()

    explorarCueva(númeroDeCueva)
    
    print('¿Queres jugar de nuevo che? (si o no)')
    jugarDeNuevo = input()
