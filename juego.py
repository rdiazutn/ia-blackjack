import random
#NOTA: los ases siempre valen 1 pero tenes que poner el flag HayAs
valoresPosibles = [1,2,3,4,5,6,7,8,9,10]
class Partida:
    def __init__(self):
        self.mano = []
        self.situacion = 0

    def pedirCarta(self):
        valor = random.choice(valoresPosibles)
        return valor

    def siguienteCarta(self):
        valor = random.choice(valoresPosibles)
        return valor

    def getSituacion(self):
        # { cuenta: N, hayAs: true|false, banca: M, estado: 'jugando'|'perdio'|'gano'|'empato' }
        return  { 'cuenta': 19, 'hayAs': False, 'banca': 8, 'estado': 'gano' }
    
    def quedarse(self):
        pass
    
    def getResultado(self):
        #{ ganador: 'jugador'|'banca'|'empate', cuentaJugador: N, cuentaBanca: M }
        return { 'ganador': 'jugador', 'cuentaJugador': 20, 'cuentaBanca': 19 }


def crearMano():
    return Partida()
