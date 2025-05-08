import Registros as r 
import pedidos as p
import menu_principal as m
import Reportes as rep
def main():
    m.caratula() 
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
            while True:
                print("----------------------------------------")
                print("1. Registrar mesas")
                print("2. Registrar mozos")
                print("3. Salir")
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if 1 <= subopcion <= 3:
                        if subopcion == 1:   
                            r.Registrar_mesas() # 1. Registrar mesas
                        elif subopcion == 2:
                            r.Registrar_mozos() # 2. Registrar mozos
                        elif subopcion == 3:
                            break
                        else:
                            print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
                
        elif opcion == 2:  # Asignar mozo a mesa
            while True:
                print("----------------------------------------")
                print("1. Asignar mozo a mesa")
                print("2. Cambiar mozo de la mesa actual")
                print("3. Salir")
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if subopcion == 1:
                        r.Asignar_mozo()
                    elif subopcion == 2:
                        r.Cambiar_mozo()
                    elif subopcion == 3:
                        print("Saliendo del menú de mozos.")
                        break  # Salimos del bucle porque eligió salir
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")

        elif opcion == 3: # Reaizar el pedido 
            while True:
                print("----------------------------------------")
                print("1. Añadir pedido y ver datos del pedido")
                print("2. Eliminar items")
                print("[0. Regresar]")
                try:
                    opcion = int(input ("Ingresar opcion: "))
                    if  opcion == 1:
                        p.registrar_pedido()
                    elif opcion == 2:
                        p.eliminar_pedido()
                    elif opcion == 0:
                        break
                except ValueError:
                    print("Valor incorrecto")
                    
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6: # Aqui se muestran los reportes de los mozos , mesas y los pedidos de los clientes
            while True:
                print("1. Mostrar mesas")
                print("2. Mostrar mozos")
                print("3. Mostrar pedidos clientes")
                print("4. Mostrar mozo con mas pedidos")
                print("5. Mostrar promedio tiempo espera")
                print("6. salir")
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if subopcion == 1:
                        r.Mostrar_mesas() # Mostrar mesas registradas
                    elif subopcion == 2:
                        r.Mostrar_mozos() # Mostrar mozos registrados
                    elif subopcion == 3:
                        p.mostrar_cliente() # Mostrar los pedidos de los clientes
                    elif subopcion == 4:
                        rep.reporte_mozo_mas_pedidos()
                    elif subopcion == 5:
                        rep.reporte_tiempo_promedio_espera()
                    elif subopcion == 6:
                        break
                    else:
                        print("La opcion es incorrecta")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
        
                
        elif opcion == 7:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
main()

