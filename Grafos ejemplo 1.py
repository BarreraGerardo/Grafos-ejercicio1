# Lista de 7 estados de la república mexicana
estados_mexicanos = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Coahuila"]

# Lista de costos para visitar cada estado (en pesos mexicanos)
costos_visita = {"Aguascalientes": 1000, "Baja California": 1500, "Baja California Sur": 2000, "Campeche": 1200, "Chiapas": 1800, "Chihuahua": 1600, "Coahuila": 1300}

# Función para recorrer los estados sin repetir
def recorrer_estados_sin_repetir(estados):
    visitados = set()  # Conjunto para almacenar estados visitados sin repetición
    for estado in estados:
        if estado not in visitados:
            print("Visitando:", estado)
            visitados.add(estado)

# Función para recorrer los estados repitiendo al menos un estado
def recorrer_estados_con_repeticion(estados):
    for estado in estados:
        print("Visitando:", estado)

# Función para obtener los costos de visitar cada estado
def obtener_costos(estados, costos):
    total = 0
    for estado in estados:
        costo = costos.get(estado, 0)
        print("Costo de visitar", estado + ":", costo, "pesos")
        total += costo
    print("Costo total de la visita:", total, "pesos")

# Llamada a la función para recorrer los estados sin repetir
print("Recorrido sin repetir estados:")
recorrer_estados_sin_repetir(estados_mexicanos)

# Llamada a la función para recorrer los estados repitiendo al menos un estado
print("\nRecorrido con repetición de estados:")
recorrer_estados_con_repeticion(estados_mexicanos)

# Llamada a la función para obtener los costos de visitar cada estado
print("\nCostos de visitar cada estado:")
obtener_costos(estados_mexicanos, costos_visita)