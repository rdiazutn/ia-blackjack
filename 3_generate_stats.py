from tabnanny import verbose
import tensorflow.keras as keras
import aux_juego
import sys

model = keras.models.load_model('blackjack_model.h5')

def risky_player_request_card(count, has_ace, oponent_count):
  return count < 19
def moderate_player_request_card(count, has_ace, oponent_count):
  return count < 18
def cautious_player_request_card(count, has_ace, oponent_count):
  return count < 17


def model_requests_card(count, has_ace, oponent_count):
  return model.predict([[count, has_ace, oponent_count]], verbose=0) > 0.5

def play_games(games, model_requests_card):
  stats = { 'win': 0, 'lose': 0, 'draw': 0 }
  for i in range(games):
    if ((i /games * 100) % 2 == 0):
        print(f"Processed {i / games * 100}%")
    game = play_game(model_requests_card)
    result = game['result']
    if (result == 'win'):
      stats['win'] += 1
    elif (result == 'lose'):
      stats['lose'] += 1
    else:
      stats['draw'] += 1
  return stats

def play_game(requests_card_function):
  partida = aux_juego.crearMano()
  situation = partida.getSituacion()
  currentValue = situation['cuenta']+10 if situation['hayAs'] and situation['cuenta']+10 <= 21  else situation['cuenta']
  while(requests_card_function(situation['cuenta'], situation['hayAs'], situation['banca'])):
    partida.pedirCarta()
    situation = partida.getSituacion()
    currentValue = situation['cuenta']+10 if situation['hayAs'] and situation['cuenta']+10 <= 21  else situation['cuenta']
    if (currentValue > 21):
      return { 'result': 'lose' }
  partida.quedarse()
  result = partida.getResultado()
  # print('---------')
  # print(partida.manoBanca)
  # print(result['banca'])
  # print(currentValue)
  # print('---------')
  if (currentValue > result['banca'] or result['banca'] > 21):
    return { 'result': 'win' }
  elif (currentValue < result['banca']):
    return { 'result': 'lose' }
  else:
    return { 'result': 'draw' }
  


if __name__ == "__main__":
  games = 1
  if(len(sys.argv)>= 1):
      games = int(sys.argv[1])
  print('Playing ', games, ' games')
  print('Stats after ', games, ' games')
  risky_stats = play_games(games, risky_player_request_card)
  print('Risky player')
  print(risky_stats)
  moderate_stats = play_games(games, moderate_player_request_card)
  print('Moderate player')
  print(moderate_stats)
  cautious_stats = play_games(games, cautious_player_request_card)
  print('Cautious player')
  print(cautious_stats)
  ai_stats = play_games(games, model_requests_card)
  print('AI')
  print(ai_stats)
