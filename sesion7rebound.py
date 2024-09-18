#Diseñe un programa en Python que pida la edad al usuario por consola. El usuario debe ingresar
#un número entero; en caso contrario, el programa arrojará una excepción y le solicitará que
#ingrese su edad nuevamente.
#Seguidamente, el programa debe imprimir que es Adulto si es mayor o igual a 18; y en caso
#ontrario, no es un adulto.

class Miexcepcion(Exception):
    def __init__ (self,mensaje):
        super().__init__(mensaje)

mensaje = "¡Error! Por favor solo ingresa números enteros como edad."

while True:
    try:
        numero = int(input("Ingrese su edad: "))
        print(f"Gracias por indicar que tu edad es de {numero} años.")
        if numero > 18:
         print("Felicidades, es mayor de edad por tanto es un Adulto.")
        else:
         print("Felicidades, es menor de edad, por tanto no es un adulto.")
        break
    except ValueError:
            raise Miexcepcion(mensaje)

    
        
