from tabulate import tabulate
import pedidos as p
import Registros as r


def reporte_mozo_mas_pedidos():
    if not p.lista_clientes or not r.Lista_mozos:
        print("No hay mozos registrados o no hay pedidos registrados")
        return

    mozos_items = {}
    for mozo in r.Lista_mozos:
        mozos_items[mozo['nombre_mozo']] = 0
    
    for cliente in p.lista_clientes:
        mozo = cliente['N_Mozo']
        if mozo in mozos_items:
            mozos_items[mozo] += len(cliente['plato'])
            mozos_items[mozo] += len(cliente['postre'])
            mozos_items[mozo] += len(cliente['bebida'])
    
    if not mozos_items or sum(mozos_items.values()) == 0:
        print("No hay pedidos registrados")
        return

    mozo_top = ("", 0)
    for nombre, cantidad in mozos_items.items():
        if cantidad > mozo_top[1]:
            mozo_top = (nombre, cantidad)
    
    items_list = []
    for nombre, cantidad in mozos_items.items():
        items_list.append((cantidad, nombre))
    
    tabla_datos = []
    for posicion, (cantidad, nombre) in enumerate(items_list, start=1):
        tabla_datos.append([posicion, nombre, cantidad])
    
    print("\n" + "="*60)
    print("MOZO CON MÁS PEDIDOS ATENDIDOS".center(60))
    print("="*60)
    print(tabulate(tabla_datos, headers=['Mozo', 'Total Pedidos'],tablefmt='grid'))
    print("="*60)
    print(f"¡El mozo más eficiente es {mozo_top[0]} con {mozo_top[1]} pedidos atendidos!".center(60))
    print("="*60 + "\n")
    
def reporte_tiempo_promedio_espera():
    if not p.lista_clientes:
        print("No hay pedidos registrados para calcular tiempos de espera")
        return
    
    total_pedidos = 0
    tiempo_total = 0  # en minutos
    pedidos_tardios = 0
    
    print("\n" + "="*60)
    print("TIEMPO DE ESPERA POR PEDIDO".center(60))
    print("="*60)
    
    tabla_datos = []
    
    for cliente in p.lista_clientes:
        if not cliente['hora_pedido'] or not cliente['hora_entrega']:
            continue
            
        # Obtener tiempos
        hora_pedido, minuto_pedido = cliente['hora_pedido'][0]
        hora_entrega, minuto_entrega = cliente['hora_entrega'][0]
        hora_maxima, minuto_maximo = cliente['hora_maxima'][0]
        
        # Calcular tiempo en minutos
        tiempo_pedido = hora_pedido * 60 + minuto_pedido
        tiempo_entrega = hora_entrega * 60 + minuto_entrega
        tiempo_maximo = hora_maxima * 60 + minuto_maximo
        
        # Calcular tiempo de espera
        tiempo_espera = tiempo_entrega - tiempo_pedido
        
        # Verificar si fue tardío
        tardio = "Sí" if tiempo_entrega > tiempo_maximo else "No"
        if tardio == "Sí":
            pedidos_tardios += 1
            
        # Acumular para promedio
        total_pedidos += 1
        tiempo_total += tiempo_espera
        
        # Agregar a tabla
        tabla_datos.append([
            cliente['N_Mesa'],
            f"{hora_pedido:02d}:{minuto_pedido:02d}",
            f"{hora_entrega:02d}:{minuto_entrega:02d}",
            f"{tiempo_espera} min",
            tardio
        ])
    
    if total_pedidos == 0:
        print("No hay pedidos completos con hora de entrega registrada")
        return
    
    # Calcular promedios
    promedio_espera = tiempo_total / total_pedidos
    porcentaje_tardios = (pedidos_tardios / total_pedidos) * 100
    
    # Mostrar tabla
    print(tabulate(tabla_datos, 
                  headers=['Mesa', 'Hora Pedido', 'Hora Entrega', 'Tiempo Espera', 'Tardío'],
                  tablefmt='grid'))
    
    # Mostrar estadísticas
    print("\n" + "ESTADÍSTICAS GENERALES".center(60))
    print(f"Tiempo promedio de espera: {promedio_espera:.1f} minutos")
    print(f"Pedidos entregados a tiempo: {100 - porcentaje_tardios:.1f}%")
    print(f"Pedidos entregados tarde: {porcentaje_tardios:.1f}%")
    print("="*60 + "\n")