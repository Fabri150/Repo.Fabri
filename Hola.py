while nombre != "adios":
    nombre = input("A quien queres saludar (adios para salir)" )
    print(f"Hola, {nombre}!")
    lol = input("Como estas?")
    match lol:
        case "bien":
            pass