paises=input("Escriba algunos paises (separados por coma): ")
paisessplt=paises.split(',')
paisessplt.sort()
setpais=set()
print(paisessplt)
for pais in paisessplt:
    if pais not in setpais or  not pais=='':
        setpais.add(pais.capitalize())
        print(setpais)
lista=""
print(", ".join(setpais))

