#Ejercicio para calcular si un estudiante opta a beca.
import os
os.system("cls || clear")
def optar_beca(nota):
    if nota > 95:
        return True
    else:
        return False
try:
    nota = float(input("Digite su nota: "))
    if optar_beca(nota):
        print("Conseguiste una beca.")
    else:
        print("No cumples los requisitos para optar a una beca")
except ValueError:
    print("Digita una nota valida.")
