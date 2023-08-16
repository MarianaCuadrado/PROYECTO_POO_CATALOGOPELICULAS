#importar clases del archivo clases.py
from clases import *

nombre_catalogo = input("¡BIENVENIDO!\nIngrese el nombre del catálogo de películas: ")
catalogo = CatalogoPelicula(nombre_catalogo)

opcion = None

while opcion != 4:
    try: 
        print("Elige una de las siguientes opciones:")
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

        elif opcion == 3:
            catalogo.eliminar_catalogo()

        elif opcion == 4:
            print("Programa finalizado")
    except Exception as e:
        print("No existen películas en este catálogo")
    else:
        print("Por favor, ingrese una opción válida")
        


