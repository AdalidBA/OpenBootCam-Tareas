paises=input("Escriba algunos paises (separados por coma): ")
setPais=(pais for pais in paises.split(","))
setPais.sort()
print(", ".join(setPais))

