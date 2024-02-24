#Programa para calcular descuento
import os
os.system("cls || clear")
#funcion que calcule el descuento.
def descuento_aplicar(valor):
    if valor > 500:
        descuento = valor * 0.1
        valordescuento = valor - descuento
        return valordescuento
    else:
        return valor

try:
    valor=float(input("Cuanto costo tu producto?: "))
    precio_final = descuento_aplicar(valor)
    print("El precio final del articulo con descuento es: {:.2f}".format(precio_final))
except ValueError:
    print("Ingrese un valor valido")