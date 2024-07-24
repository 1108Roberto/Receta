import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('recetas.db')
c = conn.cursor()

# Crear tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS recetas
             (id INTEGER PRIMARY KEY, nombre TEXT, ingredientes TEXT, pasos TEXT)''')

def agregar_receta():
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes (separados por comas): ")
    pasos = input("Ingrese los pasos: ")
    c.execute("INSERT INTO recetas (nombre, ingredientes, pasos) VALUES (?, ?, ?)",
              (nombre, ingredientes, pasos))
    conn.commit()
    print("Receta agregada exitosamente.")

def actualizar_receta():
    id = input("Ingrese el ID de la receta que desea actualizar: ")
    nombre = input("Ingrese el nuevo nombre de la receta: ")
    ingredientes = input("Ingrese los nuevos ingredientes (separados por comas): ")
    pasos = input("Ingrese los nuevos pasos: ")
    c.execute("UPDATE recetas SET nombre = ?, ingredientes = ?, pasos = ? WHERE id = ?",
              (nombre, ingredientes, pasos, id))
    conn.commit()
    print("Receta actualizada exitosamente.")

def eliminar_receta():
    id = input("Ingrese el ID de la receta que desea eliminar: ")
    c.execute("DELETE FROM recetas WHERE id = ?", (id,))
    conn.commit()
    print("Receta eliminada exitosamente.")

def ver_recetas():
    c.execute("SELECT id, nombre FROM recetas")
    recetas = c.fetchall()
    if recetas:
        for receta in recetas:
            print(f"ID: {receta[0]}, Nombre: {receta[1]}")
    else:
        print("No hay recetas disponibles.")

def buscar_receta():
    id = input("Ingrese el ID de la receta que desea buscar: ")
    c.execute("SELECT nombre, ingredientes, pasos FROM recetas WHERE id = ?", (id,))
    receta = c.fetchone()
    if receta:
        print(f"Nombre: {receta[0]}")
        print(f"Ingredientes: {receta[1]}")
        print(f"Pasos: {receta[2]}")
    else:
        print("Receta no encontrada.")

def main():
    while True:
        print("\nOpciones:")
        print("1) Agregar nueva receta")
        print("2) Actualizar receta existente")
        print("3) Eliminar receta existente")
        print("4) Ver listado de recetas")
        print("5) Buscar ingredientes y pasos de receta")
        print("6) Salir")
        
        opcion = input("Seleccione una opción: ").lower()

        if opcion == '1':
            agregar_receta()
        elif opcion == '2':
            actualizar_receta()
        elif opcion == '3':
            eliminar_receta()
        elif opcion == '4':
            ver_recetas()
        elif opcion == '5':
            buscar_receta()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
    conn.close()
