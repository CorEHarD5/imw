# ¿Me da cambio por favor?

print ("Máquina de cambio by Sergio.")
print ("Tenemos solo billetes de: 50€, 20€, 10€ y 5€")
print ("Además tenemos monedas de 1€ y 2€.")
valor_euros = int(input("Inserte una cantidad la cual va a cambiar:"))
print(type(valor))

dinero_50 = valor % 50 # la variable dinero_valor mete el resto de la división
dinero_50xd = valor // 50 # la variable dinero_valorxd es el número de billetes que devuelve

print ("Para", valor, "€, es necesario:")

if dinero_50xd > 0:
    print (dinero_50xd, "de 50€.")
else:
    print ("")
  
dinero_20 = dinero_50 % 20
dinero_20xd = dinero_50 // 20

if dinero_20xd > 0:
    print (dinero_20xd, "de 20€.")
else:
    print ("")
 
dinero_10 = dinero_20 % 10
dinero_10xd = dinero_20 // 10

if dinero_10xd > 0:
    print (dinero_10xd, "de 10€.")
else:
    print ("")
   
dinero_05 = dinero_10 % 5
dinero_05xd = dinero_10 // 5

if dinero_05xd > 0:
    print (dinero_05xd, "de 5€.")
else:
    print ("")

dinero_02 = dinero_10 % 2
dinero_02xd = dinero_10 // 2
    
if dinero_02xd > 0:
    print (dinero_02xd, "de 2€.")
else:
    print ("")
   
dinero_01 = dinero_02 % 1
dinero_01xd = dinero_02 // 1

if dinero_01xd > 0:
    print (dinero_01xd, "de 1€.")
else:
    print ("")