def crear_archivo():
    try:
        archivo = open("informacion.dat", "x")
        archivo.close()
    except FileExistsError:
        print("El archivo informacion.dat ya existe, ha sido creado previamente")
    with open("informacion.dat", "w") as archivo:
        for i in range(1,6):
            archivo.write(f"Datos de información en la línea {i} \n")

def agregar_datos_archivo():
    try:
        with open("informacion.dat", "a") as archivo:
            archivo.write("Este en una nueva línea en el archivo\nagregando la segunda línea del archivo\nfinalizando la línea agregada")
    except FileNotFoundError:
        print("No se encuenta informacion.dat")

def reemplazar_datos():
    try:
        with open("informacion.dat", "r") as archivo:
            texto = archivo.read()
        with open("informacion.dat", "w") as archivo:
            nuevotexto = texto.replace("información", "Procesamiento")
            archivo.write(nuevotexto)
    except FileNotFoundError:
        print("No se encuenta informacion.dat")

crear_archivo()
agregar_datos_archivo()      
reemplazar_datos()


with open("informacion.dat", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea, end="")