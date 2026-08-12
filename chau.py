while nombre != "hola":
    nombre = input("A quien queres despedir (hola para salir)" )
    print(f"Chau, {nombre}!")
    estado = input("Como estas?")  
    match estado:
        case "mal":
            pass