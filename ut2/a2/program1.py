import sys
import math
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == 0:
    print("x=", -c / b)

elif ((b ** 2) - (4 * a * c)) < 0:
    print("La ecuación no tiene solución real")
else:
    x1 = (-b + math.sqrt((b ** 2) - (4 * a * c)) / 2 * a)
    x2 = (-b - math.sqrt((b ** 2) - (4 * a * c)) / 2 * a)
    print("x1=", x1, "x2=", x2)
