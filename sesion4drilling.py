class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def movimiento(self):
        return f"{self.nombre} está caminando"

class Maratonista(Persona): #hereda de persona unico atributo, nombre
    def movimiento(self):
        return f"{self.nombre} está trotando"
    
class Ciclista(Persona):
    def movimiento(self):
        return f"{self.nombre} está rodando"

persona=Persona("Rubén")

print(Persona.movimiento(persona))
print(Maratonista.movimiento(persona))
print(Ciclista.movimiento(persona))
