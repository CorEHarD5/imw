import sys

k = int(sys.argv[1])
frase = sys.argv[2]

if k < 0:
    sys.exit("El número introducido no es positivo")

fraselista = frase.split()
valor = 0

for palabra in fraselista:
    if len(palabra) == k:
        valor += 1
print(f"Hay {valor} palabra(s) de tamaño {k}")