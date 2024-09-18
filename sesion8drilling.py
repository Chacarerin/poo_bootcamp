
def crear_archivo():
    archivo = open("informacion.dat", "x")
    archivo.close()

try:
    crear_archivo()
    with open("informacion.dat", "w") as archivo:
        for i in range(1,6):
            archivo.write(f"Datos de información en la línea {i} \n")
except IOError:
    print("El archivo informacion.dat ya existe, ha sido creado previamente")

with open("informacion.dat", "r") as archivo:
    for linea in archivo:
        print(linea, end='') 