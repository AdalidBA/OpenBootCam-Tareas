class vehiculo:
    color="verde"
    ruedas=4
    puertas=5
    
class coche(vehiculo):
    velocidad=120
    cilindrada=4
    
c=coche()
print(dir(c))