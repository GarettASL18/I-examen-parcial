#leer la edad de una persona y decir si es mayor o menor de edad
import os
os.system("cls || clear")
#Creacion de la funcion
def mayormenor_edad(edad):
    if edad >= 18:
        return "Eres mayor de edad."
    else:
        return "Eres menor de edad."
def main():
    try:
        edad = int(input("Ingresa la edad: "))
        resultado = mayormenor_edad(edad)
        print(resultado)
    except ValueError:
        print("Ingrese un numero entero u valido.")
if __name__ == "__main__":
    main()
