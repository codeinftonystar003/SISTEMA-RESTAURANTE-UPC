# TODO Alexis Huaman-----------------------------------------------------------------------------------------
#---------------------------(Registro de pedidos)
from tabulate import tabulate
from datetime import datetime
import Registros as r
#lista general
lista_clientes = []

#Listas dentro de los clientes
lista_platos = []
lista_postres = []
lista_bebidas = []
lista_hora_pedido = []
lista_hora_maxima = []
lista_hora_entrega = []
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



def guardar_cliente(numero_mesa, mozo_asignado, lista_platos, lista_postres, lista_bebidas, lista_hora_pedido, lista_hora_maxima, lista_hora_entrega): 
    cliente = {
        "N_Mesa": numero_mesa,
        "N_Mozo" : mozo_asignado,
        "plato" : lista_platos.copy(),
        "postre" : lista_postres.copy(),
        "bebida" : lista_bebidas.copy(),
        "hora_pedido" : lista_hora_pedido.copy(),
        "hora_maxima" : lista_hora_maxima.copy(),
        "hora_entrega" : lista_hora_entrega.copy()
    }
    lista_clientes.append(cliente)
def mostrar_cliente():
    if not lista_clientes:
        print("La lista esta vacia")
    else:
        print("El mozo asignado es: ", lista_clientes[0]["N_Mozo"])
        print(tabulate(lista_clientes,headers="keys",tablefmt="grid"))
        
def registrar_pedido():
    
    while True:
        try:
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
        except ValueError:
            print("Valor incorrecto")
    
    while True:
        print("--" * 30)
        print("<< BIENVENIDO AL MENU >>".center(60))
        print("Seleccionar que desea: ")
        print("1. Platos")
        print("2. Postres")
        print("3. Bebidas")
        print("4. Registrar hora de pedido (Necesario)")
        print("5. Registrar hora de entrega")
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
                
        elif opcion == 4:
            fecha_pedido = datetime.now()
            hora_pedido = fecha_pedido.hour
            minutos_pedido = fecha_pedido.minute
            print("--" * 30)
            print("--" * 30)
            print("<< HORA DE PEDIDO >>".center(60))
            print(f"Hora de pedido:  {hora_pedido} horas con {minutos_pedido} minutos.")
            if minutos_pedido + 30 >= 60:
                minutos_maximos = (minutos_pedido + 30) - 60
                hora_maxima = hora_pedido + 1      
                if hora_maxima > 24:
                    hora_maxima = (hora_pedido + 1) - 24
            else:
                
                hora_maxima = hora_pedido
                minutos_maximos = minutos_pedido + 30
            print("<< HORA DE MAXIMA DE ENTREGA >>".center(60))
            print(f"Hora maxima de entrega: {hora_maxima} horas con {minutos_maximos} minutos.")
            print("--" * 30)
            print("--" * 30)
            lista_hora_pedido.append((hora_pedido, minutos_pedido))
            lista_hora_maxima.append((hora_maxima, minutos_maximos))
            break
        elif opcion == 5:
            try:
                print("-"* 30)
                print("Ingresar la hora de entrega de su pedido (en formato 24h): ")
                hora_entrega = int(input("Ingresar hora: "))
                minuto_entrega = int(input("Ingresar minuto: "))
                if hora_entrega >= 0 and hora_entrega <= 24 and minuto_entrega >= 0 and minuto_entrega < 60:
                    for cliente in lista_clientes:
                        if cliente["N_Mesa"] == numero_mesa:
                            if cliente["hora_pedido"]:
                                hora_pedido, minuto_pedido = cliente["hora_pedido"][-1]
                                tiempo_pedido = hora_pedido * 60 + minuto_pedido
                                tiempo_entrega = hora_entrega * 60 + minuto_entrega
                                if tiempo_entrega > tiempo_pedido and tiempo_entrega <= 1440:
                                    print("-" * 30)
                                    print("<< HORA DE ENTREGA REGISTRADO CORRECTAMENTE >>".center(80))
                                    print("-" * 30)
                                    cliente["hora_entrega"].append((hora_entrega, minuto_entrega))
                                else:
                                    print("-" * 30)
                                    print("La hora de entrega debe ser mayor a la hora del pedido")
                                    print("-" * 30)
                            else:
                                print("-" * 30)
                                print("No hay una hora de pedido registrada")
                                print("-" * 30)
                            break
                    else:
                        print("-" * 30)
                        print("No hay un cliente registrado para esta mes")
                        print("-" * 30)
                else:
                    print("-" * 30)
                    print("Error con la hora introducida")
                    print("-" * 30)
            except ValueError:
                print("-" * 30)
                print("Valor incorrecto")
                print("-" * 30)
        elif opcion == 0:
            print("-" * 30)
            print("Regresando...")
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
        
    if lista_platos or lista_postres or lista_bebidas or lista_hora_pedido or lista_hora_maxima or lista_hora_entrega:
        guardar_cliente(numero_mesa, mozo_asignado, lista_platos, lista_postres, lista_bebidas, lista_hora_pedido, lista_hora_maxima, lista_hora_entrega)
        
    lista_platos.clear()
    lista_postres.clear()
    lista_bebidas.clear()
    lista_hora_pedido.clear()
    lista_hora_maxima.clear()
    lista_hora_entrega.clear()
    
    
# TODO Alexis Huaman-----------------------------------------------------------------------------------------
#---------------------------(ELIMINAR PEDIDOS)
def eliminar_pedido(): 
    while True:
        print("--" * 30)
        print("<< ELIMINAR PEDIDOS >>".center(60))
        print("--" * 30)
        existe_mesa = False
        existe_cliente = False
        mesa = int(input("Ingrese el numero de mesa del cliente (si no desea precione 0): "))
        if mesa == 0:
            break
        if 1 <= mesa <= 100: 
            existe_mesa = True
            for cliente in lista_clientes:
                if mesa == cliente['N_Mesa']:
                    existe_cliente = True
                    break 
        if not existe_mesa:
            print("Error, el numero de mesa no es correcto")
            continue
        if not existe_cliente:
            print("Error, no hay un cliente registrado")
            continue
        print("-"* 30)
        print("Que es lo que desea eliminar: ")
        print("1. Platos")
        print("2. Postres")
        print("3. Bebidas")
        print("[0. Regresar]")
        elim = int(input("Ingrese la opcion: "))
        if elim == 1:
            if cliente["plato"] != []:
                print("Platos:")
                for i, pedido in enumerate(cliente["plato"], start=1):
                    print(f"{i}. {pedido[0]} con precio: {pedido[1]}")
                while True:
                    eliminar = int(input("Ingrese el numero del plato a eliminar (Salir = 0): "))
                    if eliminar == 0:
                        print("Regresando...")
                        break
                    if 1 <= eliminar <= len(cliente["plato"]):
                        cliente["plato"].pop(eliminar-1)
                        print("Plato eliminado correctamente".center(80))
                        print("-" * 80)
                    else:
                        print("Error, el numero de plato no es correcto")
            else:
                print("No hay platos registrados para eliminar")
        elif elim == 2:
            if cliente["postre"] != []:
                print("Postres:")
                for i, pedido in enumerate(cliente["postre"], start=1):
                    print(f"{i}. {pedido[0]} con precio: {pedido[1]}")
                while True:
                    eliminar = int(input("Ingrese el numero del postre a eliminar (Salir = 0): "))
                    if eliminar == 0:
                        print("Regresando...")
                        break
                    if 1 <= eliminar <= len(cliente["postre"]):
                        cliente["postre"].pop(eliminar-1)
                        print("Postre eliminado correctamente".center(80))
                        print("-" * 80)
                    else:
                        print("Error, el numero de postre no es correcto")
            else:
                print("No hay postres registrados para eliminar")
        elif elim == 3:
            if cliente["bebida"] != []:
                print("Bebidas:")
                for i, pedido in enumerate(cliente["bebida"], start=1):
                    print(f"{i}. {pedido[0]} con precio: {pedido[1]}")
                while True:
                    eliminar = int(input("Ingrese el numero de la bebida a eliminar (Salir = 0): "))
                    print("Si no desea eliminar presione 0")
                    if eliminar == 0:
                        print("Regresando...")
                        break
                    if 1 <= eliminar <= len(cliente["bebida"]):
                        cliente["bebida"].pop(eliminar-1)
                        print("Bebida eliminada correctamente".center(80))
                        print("-" * 80)
                    else:
                        print("Error, el numero de bebida no es correcto")
            else:
                print("No hay bebidas registradas para eliminar")
        elif elim == 0:
            break
        else:
            print("Opcion incorrecta")


        
        
        
        
