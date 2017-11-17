import sys

a = int(sys.argv[1])

if a <= 0:
    print("Error: El número introducido no es positivo.")
else:
    sum = 0
    for i in range(1, a + 1):
        cuadrado = i ** 2
        sum = cuadrado + sum
    else:
        print(sum)
