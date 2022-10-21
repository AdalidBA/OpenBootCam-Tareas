from functools import reduce

lista = list(range(50))

print("Lista: ",lista)
resultado = list(filter((lambda x: x % 2), lista)) 
print("Los impares: ",resultado)
resultado = reduce( (lambda x, y: x + y), resultado) 
print("La suma es : ",resultado)
