inventario = {}

print(".........Inventario de productos.........")
cantidad = int(input("¿Cuántos productos desea ingresar?: "))

for i in range(cantidad):
    print(f"\nProducto #{i + 1}:")

    while True:
        codigo = input("Código del producto (ej. P001): ").strip()
        if codigo in inventario:
            print("Este código ya existe. Ingrese un código diferente.")
        else:
            break

    nombre_producto = input("Nombre del producto: ").strip()
    categoria = input("¿Cuál es la categoría del producto? (Hombre/Mujer/Niño): ").strip()
    talla = input("Ingrese la talla del producto (S, M, L, XL): ").strip().upper()

    precio = float(input("Ingrese el precio unitario (mayor a Q0.00): Q"))
    if precio <= 0:
        print("El precio debe ser mayor a Q0.00. Se asignará Q0.01 por defecto.")
        precio = 0.01

    stock = int(input("Ingrese la cantidad en stock (entero positivo): "))
    if stock < 0:
        print("La cantidad debe ser un número entero positivo. Se asignará 0 por defecto.")
        stock = 0

    inventario[codigo] = {
        "nombre": nombre_producto,
        "categoria": categoria,
        "talla": talla,
        "precio": precio,
        "stock": stock
    }

print("\nLista de productos registrados:")
for codigo, datos in inventario.items():
    print(f"\nCódigo: {codigo}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Categoría: {datos['categoria']}")
    print(f"Talla: {datos['talla']}")
    print(f"Precio unitario: Q{datos['precio']:.2f}")
    print(f"Cantidad en stock: {datos['stock']}")

print("\nBúsqueda de producto")
buscado = input("Ingrese el código del producto que desea buscar: ").strip()

if buscado in inventario:
    producto = inventario[buscado]
    print("\nProducto encontrado:")
    print(f"Nombre: {producto['nombre']}")
    print(f"Categoría: {producto['categoria']}")
    print(f"Talla: {producto['talla']}")
    print(f"Precio unitario: Q{producto['precio']:.2f}")
    print(f"Cantidad en stock: {producto['stock']}")
else:
    print("Producto no encontrado.")

valor_total = 0
for datos in inventario.values():
    valor_total += datos['precio'] * datos['stock']

print(f"\nValor total del inventario: Q{valor_total:.2f}")

categorias = {}
for datos in inventario.values():
    categoria = datos['categoria']
    if categoria in categorias:
        categorias[categoria] += 1
    else:
        categorias[categoria] = 1

print("\nCantidad de productos por categoría:")
for categoria, cantidad in categorias.items():
    print(f"{categoria}: {cantidad} productos")