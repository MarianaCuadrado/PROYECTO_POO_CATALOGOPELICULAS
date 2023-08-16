#importar clases del archivo clases.py
from clases import *

nombre_catalogo = input("¡BIENVENIDO!\nPor favor, ingrese el nombre del catálogo de películas: ")
catalogo = CatalogoPelicula(nombre_catalogo)

opcion = None

while opcion != 4:
    print("Opciones:")
    print("1. Agregar película")
    print("2. Listar película")
    print("3. Eliminar catalogo de películas")
    print("4. Salir")

    opcion = int (input ("Por favor, ingresa tu opción del 1 al 4: "))

    if opcion == 1:
        nombre_pelicula = input ("Por favor, ingrese el nombre de la pelicula: ")
        pelicula = Pelicula(nombre_pelicula)
        catalogo.agregar_pelicula(pelicula)

    elif opcion == 2:
        catalogo.listar_peliculas()

    
        


