# Diccionario para almacenar el inventario
inventario = {}

def agregar_producto():
  """
  Función para agregar un producto al inventario.
  """
  nombre_producto = input("Ingresa el nombre del producto: ")
  cantidad = int(input("Ingresa la cantidad: "))

  if nombre_producto in inventario:
    inventario[nombre_producto] += cantidad
    print(f"Se han agregado {cantidad} {nombre_producto} al inventario.")
  else:
    inventario[nombre_producto] = cantidad
    print(f"El producto {nombre_producto} ha sido agregado al inventario con {cantidad} unidades.")

def vender_producto():
  """
  Función para vender un producto del inventario.
  """
  nombre_producto = input("Ingresa el nombre del producto a vender: ")
  cantidad_a_vender = int(input("Ingresa la cantidad a vender: "))

  if nombre_producto in inventario:
    if cantidad_a_vender <= inventario[nombre_producto]:
      inventario[nombre_producto] -= cantidad_a_vender
      print(f"Se han vendido {cantidad_a_vender} {nombre_producto}.")
    else:
      print(f"No hay suficiente stock de {nombre_producto}. Solo hay {inventario[nombre_producto]} unidades disponibles.")
  else:
    print(f"El producto {nombre_producto} no existe en el inventario.")

def mostrar_inventario():
  """
  Función para mostrar el inventario completo.
  """
  if inventario:
    print("Inventario:")
    for producto, cantidad in inventario.items():
      print(f"- {producto}: {cantidad}")
  else:
    print("El inventario está vacío.")

# Bucle principal del programa
while True:
  print("\nBienvenido al sistema de inventario de la tienda.")
  print("1. Agregar un producto al inventario")
  print("2. Vender un producto")
  print("3. Mostrar inventario")
  print("4. Salir")

  opcion = input("Elige una opción: ")

  if opcion == "1":
    agregar_producto()
  elif opcion == "2":
    vender_producto()
  elif opcion == "3":
    mostrar_inventario()
  elif opcion == "4":
    print("¡Hasta luego!")
    break
  else:
    print("Opción no válida. Ingresa una opción del 1 al 4.")
