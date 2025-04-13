def mostrar_menu():
    print("\nAgenda de contactos: ")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir del programa" )
    print("-" * 20)
    
def agregar_contacto(agenda):
    nombre = input("Por favor ingrese ell nombre completo del contacto: ")
    telefono = input("Por favor ingrese el número de teléfono: ")
    email = input("Por favor ingrese el correo electrónico: ")

    agenda[nombre] = {'telefono': telefono, 'email': email} 
    # agenda[nombre] = {} # inicializamos la genda con la key nombre y el valor un diccionario con los datos del contacto otro diccionario
    # agenda[nombre] = {'telefono': telefono, 'email': email} # almacenamos el contacto en un diccionario
    print(f"Contacto {nombre} agregado exitosamente.")

def eliminar_contacto(agenda):
    nombre = input("Por favor ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]  # Eliminamos el contacto de la agenda
        print(f"Contacto {nombre} eliminado exitosamente.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")

def buscar_contacto(agenda):
    nombre = input("Por favor ingrese el nombre del contacto a buscar: ")
    if nombre in agenda: ## Verificamos si el contacto existe
        print(f"Contacto encontrado: {nombre}, Teléfono: {agenda[nombre]['telefono']}, Email: {agenda[nombre]['email']}")
    else:
        print(f"\nEl contacto {nombre} no existe en la agenda.")

def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos:")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {info['telefono']}, Email: {info['email']}")
            print("-" * 20)
    else:
        print("No hay contactos en la agenda.")

def agenda_contacto():
    agenda =  {}
    while True:
        mostrar_menu()
        opcion = input("Por favor seleccione una opción: ")
        if opcion == '1':
            agregar_contacto(agenda)
        elif opcion == '2':
            eliminar_contacto(agenda)
        elif opcion == '3':
            buscar_contacto(agenda)
        elif opcion == '4':
            listar_contactos(agenda)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor intente de nuevo.")
                

if __name__ == "__main__":
    agenda_contacto()
# Este código implementa una agenda de contactos sencilla en Python.
