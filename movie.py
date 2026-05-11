# Write your code here!
# FREEZE CODE BEGIN

class Movie:
    def _init_(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def _str_(self):
        return f"Movie: {self.title} (Directed by {self.director}, {self.year})"

if _name_ == "_main_":
    titulo = input("Ingrese el título de la película: ")
    director = input("Ingrese el director: ")
    anio = input("Ingrese el año: ")

    mi_pelicula = Movie(titulo, director, anio)
    print(mi_pelicula)