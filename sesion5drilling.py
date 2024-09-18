class Persona:
    def __init__(self, nombre, apellidos, anno):
        self.nombre = nombre
        self.apellidos = apellidos
        self.anno = anno
        
class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto

class Trabajador(Persona,Departamento):
    def __init__(self, nombre, apellidos, anno, nombre_dpto, nombre_corto_dpto, salario):
        Persona.__init__(self, nombre, apellidos, anno)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self.salario = salario

trabajador1=Trabajador("Juan", "Pérez", "2005", "Ingeniería de software", "IS", "20000")

print(trabajador1.__dict__)

print("Es trabajador instancia de persona:", isinstance(trabajador1, Persona))
print("Es trabajador instancia de Departamento:", isinstance(trabajador1, Departamento))
print("Es trabajador instancia de trabajador:", isinstance(trabajador1, Trabajador))
