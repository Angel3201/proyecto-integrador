import random

# Lista de opciones del juego
opciones = ["piedra", "papel", "tijera"]
print("Bienvenido a piedra, papel o tijera")

# Los ontadores para llevar las estadísticas de los juegos jugados XD
victorias = 0
derrotas = 0
empates = 0
partidas = 0

def pedir_jugada(opciones):
# Pide la jugada al usuario y valida la entrada.
    jugador = input("Elige: piedra, papel o tijera: ").lower()
    while jugador not in opciones:  # <-- estructura repetitiva para validar
        print("Opción incorrecta escribir de nuevo la opcion seleccionada")
        jugador = input("Elige: piedra, papel o tijera: ").lower()
    return jugador

def generar_cpu(opciones):
    """Genera la jugada de la CPU al azar e imprime el resultado."""
    CPU = random.choice(opciones)
    print(f"La CPU eligió: {CPU}")
    return CPU

def decidir_resultado(jugador, CPU):
# Decide e imprime el resultado de la ronda. Retorna: 'victoria', 'derrota' o 'empate'.
    # Caso de empate
    if jugador == CPU:
        print("Empate")
        return "empate"
    # Casos donde el jugador gana
    elif (jugador == "piedra" and CPU == "tijera") or \
         (jugador == "papel" and CPU == "piedra") or \
         (jugador == "tijera" and CPU == "papel"):
        print("victoria")
        return "victoria"
    # Casos donde el jugador pierde pasa si no es empate ni victoria
    else:
        print("derrota")
        return "derrota"

def preguntar_continuar():
# Pregunta si el usuario desea seguir jugando. Devuelve True/False.
    continuar = input("¿Quieres seguir jugando? (si/no): ").lower()
    while continuar not in ("si", "no"):  # validación de respuesta
        print("Respuesta no válida, escribe si o no")
        continuar = input("¿Quieres seguir jugando? (si/no): ").lower()
    return continuar == "si"

def mostrar_estadisticas(partidas, victorias, derrotas, empates):
# Muestra las estadísticas finales.
    print("Gracias por jugar")
    print(f"Partidas: {partidas}, Victorias: {victorias}, Derrotas: {derrotas}, Empates: {empates}")

# Estructura repetitiva en el que el juego se repite mientras el usuario siga queriendo jugar
while True:
    # Pedir jugada y validarla
    jugador = pedir_jugada(opciones)

    # Elegir jugada de la CPU al azar
    CPU = generar_cpu(opciones)

    # Estructura para decidir el resultado del juego
    resultado = decidir_resultado(jugador, CPU)
    if resultado == "empate":
        empates += 1
    elif resultado == "victoria":
        victorias += 1
    else:
        derrotas += 1

    partidas += 1  # aumentar número de partidas jugadas

    # Preguntar si el jugador quiere continuar
    if not preguntar_continuar():
        # Si no quiere seguir mostrara las estadisticas de la partida
        mostrar_estadisticas(partidas, victorias, derrotas, empates)
        break
