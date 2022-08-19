class vehiculo:
    def __init__(self,color,ruedas,puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas
    def __str__(self):
        return "{} es el color, {} es la cantidad de ruedas y tiene {} puertas".format(self.color,self.ruedas,self.puertas)
    
    
class coche(vehiculo):
    def __init__(self, color, ruedas, puertas,velocidad,cilindrada):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        return  "color {}, {} km/h, {} ruedas, {} puertas, {} cc".format( self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada )
    
c=coche("verde",4,5,120,6)
print("Coche:",c)
v=vehiculo("azul",4,4)
print("Vehiculo:",v)