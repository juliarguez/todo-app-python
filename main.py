tasks = []


def show_tasks():
    if not tasks:
        print("\nNo hay tareas\n")
        return

    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. [{status}] {t['title']}")


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

    if option == "1":
        show_tasks()

    elif option == "2":
        title = input("Nueva tarea: ")
        tasks.append({"title": title, "done": False})
    
    if option == "5":
        break
