import os

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def __str__(self):
        return f'Nombre: {self.__nombre}'
       
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre


class CatalogoPelicula:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f'{self.nombre}.txt'
        self.peliculas = []

    def agregar_pelicula(self, pelicula): 
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
            self.peliculas.append(pelicula)
            print("¡Película agregada al catálogo!")

    def listar_peliculas(self):
        with open(self.ruta_archivo, 'r') as archivo:
            print (f"Listado de películas del catálogo '{self.nombre}': ")
            print(archivo.read())
            
    
                
    def eliminar_catalogo(self):
        os.remove(self.ruta_archivo)
        print(f'Catálogo: "{self.ruta_archivo}" eliminado')
