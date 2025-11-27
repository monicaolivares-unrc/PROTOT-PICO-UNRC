#HERRERA NERI YEIMI ALEJANDRA
#EJEMPLO 1 DE MATRIZ

# Definir la matriz (una lista que contiene dos listas)
matriz = [
    [10, 20],  # Fila 0
    [30, 40]   # Fila 1
]

# Se quiere ver el número 30.
# Está en la Fila 1 (la segunda lista) y Columna 0 (primer número)
numero = matriz[1][0]
print(f"El número seleccionado es: {numero}")

#EJEMPLO 2 DE MATRIZ
# Crear la matriz
ropero = [
    ["Camisas", "Gorras"],      # Fila 0 
    ["Pantalones",   "Calcetines"]   # Fila 1 
]

# Quiero las gorras.
# Están en la Fila (0) y en el Cajón Derecho Fila (1).
prenda = ropero[0][1]

print(f"En ese cajón hay: {prenda}")

print("------------------------------------")

#HERRERA NERI YEIMI ALEJANDRA
#EJEMPLO 1 DE QUEUES
invitados = ["Yeimi", "Derek", "Carlos"]

# append() para añadir a "Fati" al final
invitados.append("Fati") 

print(invitados)
# Resultado: ['Ana', 'Luis', 'Carlos', 'Fati']

#EJEMPLO 2 DE QUEUES
# Agregar canciones (Enqueue con .append()) Append se utiliza para agregar un nuevo elemento de la lista y colocarlo hasta al final

musica = []
musica.append("Pop")    # La primera en reproducir
musica.append("Rock")   # La segunda en reproducir
 
print(f"Reproducir: {musica}") 
# Resultado: ['Pop', 'Rock']

#La canción empieza a sonar y sale de la cola (Dequeue con .pop(0)) Dequeue se utiliza para agregar un elemento a la lsta y colocarlo en el inicio

sonando = musica.pop(0) 
print(f"Sonando ahora: {sonando}")
# Resultado: Pop

