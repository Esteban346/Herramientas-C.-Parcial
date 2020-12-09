def descuento(rol, valor):
    if rol == "estudiante" or rol == "Estudiante":
        valor = valor - (valor*0.5)
    elif rol == "profesor" or rol == "profesora" or rol == "Profesor" or rol == "Profesora":
        valor = valor - (valor*0.2)
    return valor

def leerImprimir():
    cedula = int(input("Digite su cédula "))
    rol = input("¿Eres un estudiante o un profesor? ")
    valor = eval(input("Digite el valor del producto "))
    codigo = input("Digite el código del producto ")
    descuento(rol,valor)
    print("El " + rol + " con cédula " + str(cedula) + "," + " debe pagar " + "$" + str(descuento(rol,valor)) + " por el producto " + codigo)

leerImprimir()
    
                 
    
                 
    
