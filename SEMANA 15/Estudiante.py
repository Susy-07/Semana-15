estudiantes = ["Carlos Pacheco", "Sofia Lopez", "Kedin Calderon", "Joshi Salazar", "Luis Gómez" ]

def mostrar_menu():
    print("\n" + "="*35)
    print("    SISTEMA DE REGISTRO DE ESTUDIANTES")
    print("="*35)
    print("1. Agregar estudiante")
    print("2. Ver todos los estudiantes")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
    return input("Elige una opción: ")

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        nombre = input("Escribe el nombre completo: ")
        estudiantes.append(nombre)
        print(f"'{nombre}' agregado correctamente")
    elif opcion == "2":
        if not estudiantes:
            print("No hay estudiantes registrados")
        else:
            print("\nLista de estudiantes:")
            for indice, nombre in enumerate(estudiantes, start=1):
                print(f"   {indice}. {nombre}")
            print(f"\nTotal: {len(estudiantes)} estudiantes")
    elif opcion == "3":
        buscar = input("Nombre a buscar: ")
        if buscar in estudiantes:
            print(f"{buscar} ESTÁ en la lista")
        else:
            print(f"´{buscar}´ NO está registrado")
    elif opcion == "4":
        borrar = input("Nombre a eliminar: ")
        if borrar in estudiantes:
            estudiantes.remove(borrar)
            print(f"'{borrar}' eliminado")
        else:
            print(f"No se encontró ese nombre")

    elif opcion == "5":
        print("\nPrograma finalizado")
        break

    else:
        print("Opción no válida, intenta de nuevo")