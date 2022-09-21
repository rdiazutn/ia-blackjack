
// juego

const csv = []

// inicialmente repartis 2 cartas al jugador y 1 a la banca
const partida = juego.crearMano()




// trampa
while(true) {
  const situacion = partida.getSituacion()
  // { cuenta: N, hayAs: true|false, banca: M, estado: 'jugando'|'perdio'|'gano'|'empato' }
  const proximaCarta = partida.siguienteCarta()
  if (proximaCarta.valor + situacion.cuenta > 21) {
    csv.push({ situacion, pedir: false})
    break;
  }
  partida.pedirCarta()
  csv.push({ situacion, pedir: true})
}

// banca
partida.quedarse()

// resultado
const resultado = partida.getResultado()
// { ganador: 'jugador'|'banca'|'empate', cuentaJugador: N, cuentaBanca: M }

// analisis de la mano

// Si gane
  // Fijarme si me convenía quedarme antes
  // Busco primera situacion donde mi cuenta era mayor que de la banca y cambio pedir y sus siguientes a false
// Si perdí, lo desecho

// Tomar en cuenta que si se recibió un as en el medio pudo haber sido conveniente quedarse antes(#1).


// Descartar contradicciones