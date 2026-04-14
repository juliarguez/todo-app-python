tasks = []

while True:
    print("""
=== TO-DO APP ===
1. Ver tareas
2. Añadir tarea
3. Eliminar tarea
4. Completar tarea
5. Salir
""")

    option = input("Opción: ")

    if option == "5":
        break