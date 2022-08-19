import math
def areaTriangulo(altura,base):
    return int(base)*int(altura)

def areaCirculo(radio):
    return math.pi*math.sqrt(float(radio))

print("Vamos a calcular cosas")
print("El área de un círculo y un triángulo")
base=input("¿cual es la base del tríangulo? ")
altura=input("¿Cual es la altura del tríangulo? ")
radio=input("¿Cual es el radio del círculo? ")
print("El rea del tríangulos es",areaTriangulo(altura,base))
print("El área´del círculo es ",areaCirculo(radio))

