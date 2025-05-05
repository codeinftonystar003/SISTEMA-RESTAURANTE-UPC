from tabulate import tabulate
from datetime import datetime
Lista_mesas= []
Lista_mozos= []
lista_mesas_asignadas = []
#---------------------------(Registro de pedidos)
lista_clientes = []
lista_platos = []
lista_postres = []
lista_bebidas = []

def menu():
    print("--" * 30)
    print("<< MENU PRINCIPAL >>".center(60))
    print("--" * 30)
    print("[1] Registros        🍽️") 
    print("[2] Tomar mozo       👨")
    print("[3] Tomar pedido     🍔")
    print("[4] Calcular pago    💵")
    print("[5] Finalizar pedido 🍽️")
    print("[6] Ver reportes     📈")
    print("[7] Salir  ")
    print("--" * 30)
    print("<< ...SISTEMA RESTAURANTE -- BIENVENIDOS ...>>".center(60))
    print("--" * 30)
    

# TODO: Antony Yomar Peña Roña -----------------------------------------------------

def Guardar_mesas(numero_mesa, zona_mesa, capacidad_mesa, estado_mesa):
    mesas = { "numero_mesa": numero_mesa,
                "zona_mesa": zona_mesa,
                "capacidad_mesa": capacidad_mesa,
                "estado_mesa": estado_mesa}
    Lista_mesas.append(mesas)

def Mostrar_mesas():
    if not Lista_mesas:
        print("No hay mesas registradas")
    else:
        print("Mesas registradas:")
        print(tabulate(Lista_mesas, headers="keys", tablefmt="grid"))
        

def Guardar_mozos( id_mozo, nombre_mozo, telefono_mozo, estado_mozo, capacidad_mozo):
    mozos = { "id_mozo": id_mozo,
                "nombre_mozo": nombre_mozo,
                "telefono_mozo": telefono_mozo,
                "estado_mozo": estado_mozo,
                "capacidad_mozo": capacidad_mozo,
                "mesa_asignadas": [] 
                }
    Lista_mozos.append(mozos)

def Mostrar_mozos():
    if not Lista_mozos:
        print("No hay mozos registrados")
    else:
        print("Mozos registrados:")
        print(tabulate(Lista_mozos, headers="keys", tablefmt="grid"))
        
def Registrar_mesas():
    print("Registro de mesas".center(80, "-"))
    print("-" * 80)
    while True:
        existe_mesa = False
        numero_mesa = int(input("Ingrese el numero de  mesa a registrar (1 - 100): "))
        if 1<= numero_mesa <= 100:
            for  id  in Lista_mesas:
                if id["numero_mesa"] == numero_mesa:
                    existe_mesa = True
                    break
        if not existe_mesa and 1<= numero_mesa <= 100 :
            break
        else:
            print("Error, el numero de mesa no es correcto")
    
    while True:
        zona_mesa = input("Ingrese la zona de disponibilidad de la mesa (sala/terraza): ").lower()
        if zona_mesa in ["sala","terraza"]:
            break
        else:
            print("Error, la zona no es correcta")
            
    while True:
        try:
            capacidad_mesa = int(input("Ingrese la capacidad de la mesa: "))
            if 1<= capacidad_mesa <= 20:
                break
            else:
                print("Error, la capacidad de la mesa no es correcta")
        except ValueError:
            print("Error en los datos de ingreso")
    
    while True:
        estado_mesa = input("Ingrese el estado de la mesa (libre/ocupada/reservada): ").lower()
        if estado_mesa in ["libre","ocupada","reservada"]:
            break
        else:
            print("Error, el estado de la mesa no es correcto")
    print("-" * 80)
    print("Mesa registrada correctamente".center(80))
    print("-" * 80)
    Guardar_mesas(numero_mesa, zona_mesa, capacidad_mesa, estado_mesa)

def Registrar_mozos():
    print("-" * 80)
    print("Registro de mozos".center(80, "-"))
    print("-" * 80)
    
    while True:
        existe_mozo = False
        id_mozo = input("Ingrese el id del mozo (4 digitos): ")
        if len(id_mozo) == 4:
            for id in Lista_mozos:
                if id["id_mozo"] == id_mozo:
                    existe_mozo = True
                    break
            if not existe_mozo:
                break
            else:
                print("Error, el id del mozo ya existe")
        else:
            print("Error en los datos de ingreso")
    nombre_mozo = input("Ingrese el nombre y apellido del mozo: ")
    
    while True:
        try:
            telefono_mozo = input("Ingrese el telefono del mozo (9 digitos): ")
            if len(str(telefono_mozo)) == 9:
                break
            else:
                print("Error, el telefono del mozo no es correcto")
        except ValueError:
            print("Error en los datos de ingreso")
    
    while True:
        estado_mozo = input("Ingrese el estado del mozo (activo/inactivo): ").lower()
        if estado_mozo in ["activo","inactivo"]:
            break
        else:
            print("Error, el estado del mozo no es correcto")
            
    capacidad_mozo = 4
    Guardar_mozos(id_mozo, nombre_mozo, telefono_mozo, estado_mozo, capacidad_mozo)
    print("-" * 80)
    print("Mozo registrado correctamente".center(80))
    print("-" * 80)
    
    
def Asignar_mozo():
    Mostrar_mozos()
    if not Lista_mozos:
        print("No hay mozos registrados")
        return
    id_mozo = input("Ingrese el id del mozo a asignar (4 digitos): ")
    mozo_seleccionado = None
    for id in Lista_mozos:
        if id["id_mozo"] == id_mozo :
            if id["estado_mozo"] == "activo":
                mozo_seleccionado = id
                break
            else:
                print("Error, el mozo no esta disponible")
                return
    else:
        print("Error, el id del mozo no es correcto")
        return
    
    if len(mozo_seleccionado["mesa_asignadas"]) >= mozo_seleccionado["capacidad_mozo"]:
        print("-" * 80)
        print("Error, el mozo no puede atender más mesas".center(80))
        print("-" * 80)
        return
    
    while True:
        try:
            numero_mesa = int(input("Ingrese el numero de mesa a reservar (1 - 100): "))
            if 1<= numero_mesa <= 100:
                break
            else:
                print("Error, el numero de mesa no es correcto")
        except ValueError:
            print("Error en los datos de ingreso")
            
    for id in Lista_mesas:
        if id["numero_mesa"] == numero_mesa:
            mesas_asignadas = id["numero_mesa"]
            if mesas_asignadas not in mozo_seleccionado["mesa_asignadas"]:
                if id["estado_mesa"] == "libre":
                    confirmar_pedido = input("¿Desea confirmar la reserva? (si/no): ").lower()
                    if confirmar_pedido == "si":
                        id["estado_mesa"] = "reservada"
                        print("-" * 80)
                        print("Mesa reservada correctamente".center(80))
                        print("-" * 80)
                        mozo_seleccionado["mesa_asignadas"].append(numero_mesa)
                    else:
                        print("Reserva cancelada")
                else:
                    print("Error, la mesa no esta disponible")
            else:
                print("Error, la mesa ya está asignada")
    
   

def Cambiar_mozo():
    Mostrar_mozos()
    if not Lista_mozos:
        print("No hay mozos registrados")
        return

    id_mozo = input("Ingrese el id del mozo a cambiar (4 dígitos): ") # vaidar entrada
    id_nuevo_mozo = input("Ingrese el id del nuevo mozo (4 dígitos): ") # validar entrada 

    try:
        numero_mesa = int(input("Ingrese el número de mesa a cambiar mozo (1 - 100): ")) # validar entrada de datos 
    except ValueError:
        print("Error en el número de mesa")
        return

    # Buscar el nuevo mozo
    nuevo_mozo = None
    for mozo in Lista_mozos:
        if str(mozo["id_mozo"]) == id_nuevo_mozo:
            if mozo["estado_mozo"] == "activo":
                nuevo_mozo = mozo
                break
            else:
                print("Error, el nuevo mozo no está disponible")
                return
    else:
        print("Error, el id del nuevo mozo no es correcto")
        return

    # Buscar el mozo actual y quitar la mesa
    mozo_actual = None
    for mozo in Lista_mozos:
        if str(mozo["id_mozo"]) == id_mozo:
            mozo_actual = mozo
            if numero_mesa in mozo["mesa_asignadas"]:
                mozo["mesa_asignadas"].remove(numero_mesa)
                break
            else:
                print("Error, la mesa no está asignada al mozo actual")
                return
    else:
        print("Error, el id del mozo no es correcto")
        return

    # Asignar la mesa al nuevo mozo
    if len(nuevo_mozo["mesa_asignadas"]) < nuevo_mozo["capacidad_mozo"]:
        nuevo_mozo["mesa_asignadas"].append(numero_mesa)
        print("-" * 80)
        print("Cambio de mozo realizado correctamente".center(80))
        print("-" * 80)
    else:
        print("Error, el nuevo mozo no puede atender más mesas")
        
        
        
        

# TODO Alexis Huaman-----------------------------------------------------------------------------------------

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
        "plato" : lista_platos.copy(),
        "postre" : lista_postres.copy(),
        "bebida" : lista_bebidas.copy(), 
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
            for  id  in Lista_mesas:
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
        print("[0. Regresar]")
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
    for mozo in Lista_mozos:
        if numero_mesa in mozo["mesa_asignadas"]:
            mozo_asignado = mozo["nombre_mozo"]
            break
    else:
        print("No hay un mozo asignado a esta mesa.")
    guardar_cliente(numero_mesa, mozo_asignado, lista_platos, lista_postres, lista_bebidas)
    lista_platos.clear()
    lista_postres.clear()
    lista_bebidas.clear()

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
                else:
                    print("No existe un pedido registrado para la mesa")
                    existe_cliente = False
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
                    print("Si no desea eliminar presione 0")
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
        
    
def Calcular_hora():
    pass

def Eliminar_items():
    pass

    
# ! -----------------------------------------------------------------------------------------
def main():
    while True:
        menu()
        while True:
            try:
                opcion = int(input("Seleccione una opción: "))
                if 1 <= opcion <= 7:
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        if opcion == 1:
            print("1. Registrar mesas")
            print("2. Registrar mozos")
            print("3. Salir")
            while True:
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if 1 <= subopcion <= 3:
                        if subopcion == 1:   
                            Registrar_mesas() # 1. Registrar mesas
                        elif subopcion == 2:
                            Registrar_mozos() # 2. Registrar mozos
                        elif subopcion == 3:
                            break
                        else:
                            print("Opcion no valida")
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
          
                
        elif opcion == 2: # Asignar mozo a mesa
            print("1. Asignar mozo a mesa")
            print("2. Cambiar mozo de la mesa actual")
            print("3. Salir ")
            while True:
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if 1 <= subopcion <= 3:
                        if subopcion == 1: # Asignar mozo a mesa
                            Asignar_mozo()
                        elif subopcion == 2: # Cambiar mozo de la mesa actual
                            Cambiar_mozo()
                        elif subopcion ==3:
                            break
                        else:
                            print("Opcion no valida")
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
        
                
                
        elif opcion == 3: # Reaizar el pedido 
            while True:
                print("1. Añadir pedidos")
                print("2. Eliminar pedidos")
                print("3. Registrar hora de inicio y final")
                print("[0. Regresar]")
                try:
                    opcion = int(input ("Ingresar opcion: "))
                    if  opcion == 1: # Añadir items de pedido para las mesas
                        registrar_pedido()
                    elif opcion == 2:
                        eliminar_pedido()
                    elif opcion == 3:
                        print("Funcion de horas")
                    elif opcion == 0:
                        break
                except ValueError:
                    print("Valor incorrecto")
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6: # Aqui se muestran los reportes de los mozos , mesas y los pedidos de los clientes
            print("1. Mostrar mesas")
            print("2. Mostrar mozos")
            print("3. Mostrar  pedidos clientes")
            print("4. Salir")
            while True:
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if 1 <= subopcion <= 4:
                        if subopcion == 1:
                            Mostrar_mesas() # Mostrar mesas registradas
                        elif subopcion == 2:
                            Mostrar_mozos() # Mostrar mozos registrados
                        elif subopcion == 3:
                            mostrar_cliente() # Mostrar los pedidos de los clientes
                        elif subopcion == 4:
                            break
                        else:
                            print("Opcion no valida")
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
        elif opcion == 7:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
main()








