productos = tuple((
    "Agua",
    "Café",
    "Té", 
    "Jugo", 
    "Refresco", 
    "Cerveza", 
    "Vino", 
    "Leche", 
    "Smoothie", 
    "Limonada"))
precios = tuple((3000, 
                6000, 
                5000, 
                4000, 
                3500, 
                10000, 
                20000, 
                2500, 
                9000, 
                4500))
for i,val in enumerate(productos):
    print(f"""       {i}. {val} ${precios[i]} """)
opcion = int(input("Selecciona una opcion"))
print(f"Usuario usted selecciono el producto {productos[opcion]} con un valor de ${precios[opcion]}")
dinero = int(input("Ingrese la cantidad de dinero disponible"))
if dinero >= precios[opcion]:
    vueltos = dinero - precios[opcion]
    print(f"Usuario usted compro el producto{productos[opcion]} con un valor de ${precios[opcion]}, sus vueltos son ${vueltos}")
else:
    print(f"Usuario el producto que desea comprar {productos[opcion]} con un valor de ${precios[opcion]}, le falta un total de ${precios[opcion] - dinero} ")
11