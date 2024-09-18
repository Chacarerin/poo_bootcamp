class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def set_edad(self, edad):
        self.edad = edad

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

#objetos
persona_1 = Persona("Pedro", "Vivas", "Masculino", "20 años", "1.78 mts", "68 Kg")
persona_2 = Persona("Juan", "Camargo", "Masculino", "18", "1.8 mts", "75 Kg")

persona_1.set_edad("21 años")
persona_2.set_apellidos("Santiago")

print(persona_1.edad)
print(persona_2.apellidos)