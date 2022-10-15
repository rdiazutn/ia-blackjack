import tensorflow.keras as keras
import tensorflow as tf
import csv

def _mean_relative_error(normalizer):
  def mean_relative_error(y_pred, y_true):
    return tf.math.divide_no_nan(tf.abs(y_true - y_pred), normalizer)
  return mean_relative_error


with open('datos.csv', 'r') as f:
  reader = csv.reader(f, delimiter=';')
  data = list(reader)
  convert_cell = lambda cell: 1 if cell == 'TRUE' else 0 if cell == 'FALSE' else int(cell) 
  data_parsed = list(map(lambda row: list(map(convert_cell, row)), data))
  x_train = list(map(lambda row: row[0:3], data_parsed))
  y_train = list(map(lambda row: row[3], data_parsed))
  print(x_train)
  print(y_train)

  learning_rate = 0.001
  layers = [3, 8, 8 ,1]

  model = keras.Sequential()

  # Capa 1
  model.add(keras.layers.Dense(layers[1], activation='relu'))
  # Capa 2
  model.add(keras.layers.Dense(layers[2], activation='relu'))
  # Capa 3
  model.add(keras.layers.Dense(layers[3], activation='sigmoid'))

  # Compilamos el modelo
  ## SGD descenso del gradiente
  ## loss función de pérdida
  model.compile(loss='mse', optimizer=keras.optimizers.Adam(learning_rate=learning_rate), 
    metrics=[tf.keras.metrics.MeanAbsoluteError(), _mean_relative_error(normalizer=[1]), 'accuracy'])

  # Entrenamos el modelo
  model.fit(x_train, y_train, epochs=550, batch_size=32)
  # print('Prediction for ', x_train[:1])
  # print(model.predict(x_train[:1]))

  print('-----------------')
  print('Evaluate model on test data')
  results = model.evaluate(x_train, y_train, batch_size=128)
  print('La pérdida es', results[0], ' y la precisión es', results[1])
  print('-----------------')
  model.save('blackjack_model.h5')