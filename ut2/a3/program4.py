import sys

a = int(sys.argv[1])
mult = 1

if a <= 0:
    print("Error: El número no es positivo")

else:
    for i in range(1, a + 1):
        mult *= i
        print (i, "! =", mult)
