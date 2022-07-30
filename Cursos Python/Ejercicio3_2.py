import math
peso=input("Escriba su peso en kilogramos: ")
estatura=input("escriba su estatura en metros: ")
print("Su masa corporal es de "+str(round(((float(peso))/math.sqrt(float(estatura))),2)))