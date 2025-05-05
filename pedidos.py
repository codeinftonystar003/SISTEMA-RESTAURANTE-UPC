# TODO Alexis Huaman-----------------------------------------------------------------------------------------
#---------------------------(Registro de pedidos)
from tabulate import tabulate
import Registros as r
lista_clientes = []
lista_platos = []
lista_postres = []
lista_bebidas = []
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
        1: ["Lomo Saltado", 35.00],
        2: ["Ceviche", 35.00],
        3: ["Causa limeña", 25.00],
        4: ["Arroz con pollo", 20.00],
        5: ["Aji de gallina", 20.00],
        6: ["Pollo a la brasa", 24.00],
        7: ["Papa Rellena", 25.00],
        8: ["Chicharron de pescado", 30.00],
        9: ["Tallarines verdes", 25.00],
        10: ["Tallarines Rojos", 25.00]
        }
    print("--" * 30)
    print("<< MENU DE PLATILLOS DE FONDO >>".center(60))
    print("--" * 30)
    print("Platillos:", " "*28, "Precio:")
    for i, (nombre_precios) in enumerate(platos.values(), start=1):
        print(f"{i}. {nombre_precios[0]:<40} s/. {nombre_precios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return platos
def carta_postres():
    postres= {
        1: ["Mazamorra morada", 12.00],
        2: ["Arroz con leche", 12.00],
        3: ["Suspiro a la limeña", 10.00],
        4: ["Picarones", 15.00],
        5: ["Alfajores", 10.00],
        6: ["Torta de chocolates", 18.00],
        7: ["Turron", 15.00],
        8: ["King kong de manjar blanco",12.00]
    }
    print("--" * 30)
    print("<< MENU DE POSTRES >>".center(60))
    print("Postres:", " "*30, "Precios:")
    for num, nombre_precios in enumerate(postres.values(),start=1):
        print (f"{num}.{nombre_precios[0]:<40} s/. {nombre_precios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return postres
def carta_bebidas():
    bebidas = {
        1: ["Chicha morada", 18.00],
        2: ["Chicha de jora", 18.00],
        3: ["CocaCola", 10.00],
        4: ["InkaCola", 10.00],
        5: ["Jugo natural", 10.00],
        6: ["Cafe", 6.00],
        7: ["Pisco Sour", 20.00],
        8: ["Chilcano de pisco", 18.00]
    }
    print("--" * 30)
    print("<< MENU DE BEBIDAS >>".center(60))
    print("--" * 30)
    print("Bebidas:", " "*30, "Precio:")
    for num, nombre_precios in enumerate(bebidas.values(), start=1):
        print(f"{num}.{nombre_precios[0]:<40} s/. {nombre_precios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return bebidas



def guardar_cliente(numero_mesa, mozo_asignado, lista_platos, lista_postres, lista_bebidas):
    cliente = {
        "N_Mesa": numero_mesa,
        "N_Mozo" : mozo_asignado,
        "plato" : lista_platos,
        "postre" : lista_postres,
        "bebida" : lista_bebidas 
    }
    lista_clientes.append(cliente)
def mostrar_cliente():
    if not lista_clientes:
        print("La lista esta vacia")
    else:
        print("El mozo asignado es: ", lista_clientes[0]["N_Mozo"])
        print(tabulate(lista_clientes,headers="keys",tablefmt="grid"))
        
def registrar_pedido():
    
    plato = "Sin pedir"
    postre = "Sin pedir"
    bebida = "Sin pedir"
    
    
    
    while True:
        existe_mesa = False
        numero_mesa = int(input("Ingrese el numero de  mesa a registrar (1 - 100): "))
        if 1<= numero_mesa <= 100:
            for  id  in r.Lista_mesas:
                if id["numero_mesa"] == numero_mesa:
                    existe_mesa = True
                    break
        if existe_mesa:
            break
        else:
            print("Error, el numero de mesa no es correcto")     
    
    while True:
        print("--" * 30)
        print("<< BIENVENIDO AL MENU >>".center(60))
        print("Seleccionar que desea: ")
        print("1. Platos")
        print("2. Postres")
        print("3. Bebidas")
        print("[0. Salir]")
        opcion = int(input ("Ingresar opcion: "))
        if opcion == 1:
            platos = carta_platos()
            while True:
                opcion = int(input("Elegir opcion de plato: "))
                if 1<= opcion <= 10:
                    plato = platos[opcion] # platos[opcion] = nombre, precio
                    lista_platos.append(plato)
                    break
                else:
                    print("No existe opcion.")
        elif opcion == 2:
            postres = carta_postres()
            while True:
                opcion = int(input("Elegir opcion del postre: "))
                if 1<= opcion <= 8:
                    postre = postres[opcion] # 
                    lista_postres.append(postre)
                    break
                else:
                    print("No existe opcion.")
        elif opcion == 3:
            bebidas = carta_bebidas()
            while True:
                opcion = int(input("Elegir opcion de bebida: "))
                if 1<= opcion <= 10:
                    bebida = bebidas[opcion]
                    lista_bebidas.append(bebida)
                    break
        elif opcion == 0:
            break
        else:
            print("Opcion no existente")
    mozo_asignado = None
    for mozo in r.Lista_mozos:
        if numero_mesa in mozo["mesa_asignadas"]:
            mozo_asignado = mozo["nombre_mozo"]
            break
    else:
        print("No hay un mozo asignado a esta mesa.")
    guardar_cliente(numero_mesa, mozo_asignado, plato, postre, bebida)
    
