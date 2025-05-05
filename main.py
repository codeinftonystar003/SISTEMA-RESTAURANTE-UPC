import Registros as r 
import pedidos as p
import menu_principal as m
def main():
    while True:
        m.menu()
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
            while True:
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if 1 <= subopcion <= 2:
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
            if subopcion == 1:   
                r.Registrar_mesas() # 1. Registrar mesas
            elif subopcion == 2:
                r.Registrar_mozos() # 2. Registrar mozos
            else:
                print("Opcion no valida")
                
        elif opcion == 2: # Asignar mozo a mesa
            print("1. Asignar mozo a mesa")
            print("2. Cambiar mozo de la mesa actual")
            while True:
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if 1 <= subopcion <= 2:
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
            if subopcion == 1: # Asignar mozo a mesa
                r.Asignar_mozo()
            elif subopcion == 2: # Cambiar mozo de la mesa actual
                r.Cambiar_mozo()
            else:
                print("Opcion no valida")
                
                
        elif opcion == 3: # Reaizar el pedido 
            print("1. Añadir items")
            print("2. Eliminar items")
            print("3. Registrar hora de inicio y final")
            print("[0. Regresar]")
            while True:
                try:
                    opcion = int(input ("Ingresar opcion: "))
                    if  opcion == 1: # Añadir items de pedido para las mesas
                        p.registrar_pedido()
                    elif opcion == 2:
                        print("Funcion eliminar pedido")
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
            while True:
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if 1 <= subopcion <= 3:
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
            if subopcion == 1:
                r.Mostrar_mesas() # Mostrar mesas registradas
            elif subopcion == 2:
                r.Mostrar_mozos() # Mostrar mozos registrados
            elif subopcion == 3:
                p.mostrar_cliente() # Mostrar los pedidos de los clientes
            else:
                print("Opcion no valida")
        elif opcion == 7:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
main()

