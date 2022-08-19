class alumno:
    def __init__(self,nombre, calificacion):
        self.nombre=nombre
        self.calificacion=calificacion
        
    def obtenerdatos(self):
        print("Nombre:",self.nombre)
        print("Calificación:",self.calificacion)
    
    def aprovado(self):
        if self.calificacion<6:
            print("El alumno esta reprovado")
        else:
            print("El alumno esta aprovado")
            
alumno1=alumno("Ricardo",10)
alumno2=alumno("Maria",5)

print(alumno1.obtenerdatos())
print(alumno1.aprovado())
print(alumno2.obtenerdatos())
print(alumno2.aprovado())
