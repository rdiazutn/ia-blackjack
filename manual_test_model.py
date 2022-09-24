import tensorflow.keras as keras

model = keras.models.load_model('blackjack_model.h5')

print('Bienvenido a la prueba manual, siga las instrucciones')
count = int(input('Ingrese cuenta\n'))
has_ace = 1 if input('Hay algún as? si/no\n') == 'si' else 0
oponent_count = int(input('Ingrese cuenta de la máquina\n'))
print('La predicción es', 'Pedir' if model.predict([[count, has_ace, oponent_count]]) > 0.5 else 'Plantarse')

