#Ejercicio para gestionar una lista de contactos.
import os
os.system("cls || clear")
#Crear clase contacto.
class Contacto:
    def __init__(self, nombre, numero_telefono):
        self.nombre = nombre
        self.numero_telefono = numero_telefono
    def contactar(self):
        print(f"Este contacto es {self.nombre} y su numero de telefono es: {self.numero_telefono}")
#Seleccionar el contacto que desee
contacto1 = Contacto("Ricardo", 58205342)
contacto2 = Contacto("Jose", 25105865)
contacto3 = Contacto("Erving", 57102563)
contacto1.contactar()
