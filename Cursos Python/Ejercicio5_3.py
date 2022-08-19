def calculaBisiesto(anho):
    if anho%4==0:
        return "Es bisiesto"
    else:
        return "No es bisiesto"

anho=input("Escriba un año ")
print(calculaBisiesto(int(anho)))