import random
número1 = random.randint(1, 10)
número2 = random.randint(1, 10)
print('¿Cuánto es ' + str(número1) + ' + ' + str(número2) + '?')
respuesta = input()
if int(respuesta) == número1 + número2:
    print('Correcto')
else:
    print('Noooo, la respuesta es ' + str(número1 + número2))
    
