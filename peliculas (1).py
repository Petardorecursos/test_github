import time
import os
# Creo una Función para guardar la información de las películas en un archivo
def guardar_peliculas(peliculas, nombre_archivo):
     # Abrimos el archivo en modo escritura ('w'), si el archivo no existe, se crea; si existe, se sobrescribe
    with open(nombre_archivo, 'w') as archivo:
        # escribimos sobre cada película en la lista de películas
        for pelicula in peliculas:
             # hacemos que sea una cadena de texto separada por comas y la escribimos en el archivo
            archivo.write(','.join(pelicula) + '\n')

# Creo una Función para buscar películas por studio
def buscar_por_studio(peliculas, studio):
    peliculas_studio = []
     # escribimos sobre cada película en la lista de películas
    for pelicula in peliculas:
        # Comparamos el studio de la película con el studio buscado (ignorando mayúsculas/minúsculas) gracias a la funcion lower
        if pelicula[1].lower() == studio.lower():
            # Si el Studio coincide, añadimos la película a la lista de películas del Studio
            peliculas_studio.append(pelicula)
    return peliculas_studio

# defino funcion que hace funcionar el programa
def main():
    peliculas = []
    # Ciclo Para que el usuario ingrese toda la informacion
    while True:
        os.system("cls")
        titulo = input("Ingrese el título de la película (o 'fin' para terminar): ")
        # Si el usuario ingresa 'fin', terminamos el ciclo (nos da igual si es mayuscula gracias a la funcion lower)
        if titulo.lower() == 'fin':
            os.system("cls")
            break
        studio = input("Ingrese el studio de la película: ")
        anio = input("Ingrese el año de estreno de la película: ")
        # Añadimos la información de la película como una tupla a la lista de películas
        peliculas.append((titulo, studio, anio))

 # Pedimos al usuario que ingrese el nombre del studio para buscar sus películas
    studio_buscar = input("Ingrese el nombre del studio para buscar sus películas: ")
    os.system("cls")
     # Llamamos a la función buscar_por_studio para obtener las películas del studio especificado
    peliculas_encontradas = buscar_por_studio(peliculas, studio_buscar)

 # Mostramos las películas encontradas del studio especificado
    print("\nPelículas encontradas del studio", studio_buscar, ":")
    for pelicula in peliculas_encontradas:
        print("Título:", pelicula[0], ", Studio:", pelicula[1], ", Año de estreno:", pelicula[2])

 # Guardamos la información de todas las películas en un archivo
    guardar_peliculas(peliculas, 'peliculas.txt')
    print()
    time.sleep(4)
    print("La información de las películas ha sido guardada en 'peliculas.txt'.")
    time.sleep(4)


# while True para activar si o si la funcion main
while True:
    main()
    break
