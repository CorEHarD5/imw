import sys
from math import pi
radius = int(sys.argv[1])
print("Menu de opciones:")
print("(1) Calcular el diámetro de la circunferencia.")
print("(2) Calcular el perímetro de la circunferencia.")
print("(3) Calcular el área del círculo.")
print("(4) Salir.")
option_menu = int(input("Ponga el número de la opción deseada: "))
if option_menu == 1:
    solution = 2 * radius
    print("Diámetro: ", solution)
elif option_menu == 2:
    solution = 2 * pi * radius
    print("Perimetro: ", solution)
elif option_menu == 3:
    solution = pi * (radius ** 2)
    print("Área: ", solution)
elif option_menu == 4:
    print("Saliendo...")
else:
    print("Error")
