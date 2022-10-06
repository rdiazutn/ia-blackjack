import random

# python generar_datos.py 3 para ejecutar

cantidadMazos = 8
#NOTA: los ases siempre valen 1 pero tenes que poner el flag HayAs
valoresPosibles = [1,2,3,4,5,6,7,8,9,10,10,10,10]
class Partida:
    def __init__(self):
        self.manoJugador = []
        self.manoBanca = []
        self.mazo = []
        self.situacion = 0

        # se genera el mazo completo y lo mezclo
        # TODO revisar si se puede multiplicar el array asi nomas
        self.mazo = valoresPosibles * 4 * cantidadMazos
        random.shuffle(self.mazo)
        random.shuffle(self.mazo)
        random.shuffle(self.mazo)
        random.shuffle(self.mazo)

        # se reparten las cartas para el jugador
        for i in range(2):
            carta = self.mazo.pop()
            self.manoJugador.append(carta)

        # se reparten las cartas para la banca
        carta = self.mazo.pop()
        self.manoBanca.append(carta)
        

    def pedirCarta(self):
        carta = self.mazo.pop(0)
        self.manoJugador.append(carta)
        return carta

    def siguienteCarta(self):
        return self.mazo[0]

    def getSituacion(self):
        hayAs = False

        # calculo de la mano del jugador
        cuentaJugador = 0
        for i in self.manoJugador:
            if i == 1:
                hayAs = True
            cuentaJugador = cuentaJugador + i
               
        return  { 'cuenta': cuentaJugador, 'hayAs': hayAs, 'banca': self.getCuentaBanca()}
    
    def quedarse(self):
        # una vez que el jugador decide quedarse la banca tiene que terminar su mano
        while(True):
            carta = self.mazo.pop()
            self.manoBanca.append(carta)
            cuenta = self.getCuentaBanca()
            if cuenta >= 17:
                break

    def getCuentaBanca(self):
        cuentaBanca = 0 
        # dejo los ases al final del array para un calculo mas facil
        self.manoBanca.sort(reverse=True)
        for k in self.manoBanca:
            if k == 1:
                if cuentaBanca > 10:
                    cuentaBanca = cuentaBanca + 1
                else:
                    cuentaBanca = cuentaBanca + 11
            else:
                cuentaBanca += k
        return cuentaBanca
    
    def getResultado(self):
        situacion = self.getSituacion()
        return {'cuenta': situacion['cuenta'], 'hayAs': situacion['hayAs'],  'banca': self.getCuentaBanca()}


def crearMano():
    return Partida()
