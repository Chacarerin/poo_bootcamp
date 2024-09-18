#Diseñe un programa en Python que cree un archivo si no se encuentra; en caso de existir el
#archivo, debe reflejar un mensaje que especifica que ya se encuentra el archivo previamente
#creado.
#El archivo por crear debe llamarse informacion.dat. el cual contiene lo siguiente:
#Datos de información en la línea 1
#Datos de información en la línea 2
#Datos de información en la línea 3
#Datos de información en la línea 4
#Datos de información en la línea 5

def crear_archivo():
    archivo = open("informacion.dat", "x")
    archivo.close()

try:
    crear_archivo()
    with open("informacion.dat", "w") as archivo:
        for i in range(1,6):
            archivo.write(f"Datos de información en la línea {i} \n")
except IOError:
    print("El archivo ya existe")