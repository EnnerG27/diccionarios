# Diccionario para almacenar los contactos
contactos = {}

def agregar_contacto():
  """
  Función para agregar un nuevo contacto a la agenda.
  """
  nombre = input("Ingresa el nombre del contacto: ")
  numero_telefono = input("Ingresa el número de teléfono: ")
  contactos[nombre] = numero_telefono
  print(f"El contacto {nombre} ha sido agregado correctamente.")

def buscar_contacto():
  """
  Función para buscar un contacto en la agenda.
  """
  nombre = input("Ingresa el nombre del contacto: ")
  if nombre in contactos:
    numero_telefono = contactos[nombre]
    print(f"El número de teléfono de {nombre} es: {numero_telefono}")
  else:
    print(f"El contacto {nombre} no existe en la agenda.")

def mostrar_contactos():
  """
  Función para mostrar todos los contactos almacenados en la agenda.
  """
  if contactos:
    print("Contactos:")
    for nombre, numero_telefono in contactos.items():
      print(f"- {nombre}: {numero_telefono}")
  else:
    print("No hay contactos almacenados en la agenda.")

def actualizar_numero():
  """
  Función para actualizar el número de teléfono de un contacto existente.
  """
  nombre = input("Ingresa el nombre del contacto a actualizar: ")
  if nombre in contactos:
    nuevo_numero = input("Ingresa el nuevo número de teléfono: ")
    contactos[nombre] = nuevo_numero
    print(f"El número de teléfono de {nombre} ha sido actualizado correctamente.")
  else:
    print(f"El contacto {nombre} no existe en la agenda.")

def eliminar_contacto():
  """
  Función para eliminar un contacto de la agenda.
  """
  nombre = input("Ingresa el nombre del contacto a eliminar: ")
  if nombre in contactos:
    del contactos[nombre]
    print(f"El contacto {nombre} ha sido eliminado correctamente.")
  else:
    print(f"El contacto {nombre} no existe en la agenda.")

# Bucle principal del programa
while True:
  print("\nBienvenido a la gestión de contactos.")
  print("Opciones:")
  print("1. Agregar un contacto.")
  print("2. Buscar un contacto.")
  print("3. Mostrar todos los contactos.")
  print("4. Actualizar número de teléfono.")
  print("5. Eliminar un contacto.")
  print("6. Salir.")

  opcion = input("Ingresa tu opción: ")

  if opcion == "1":
    agregar_contacto()
  elif opcion == "2":
    buscar_contacto()
  elif opcion == "3":
    mostrar_contactos()
  elif opcion == "4":
    actualizar_numero()
  elif opcion == "5":
    eliminar_contacto()
  elif opcion == "6":
    print("¡Hasta luego!")
    break
  else:
    print("Opción no válida. Ingresa una opción del 1 al 6.")
