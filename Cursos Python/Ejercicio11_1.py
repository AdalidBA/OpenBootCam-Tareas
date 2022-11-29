import sqlite3

nombre=input("nombre del alumno: ")

con=sqlite3.connect("Cursos Python/alumnos.db")
cur=con.cursor()
sql="select * from nombres where nombre like '%{}%'".format(nombre)
cur.execute(sql)
datos=cur.fetchall()
if len(datos) ==0:
    print("No se encontro alumno")
else:
    for dato in datos:
        print(dato)
cur.close()
con.close()