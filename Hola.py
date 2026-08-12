while nombre != "adios":
    nombre = input("A quien queres saludar (adios para salir)" )
    print(f"Hola, {nombre}!")
    estado = input("Como estas?")
    match estado:
        case "bien":
            pass