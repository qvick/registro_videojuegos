videojuegos = []

plataformas = ("PC", "PS5", "Xbox Series X", "Nintendo Switch")

while True:
    print("\n--- MENÚ DE VIDEO JUEGOS ---")
    print("1. Regsitrar Video Juego")
    print("2. Ver Video Juego")
    print("3. Modificar Video Juego")
    print("4. Eliminar Video Juego")
    print("5. Salir")

    opcion = input("Seleccione una opcion (1-5): ")

    if opcion == 1:
        codigo = int(input("Ingrese el código del videogo: "))
        nombre = input("Ingrese el nombre del videojuego: ")
        genero = input("Ingrese el género del videojuego")

        print("\nPlataformas disponibles:")
        print("1. PC")
        print("2. PS5")
        print("3. Xbox Series X")
        print("4. Nintendo Switch")
        plataforma_codigo = int(input("Seleccione el número de la plataforma: "))
        plataforma = plataformas[plataforma_codigo -1 ]

        videojuego = {
            "codigo": codigo,
            "nombre": nombre,
            "genero": genero,
            "plataforma": plataforma
        }
        
        videojuegos.append(videojuego)
        print("Videojuego registrado correctamente")
        
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Opcion Inválida. ")