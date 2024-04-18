import math

# Función para calcular la circunferencia dado un radio
def calcular_circunferencia(radio):
    pi = round(math.pi, 6)  # Valor de pi con 6 decimales
    circunferencia = 2 * pi * radio
    return circunferencia

# Valores de radio
radios = [3, 8, 10]

# Calcular y mostrar la circunferencia para cada radio
for radio in radios:
    circunferencia = calcular_circunferencia(radio)
    print (f"Para un radio de {radio}, la circunferencia es: {circunferencia:.6f}")
