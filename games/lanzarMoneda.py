import random
print('Lanzare una moneda mil veces. Adivina cuántas veces caerá CARA. (presiona INTRO para comenzar)')
input()
lanzamientos = 0
caras = 0
while lanzamientos < 1000:
    if random.randint(0, 1) == 1:
        caras = caras + 1
    lanzamientos = lanzamientos + 1

    if lanzamientos == 900:
        print('900 lanzamientos hubo ' + str(caras) + ' caras')
    if lanzamientos == 100:
        print('En 100 lanzamientos cara salió ' + str(caras) + ' veces')
    if lanzamientos == 500:
        print('la mitad de lanzamientos y cara salió ' + str(caras) + ' veces.')

print()
print(' En 1000 lanzamientos , al final cara salió ' + str(caras) + ' veces.')
print('¿Estuviste cerca?')
