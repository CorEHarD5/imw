import sys

num = sys.argv[1:]
long_num = len(num)
suma = 0

for i in range(0, long_num):
	suma += float(num[i])
media = suma / long_num
print(f"La media de los valores es: {media}")
