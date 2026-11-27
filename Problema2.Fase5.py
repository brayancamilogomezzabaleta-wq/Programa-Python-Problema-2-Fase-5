menu = []
print("====================================")
print("     REGISTRO DE PRODUCTOS")
print("====================================")
cantidad = 6
for i in range(cantidad):
    print("\nProducto numero", i + 1)
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoria: ")
    precio = float(input("Ingrese el precio base: $"))
    producto = [nombre, categoria, precio]
    menu.append(producto)
print("\n====================================")
print("       CONFIGURACION PROMOCION")
print("====================================")
categoria_objetivo = input("Ingrese la categoria con promocion: ")
umbral_precio = float(input("Ingrese el precio minimo: $"))
descuento = 0.15
def calcular_precio_final(producto):
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]
    if categoria.lower() == categoria_objetivo.lower() and precio_base > umbral_precio:
        precio_final = precio_base - (precio_base * descuento)
    else:
        precio_final = precio_base
    return precio_final
print("\n====================================")
print("       MENU DEL RESTAURANTE")
print("====================================")
for producto in menu:
    nombre = producto[0]
    precio_base = producto[2]
    precio_final = calcular_precio_final(producto)
    print("\nProducto:", nombre)
    print("Precio base: $", format(precio_base, ".2f"))
    print("Precio final: $", format(precio_final, ".2f"))
    if precio_final < precio_base:
        print("Promocion aplicada: 15% de descuento")
    else:
        print("Promocion no aplicada")
print("\n====================================")
print("          FIN DEL PROGRAMA")
print("====================================")