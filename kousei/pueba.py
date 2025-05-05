# EJEMPLO:
clientes = {
    "mesa1": {
        "nombre": "Mesa 1",
        "mozo": "Mozo 1",
        "pedido": []
    },
    "mesa2": {
        "nombre": "Mesa 2",
        "mozo": "Mozo 2",
        "pedido": []
    },
}

def carta_platos():
    platos = {
        "1. Lomo Saltado": 35.00,
        "2. Ceviche": 35.00,
        "3. Causa limeña": 25.00,
        "4. Arroz con pollo": 20.00,
        "5. Aji de gallina": 20.00,
        "6. Pollo a la brasa": 24.00,
        "7. Papa Rellena": 25.00,
        "8. Chicharron de pescado": 30.00,
        "9. Tallarines verdes": 25.00,
        "10. Tallarines Rojos": 25.00
        }
    
    print("--" * 30)
    print("<< MENU DE PLATILLOS DE FONDO >>".center(60))
    print("--" * 30)
    print("Platillos:", " "*28, "Precio:")
    for plato, precio in platos.items():
        print(f"{plato:<40} s/. {precio:.2f}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return platos
    

carta_platos()
eleccion = int(input("Elegir: "))
for opcion in 10:
    if eleccion == eleccion+1:
        clientes[opcion] = eleccion  


print (clientes)