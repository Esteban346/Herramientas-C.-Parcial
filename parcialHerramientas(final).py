#Esteban Llanos
def descuento(rol, valor, cantidad): #Esta función se encarga de saar el valor a pagar con su respectivo descuento.
    if rol == "estudiante" or rol == "Estudiante":
        valor = (valor - (valor*0.5))*cantidad          #Esta parte del código saca el decuento si es estudiante y el valor total a pagar.
    elif rol == "profesor" or rol == "profesora" or rol == "Profesor" or rol == "Profesora":
        valor = (valor - (valor*0.2))*cantidad    #Esta parte del código saca el decuento si es profesor y el valor total a pagar.
    return valor

def leerImprimir(): #Esta función lee los datos que digitó el usuario y llama a la función decuentos para realizar la impresión de la salida.
    cedula = int(input("Digite su cédula "))
    rol = input("¿Eres un estudiante o un profesor? ")
    valor = eval(input("Digite el valor del producto ")) #Esta parte del código se encarga de pedir el valor de las variables.
    codigo = input("Digite el código del producto ")
    cantidad = int(input("Digite la cantidad de unidades "))
    descuento(rol,valor, cantidad) #Esta parte del código hace un llamado a la función descuento.
    print("El " + rol + " con cédula " + str(cedula) + "," + " debe pagar " + "$" + str(descuento(rol,valor, cantidad)) + " por el producto " + codigo) #Esta parte del código se encarga de imprimir la salida.

leerImprimir()
    
                 
    
                 
    
