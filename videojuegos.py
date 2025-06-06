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
    
    if opcion == "1":
        while True:
            codigo = int(input("Ingrese el código del videogo: "))
            nombre = input("Ingrese el nombre del videojuego: ")
            if genero.isspace() or genero.isalpha():
                print(" error, Debe ingresar letras o número!")
            else:
                break
        while True:
            genero = input("Ingrese el género del videojuego")
            if genero.isspace() or genero.isalpha():
                print(" error, Ingrese caracteres Validos")
            else:
                break
        print("\nPlataformas disponibles:")
        print("1. PC")
        print("2. PS5")
        print("3. Xbox Series X")
        print("4. Nintendo Switch")
        try:
            plataforma_codigo = int(input("Seleccione el número de la plataforma: "))
        except:
            print("Ingrese caracteres Validos!!")
        plataforma = plataformas[plataforma_codigo -1 ]

        videojuego = {
            "codigo": codigo,
            "nombre": nombre,
            "genero": genero,
            "plataforma": plataforma
        }
        videojuegos.append(videojuego)
        print("Videojuego registrado correctamente")

    elif opcion == "2":
        if len(videojuegos) == 0:
            print("No hay Videojuegos registrados.")
        else:
            print("n\--- LISTA DE VIDEOJUEGOS ---")
            for v in videojuegos:
                print(f"Codigo: {v['codigo']}, nombre: {v['nombre']}, Género: {v['Genero']}, Plataforma: {v['plataforma']}")
    elif opcion == "3":
        try:
            codigo = int(input("Ingrese el codigo del videojiego a modificar: "))
        except:
            print("Ingrese caracteres Validos!!")
        encontrado = False
        for v in videojuegos:
            if v["codigo"] == codigo:
                v["nombre"] = input("Nuevo nombre: ")
                v["genero"] = input("Nuevo género: ")

                print("\nPlataformas disponibles: ")
                print("1. PC")
                print("2. PS5")
                print("3. Xbox Series X")
                print("4. Nintendo Switch")

                try:
                    plataforma_codigo = int(input("Seleccione el número de la nueva plataforma: "))
                except:
                    print("Ingrese caracteres Validos!!.")
                v["plataforma"] = plataforma[plataforma_codigo - 1]

                print("Videojuego modificado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print("Videojuego no encontrado.")
    elif opcion == "4":
        try:
            codigo = int(input("ingrese el código del videouego a eliminar: "))
        except:
            print("Ingrese caracteres Validos!!")
        eliminado = False
        for v in videojuegos:
            if v ["codigo"] == codigo:
                videojuegos.remove(v)
                print("Videojuego eliminado correctamente.")
                eliminado = True
                break
            if not eliminado:
                print("Videojuego no encontrado.")

    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opcion Inválida. ")