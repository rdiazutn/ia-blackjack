import sys
import juego
import csv

CSV_FILE = 'datos.csv'

# Generar datos
if __name__ == "__main__":
    partidas = 1
    desicionMano = {}
    if(len(sys.argv)>= 1):
        partidas = int(sys.argv[1])
    print ("Generando %s partidas" % partidas)
    # inicialmente repartis 2 cartas al jugador y 1 a la banca
    f = open(CSV_FILE, 'w')
    writer = csv.writer(f)
    for i in range(int(partidas)):
        csvData = []
        partida = juego.crearMano()
        partidaData = []
        # trampa
        while(True):
            situacion = partida.getSituacion()
            # { cuenta: N, hayAs: true|false, banca: M, estado: 'jugando'|'perdio'|'gano'|'empato' }
            proximaCarta = partida.siguienteCarta()
            if (proximaCarta + situacion.get('cuenta') > 21):
                partidaData.append({ 'situacion': situacion, 'pedir': False})
                break
            partida.pedirCarta()
            partidaData.append({ 'situacion': situacion, 'pedir': True})
        # banca ?? 
        partida.quedarse()

        # resultado
        resultado = partida.getResultado()
        # { ganador: 'jugador'|'banca'|'empate', cuentaJugador: N, cuentaBanca: M }
        
        # analisis de la mano

        # Si perdí, lo desecho
        # Si gane
        
        if (resultado['ganador'] == 'jugador'):
            # Fijarme si me convenía quedarme antes
            # Busco primera situacion donde mi cuenta era mayor que de la banca y cambio pedir y sus siguientes a false
            pedir=True
            for instancia in partidaData:
                situacion = instancia['situacion']
                # Tomar en cuenta que si se recibió un as en el medio pudo haber sido conveniente quedarse antes(#1).
                asCambiaSituacion = (situacion['hayAs'] and situacion['cuenta']+10>situacion['banca'] and situacion['cuenta']+10 <=21)
                if (situacion['cuenta']>situacion['banca'] or asCambiaSituacion):
                    pedir = False
                    if(asCambiaSituacion):
                        situacion['cuenta']+=10
                instancia['pedir']=pedir
                key = f"{situacion['cuenta']};{'TRUE' if situacion['hayAs'] else 'FALSE'};{situacion['banca']}"
                if(not key in desicionMano):
                    desicionMano[key] = 0
                desicionMano[key] += pedir if 1 else -1 
    # write a row to the csv file

    for key in desicionMano:
        row = ("%s;%s" % (key, 'TRUE' if desicionMano[key] > 0 else 'FALSE' ))
        print("Guardando partida %s" % row)
        writer.writerow([row])
    # close the file
    f.close()