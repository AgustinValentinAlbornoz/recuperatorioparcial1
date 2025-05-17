nombres = []
cantidades = []

salir = True

while salir:
    print("Menú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombres.append(input("Ingrese el nombre del producto: "))
        cantidades.append(int(input("Ingrese la cantidad: ")))
        print("Producto agregado con éxito.")

    elif opcion == "2":
        print("Productos agotados:")
        agotados = False
        for i in range(len(nombres)):
            if cantidades[i] == 0:
                print(f"- {nombres[i]}")
                agotados = True
        if not agotados:
            print("No hay productos agotados.")

    elif opcion == "3":
        producto = input("Ingrese el nombre del producto a actualizar: ")
        if producto in nombres:
            index = nombres.index(producto)
            cantidades[index] = int(input("Ingrese la nueva cantidad: "))
            print("Stock actualizado.")
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        print("Listado de productos:")
        for i in range(len(nombres)):
            print(f"{nombres[i]}: {cantidades[i]} unidades")

    elif opcion == "5":
        print("Gracias por usar el sistema.")
        salir = False

    else:
        print("Opción inválida.")