from tabulate import tabulate
from datetime import datetime
# lista de mesas y mozos
Lista_mesas= []
Lista_mozos= []
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
            
        if  not existe_mesa and 1<= numero_mesa <= 100:
            break
        else:
            print("Error, el numero de mesa no esta en rango o ya existe")
    
    while True:
        zona_mesa = input("Ingrese la zona de disponibilidad de la mesa (sala/terraza): ").lower()
        if zona_mesa in ["sala","terraza"]:
            break
        else:
            print("Error, la zona no es correcta")
            
    while True:
        try:
            capacidad_mesa = int(input("Ingrese la capacidad de la mesa (1 - 10): "))
            if 1<= capacidad_mesa <= 10:
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
        if len(id_mozo) == 4 and id_mozo.isdigit():
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
    while True:
        id_mozo = input("Ingrese el id del mozo a asignar (4 digitos): ")
        if len(id_mozo) == 4 and id_mozo.isdigit():
            break
        else:
            print("Error, el id del mozo no es correcto")
            
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
        print("Error, el id del mozo no esta registrado")
        return
    
    if len(mozo_seleccionado["mesa_asignadas"]) >= 4:
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
                        
                           # Cambiar estado del mozo a "inactivo" si tiene 4 mesas asignadas
                        if len(mozo_seleccionado["mesa_asignadas"]) == 4:
                            mozo_seleccionado["estado_mozo"] = "inactivo"
                            print("-" * 80)
                            print(f"El mozo {mozo_seleccionado['nombre_mozo']} ahora está inactivo.".center(80))
                            print("-" * 80)
                            
                    elif confirmar_pedido == "no":
                        print("Reserva cancelada")
                    else:
                        print("Error, la opción no es correcta")
                else:
                    print("Error, la mesa no esta disponible")
            else:
                print("Error, la mesa ya está asignada")
    else:
        print("La mesa no esta registrada")
   

def Cambiar_mozo():
    Mostrar_mozos()
    if not Lista_mozos:
        print("No hay mozos registrados")
        return

    while True:
        id_mozo = input("Ingrese el id del mozo a cambiar (4 dígitos): ")
        id_nuevo_mozo = input("Ingrese el id del nuevo mozo (4 dígitos): ")
        if len(id_mozo) == 4 and id_mozo.isdigit() and len(id_nuevo_mozo) == 4 and id_nuevo_mozo.isdigit():
            break
        else:
            print("Error, ambos IDs deben ser numéricos de 4 dígitos")

    while True:
        try:
            numero_mesa = int(input("Ingrese el número de mesa a cambiar mozo (1 - 100): "))
            if 1 <= numero_mesa <= 100:
                break
            else:
                print("Error, el número de mesa debe estar entre 1 y 100")
        except ValueError:
            print("Error en el número de mesa")
            return

    # Buscar el nuevo mozo
    nuevo_mozo = None
    for mozo in Lista_mozos:
        if mozo["id_mozo"] == id_nuevo_mozo:
            if mozo["estado_mozo"] == "activo":
                nuevo_mozo = mozo
                break
            else:
                print("Error, el nuevo mozo no está disponible")
                return
    if nuevo_mozo is None:
        print("Error, el ID del nuevo mozo no está registrado")
        return

    # Buscar el mozo actual y quitar la mesa
    mozo_actual = None
    for mozo in Lista_mozos:
        if mozo["id_mozo"] == id_mozo:
            mozo_actual = mozo
            if numero_mesa in mozo["mesa_asignadas"]:
                mozo["mesa_asignadas"].remove(numero_mesa)
                break
            else:
                print("Error, la mesa no está asignada al mozo actual")
                return
    if mozo_actual is None:
        print("Error, el mozo actual no se encuentra registrado")
        return

    # Asignar la mesa al nuevo mozo
    if len(nuevo_mozo["mesa_asignadas"]) < 4:
        nuevo_mozo["mesa_asignadas"].append(numero_mesa)
        print("-" * 80)
        print("Cambio de mozo realizado correctamente".center(80))
        print("-" * 80)
    else:
        print("Error, el nuevo mozo no puede atender más mesas")

        

