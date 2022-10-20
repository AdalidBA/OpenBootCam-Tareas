f=open("archivo.txt","w")
f.close()
f=open("archvio.text","w")
f.write("hola mundo")
f.close()
f=open("archivo.txt","r")
lineas=f.readlines()
f.close()
for linea in lineas:
    print(linea+"\n")
    