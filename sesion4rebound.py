class Libro:
    def __init__(self, author, title, year_of_publishment):
        self.author = author
        self.title = title
        self.year_of_publishment = year_of_publishment

libro_1=Libro("Dan Brown", "infierno", None)
libro_2=Libro("Dan Brown", "El código Da Vinci", "2003")

print(libro_1.__dict__)
print(libro_2.__dict__)
    