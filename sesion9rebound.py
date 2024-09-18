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

def agregar_datos_archivo():
    try:
        archivo = open("informacion.dat", "a")
        archivo.write("Hola Mundo \nEste en una nueva línea en el archivo\nagregando la segunda línea del archivo\nfinalizando la línea agregada")
        archivo.close()
    except FileNotFoundError:
        print("No se encuenta informacion.dat")

agregar_datos_archivo()

archivo = open("informacion.dat")
lineas = archivo.readlines()
for linea in lineas:
    print(linea, end="")