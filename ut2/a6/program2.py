def add_contacts(phone_book, name, phone):
	phone_book[name] = phone

def show_contacts(phone_book):
	if phone_book == {}:
		print("\nNo hay ningún contacto.\n")
	for name, number in phone_book.items():
		print(f"\n -{name}: {number}")

def remove_contacts(phone_book, name):
	del(phone_book[name])

def menu():
	phone_book = {}
	while True:
		print("""
1.- Mostrar contactos en el libro de teléfonos.
2.- Añadir un contacto.
3.- Eliminar un contacto.
4.- Finalizar.
			""")
		option = input("Escoja la opción deseada: ")

		if option == "1":
			show_contacts(phone_book)
		elif option == "2":
			name = input("Escriba el nombre del contacto: ")
			if name in phone_book:
				print("Se ha producido un error: El contacto introducido ya existe.")
			else:
				number = input("Introduzca el número de teléfono: ")
				add_contacts(phone_book, name, number)
		elif option == "3":
			name = input("Escriba el contacto a eliminar: ")
			if name in phone_book:
				remove_contacts(phone_book,name)
			else:
				print("\nError:\n-> El nombre introducido no es un contacto.\n-> Puede consultar los contactos eligiendo la opción 1.")
		elif option == "4":
			print("\nSaliendo...")
			break
		else:
			print("Error: Opción no válida.")

menu()
