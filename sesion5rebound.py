class A:
    def __init__(self):
        pass
    def metodo_a(self):
        print("Clase B")
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")

    def metodo_b(self):
        print("Método heredado de B")

class C(A,B):
    def __init__(self):
        super().__init__()
        #print("Clase C")

    def metodo_c(self):
        print("Método de clase C")

c = C()
c.metodo_a()
c.metodo_b()
c.metodo_c()