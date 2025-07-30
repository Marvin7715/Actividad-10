lista_productos = []

print (".........Inventario de productos........")

for _ in range(productos):
    print(f"producto {productos+1}: ")
    productos = int(input("¿Cuántos productos desea ingresar?: "))

    codigo = input("Código del producto: ")
    nombre_producto = input("Nombre del producto: ")
    categoria = input ("¿Cúal es la categoria del producto?: ")
    talla = input("Ingrese la talla del producto en letras 'Eje. M,S,L': ")
    precio = int(input("Precio unitario mayor a 0, Q: "))
    stock = int(input("Cantidad en stock: "))


    inventario = {
    "codigo": codigo,
    "nombre_producto": nombre_producto,
    "categoria": categoria,
    "talla": talla,
    "precio": precio,
    "stock": stock
    }