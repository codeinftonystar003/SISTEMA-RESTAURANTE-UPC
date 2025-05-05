def menu_opcion2():
    print("--" * 30)
    print("<< OPCION 2 >>".center(60))
    print("Elegir opcion: ")
    print("1. Añadir items")
    print("2. Eliminar items")
    print("3. Registrar hora de inicio y final")
    print("[0. Regresar]")
def cartas():
    print("--" * 30)
    print("<< BIENVENIDO AL MENU >>".center(60))
    print("Seleccionar que desea: ")
    print("1. Platos")
    print("2. Postres")
    print("3. Bebidas")
    print("[0. Salir]")
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
def carta_postres():
    postres= {
        "1. Mazamorra morada": 12.00,
        "2. Arroz con leche": 12.00,
        "3. Suspiro a la limeña": 10.00,
        "4. Picarones": 15.00,
        "5. Alfajores": 10.00,
        "6. Torta de chocolates": 18.00,
        "7. Turron": 15.00,
        "8. King kong de manjar blanco":12.00
    }
    
    print("--" * 30)
    print("<< MENU DE POSTRES >>".center(60))
    print("Postres:", " "*30, "Precios:")
    for postres, precios in postres.items():
        print (f"{postres:<40} s/. {precios:.2f}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return postres
def carta_bebidas():
    bebidas = {
        "1. Chicha morada": 18.00,
        "2. Chicha de jora": 18.00,
        "3. CocaCola": 10.00,
        "4. InkaCola": 10.00,
        "5. Jugo natural": 10.00,
        "6. Cafe": 6.00,
        "7. Pisco Sour": 20.00,
        "8. Chilcano de pisco": 18.00   
    }
    print("--" * 30)
    print("<< MENU DE BEBIDAS >>".center(60))
    print("--" * 30)
    print("Bebidas:", " "*30, "Precio:")
    for bebida, precio in bebidas.items():
        print(f"{bebida:<40} s/. {precio:.2f}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return bebidas


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

def menu ():
    print("OPCION:")
    print("2. pedido por mesa")
menu()

def existe_mesa(mesa):
    return mesa in clientes


while True:
    opcion = int(input ("Ingresar opcion: "))
    if opcion == 2:
        menu_opcion2()
        opcion = int(input ("Ingresar opcion: "))
        if opcion == 1:
            cartas()
            opcion = int(input("Ingresar opcion deseada: "))
            if opcion == 1:
                carta_platos()
            elif opcion == 2:
                carta_postres()
            elif opcion == 3:
                carta_bebidas()
            elif opcion == 0:
                print("Regresando...")
        elif opcion == 2:
            print("Eliminar pedido de la mesa")
            mesa = input("Ingrese el nombre de la mesa: ")
            if existe_mesa(mesa):
                print("Mesa encontrada.")
                print("Pedido actual:", clientes[mesa]["pedido"])
                item = input("Ingrese el item a eliminar: ")
                if item in clientes[mesa]["pedido"]:
                    clientes[mesa]["pedido"].remove(item)
                    print(f"Item '{item}' eliminado de la mesa {mesa}.")
                else:
                    print(f"Item '{item}' no encontrado en la mesa {mesa}.")
            else:
                print("Mesa no encontrada.")
        elif opcion == 3:
            print("Registrar hora de inicio y final")
        elif opcion == 0:
            break
            
print (clientes)