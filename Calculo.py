# TODO Lucero  
import pedidos as p
import Registros as r
lista_clientes = []
lista_platos = []
lista_postres = []
lista_bebidas = []
lista_hora_pedido = []
lista_hora_maxima = []
lista_hora_entrega = []
lista_pagos = []
pagos_finales=[]
def pago_final():
  print("-"*50)
  print("Calculo ".center (31))
  while True:
       try:
           existe_mesa= False
           n_mesa=int(input("Digite el numero de mesa a pagar 👉🏼: "))
           if n_mesa>=1 and n_mesa<=100:
               for id in r.Lista_mesas:
                   if id ["numero_mesa"]==n_mesa:
                       existe_mesa=True
                       for clientes in p.lista_clientes: 
                          if n_mesa == clientes["N_Mesa"]: #encontrar el numero de mesa ingresado en la lista de clientes 
                             #----------------------- hallar el precio de cada consumo de la mesa
                             pago_plato = int(clientes["plato"][0][1])
                             pago_postre= int(clientes["postre"][0][1])
                             pago_bebida= int(clientes["bebida"][0][1])
                             pago_final= pago_plato + pago_postre + pago_bebida
                            
                             #----------------------- convertir a minutos la hr de pedido
                             auxiliar1 = clientes["hora_pedido"]
                             auxiliar2 = clientes["hora_pedido"]
                             hora_pedido_H = auxiliar1[0][0]
                             hora_pedido_M = auxiliar2[0][1]
                             convertir_min_pedido = hora_pedido_H*60 + hora_pedido_M
                             print(convertir_min_pedido)
                             #----------------------- convertir a minutos la hr de entrega
                             hora_entrega_H= clientes["hora_entrega"][0][0]
                             hora_entrega_M= clientes["hora_entrega"][0][1]
                             convertir_min_entrega = hora_entrega_H*60 + hora_entrega_M
                             if convertir_min_entrega > convertir_min_pedido+30: # si el tiempo de entrega paso el limite de 30 min de espera
                                 print ( "--" *30)
                                 print("‼️Debido a que el tiempo de espera fue mas de 30 minutos...")
                                 print("👉🏼¡Ud. ha recibido un descuento automatico del 10% del pago total!")
                                 print("--"*30)
                                 descuento= pago_final * 0.10
                                 pago_final=pago_final- descuento
                                 print(f"\nEl pago por la mesa #{n_mesa} es {pago_final}")
                             else:
                                  break
                             print(f"\nEl pago total seria {pago_final} soles.")
                          else:
                            print("El numero de mesa ingresado no esta registrado")
                          mesa_pago_final = {clientes["N_Mesa"]:pago_final}
                          pagos_finales.append(mesa_pago_final)
                    
                   propina= str(input("\nSugerimos propina del 10% sobre el pago total, desea aceptar?: "))
                   if propina.lower()=="si":
                     propina_total= pago_final * 0.10
                     pago_final= pago_final + propina_total
                     print ("--"*30)
                     print(f"\n--> El nuevo total de pago seria es {pago_final} soles.")
                     print("¡¡Muchas Gracias!!".center (31))
                   else:
                       if propina.lower()=="no":
                           print("Esta bien, no se preocupe!\n") 
                           print("El pago final seria= ", pago_final)
                           print("Gracias!!".center (31))  
           if existe_mesa:
               break
           else: 
                print("❌ Error, numero de mesa incorrecto, capacidad de (1-100) ")
       except ValueError:
           print ("❌ Error, digite un numero") 







