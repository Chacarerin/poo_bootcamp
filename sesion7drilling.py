#Diseñe una nueva clase de excepción definida por el usuario, que gestione la entrada del valor de
#una variable salario, y la misma se encuentre entre los valores de 1000 y 2000; de lo contrario, se
#lanza una excepción que refleja que el salario no se encuentra en el rango de 1000 y 2000.

#Ingrese el salario: 5000
#Traceback (most recent call last):
# File "drilling-CUE07.py", line 20, in <module>
# raise RangoSalarioError(salario)
#__main__.RangoSalarioError: 5000 -> Salario no está definido en el
#rango (1000 a 2000)

class RangoSalarioError(Exception):
    def __init__ (self,salario):
        self.salario = salario
        super().__init__(f"{salario} -> Salario no está definido en el rango (1000 a 2000)")

try:
    salario = int(input("Ingrese el salario: "))
    print(f"Gracias por indicar que su rango de salario es de {salario}.")
    if salario >= 1000 and salario <= 2000:
        print("Gracias por la información.")
    else:
        raise RangoSalarioError(salario)
except ValueError:
    raise RangoSalarioError()
    