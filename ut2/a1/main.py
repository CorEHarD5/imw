# ¿Me da cambio por favor?

import sys
valor_euros = int(sys.argv[1])

print ("Máquina de cambio by Sergio.")
print ("Tenemos solo billetes de: 50€, 20€, 10€ y 5€")
print ("Además tenemos monedas de 1€ y 2€.")


dinero_50 = valor_euros % 50
dinero_50xd = valor_euros // 50

print ("Para", valor_euros, "€, es necesario:")

if dinero_50xd > 0:
    print (dinero_50xd, "de 50€.")

dinero_20 = dinero_50 % 20
dinero_20xd = dinero_50 // 20

if dinero_20xd > 0:
    print (dinero_20xd, "de 20€.")

 
dinero_10 = dinero_20 % 10
dinero_10xd = dinero_20 // 10

if dinero_10xd > 0:
    print (dinero_10xd, "de 10€.")

   
dinero_05 = dinero_10 % 5
dinero_05xd = dinero_10 // 5

if dinero_05xd > 0:
    print (dinero_05xd, "de 5€.")


dinero_02 = dinero_05 % 2
dinero_02xd = dinero_05 // 2
    
if dinero_02xd > 0:
    print (dinero_02xd, "de 2€.")

   
dinero_01 = dinero_02 % 1
dinero_01xd = dinero_02 // 1

if dinero_01xd > 0:
    print (dinero_01xd, "de 1€.")
