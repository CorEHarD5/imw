import sys

a = int(sys.argv[1])

if a <= 0:
    print("Error: El número introducido no es positivo.")
else:
    for i in range(2, a):
        resto = a % i
        if resto == 0:
            print ("El número introducido no es primo")
            break
    else:
        print ("El número introducido es primo")
