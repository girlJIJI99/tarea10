def cinefacil():
    funciones = {
        "1": {"pelicula": "La Bella y la Bestia", "hora": "18:00"},
        "2": {"pelicula": "Barbie", "hora": "20:00"},
        "3": {"pelicula": "Toy Story", "hora": "22:00"}
    }

    reservas = []

    while True:
        print (" \n Bienvenido a CineFácil ")
        nombre = input("Ingrese su nombre: ")

        print("\n Funciones disponibles: ")
        for clave, funcion in funciones.items():
            print(f"{clave}. {funcion['pelicula']} - {funcion ['hora'] }")

        opcion = input("Seleccione una funcion: ")
        if opcion not in funciones:
            print("Intente de nuevo.")
            continue

        boletos = int(input ("Cuántos boletos desea comprar? ") )
        precio = 50
        total = boletos * precio

        reserva = {
            "nombre": nombre,
            "pelicula": funciones[opcion]["pelicula"],
            "hora": funciones[opcion]["hora"],
            "boletos": boletos,
            "total": total
        }

        reservas.append(reserva)

        print("\n  RESERVA REGISTRADA :")
        print(f"Cliente: {nombre}")
        print(f"Película: { reserva['pelicula'  ]} a las {reserva['hora']}")
        print(f"Boletos: {boletos}")
        print(f"Total a pagar: Q { total}")

        mostrar_todas = input("\nDesea ver todas las reservas? (si/no): ")
        if mostrar_todas.lower() == 's':
            print("\n CONFIRMACION RESERVAS REGISTRADAS:")
            for r in reservas:
                print(r)

        continuar = input("\nDesea hacer otra reserva? (si/no): ")
        if continuar.lower() != 'si':
            break

cinefacil()
