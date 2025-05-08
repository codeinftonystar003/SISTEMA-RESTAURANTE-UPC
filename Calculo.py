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
lista_pagos=[]
pagos_finales=[] #para agregar los pagos totales de cada mesa
print("-"*50)
print("Calculo ".center (31,"-")) 
def pago_final():
  while True:
       try:
           existe_mesa= False
           n_mesa=int(input("Digite el numero de mesa a pagar 👉🏼: "))
           if n_mesa>=1 and n_mesa<=100:
               for id in r.Lista_mesas:
                   if id ["n_mesa"]==n_mesa:
                       existe_mesa=True
                       for clientes in p.lista_clientes: 
                          if n_mesa == p.lista_clientes["N_Mesa"]: #encontrar el numero de mesa ingresado en la lista de clientes 
                             pago_plato= p.lista_platos["plato"]
                             pago_postre= p.lista_postres["postre"]
                             pago_bebida= p.lista_bebidas["bebida"]
                             pago_final= pago_plato + pago_postre + pago_bebida
                             
                             print(f"\nEl pago total seria {pago_final} soles.")
                          else:
                             print("El numero de mesa ingresado no esta registrado")
                          pago_postre= p.lista_postres["postre"]
                          pago_bebida= p.lista_bebidas["bebida"]
                          pago_final= pago_plato + pago_postre + pago_bebida
                          mesa_pago_final = {clientes["N_Mesa"]:pago_final}
                          pagos_finales.append(mesa_pago_final)
                    
                   propina= (str("\nSugerimos propina del 10% sobre el pago total, desea aceptar?: "))
                   if propina.lower()=="si":
                     propina_total= pago_final * 0.10
                     pago_final= pago_final + propina_total
                     print ("--"*30)
                     print(f"\n--> El nuevo total de pago seria es {pago_final} soles.")
                     print("¡¡Muchas Gracias!!".center (31,"-"))
                   else:
                       if propina.lower()=="no":
                           print("Esta bien, no se preocupe!\n") 
                           print("El pago final seria= ", pago_final)
                           print("Gracias!!".center (31,"-"))  
           if existe_mesa:
               break
           else: 
                print("❌ Error, numero de mesa incorrecto, capacidad de (1-100) ")
       except ValueError:
           print ("❌ Error, digite un numero")

def descuento_espera(t_inicio, t_final, t_espera,descuento,pago_final, pago_subtotal): #descuento de 10% si la espera fue mas de 30min
    
    t_espera= t_final-t_inicio #hallar el tiempo de demora de la mesa
    print ( "--" *30)
    if t_espera>30: # si el tiempo fue mayor a 30
        print("‼️Debido a que el tiempo de espera fue mas de 30 minutos...")
        print("👉🏼¡Ud. ha recibido un descuento automatico del 10% del pago total!")
        print("--"*30)
        descuento= pago_subtotal * 0.10
        pago_final= pago_subtotal-descuento
        print("\nEl pago por la mesa #{n_mesa} es= ", pago_final) 


