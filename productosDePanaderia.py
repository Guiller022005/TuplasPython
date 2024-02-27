# Diccionarios para productos y descuentos de una tienda
# Diccionario de productos x categoria
productos = {
    "Pan": ["Baguette", "Pan de molde", "Pan integral", "Pan de centeno"],
    "Dulces": ["Croissant", "Donuts", "Palmeras de chocolate", "Tarta de manzana"],
    "Pastelería": ["Tarta de frutas", "Eclairs", "Napolitanas de crema", "Empanadas de carne"]
}
# Diccionario de precios
precios = {
    "Baguette": 5000,
    "Pan de molde": 4500,
    "Pan integral": 5500,
    "Pan de centeno": 6000,
    "Croissant": 3500,
    "Donuts": 3000,
    "Palmeras de chocolate": 4000,
    "Tarta de manzana": 7000,
    "Tarta de frutas": 8000,
    "Eclairs": 2500,
    "Napolitanas de crema": 3500,
    "Empanadas de carne": 4000
}

# Diccionario de promociones 
promociones_panaderia = {
    "Pan": {"Descuento 10% en la compra de 2 unidades o más": 0.1, "Llévate 3 y paga 2 en panes integrales": 3},
    "Dulces": {"2x1 en croissants": 0.5, "Descuento del 15% en palmeras de chocolate": 0.15},
    "Pastelería": {"Tarta de frutas a mitad de precio en la compra de una tarta de manzana": 0.5, "Descuento del 20% en eclairs": 0.2}
}

for indice, categoria in enumerate(productos, start=1):
    print(f"{indice}. {categoria}")

# Solicitar al cliente q ingrese una categoria
opcion = int(input("Selecciona una categoria")) - 1
categoria_seleccionada = list(productos.keys())[opcion]
print(f"Usuario, usted seleccionó la categoría '{categoria_seleccionada}'")

# Mostrar productos disponibles y mostrar la opcion deacuerdo al producto seleccionado
print(f"Productos disponibles en la categoría '{categoria_seleccionada}': {productos[categoria_seleccionada]}")

producto_seleccionado = input("Selecciona un producto: ")
if producto_seleccionado in precios:
    precio_producto = precios[producto_seleccionado]
    print(f"El producto '{producto_seleccionado}' tiene un precio de ${precio_producto}")

    dinero = int(input("Ingrese la cantidad de dinero disponible: "))

    if dinero >= precio_producto:
        vueltos = dinero - precio_producto
        print(f"Usted compró el producto '{producto_seleccionado}' con un valor de ${precio_producto}, sus vueltos son ${vueltos}")
    else:
        print(f"Lo sentimos, el producto '{producto_seleccionado}' con un valor de ${precio_producto} está fuera de su presupuesto.")
else:
    print("Lo sentimos, el producto seleccionado no está disponible en esta categoría.")

