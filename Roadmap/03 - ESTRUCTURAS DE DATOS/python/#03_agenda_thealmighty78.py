""" * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 """

# contact_list = []
# new_name = ""

# while new_name != 'quit':
#     opcion = input("Que operación deseas realizar: \n[I]nsertar \n[A]ctualizar \n[B]usqueda \n[E]liminar \n[Q]uit:\n: ")
#     if opcion == 'Q':
#         break
#     elif opcion == 'I':
#         new_name = input("Insertar nombre: ")
#         contact_list.append(new_name.title())
#         numero_contacto = int(input("insertar numero de telefono: "))
#         # if numero_contacto == len()
#         #     print('inserte un numero valido')
#         # else:    
#         contact_list.append(numero_contacto)

#     else:
#         print("\nDebes seleccionar una de las opciones disponibles.\n")

# print(contact_list)


# print('no has seleccionado una opción valida')
        # break

#datos con lista

#new_name = "" DESACTIVADA
contact_diccionario = 
{}


while True:
      
    option = input("Que operación deseas realizar:\n[i]nsertar\n[a]ctualizar \n[b]usqueda \n[e]liminar \n[q]uit:\n: ")
    if option == 'q':
        print("Gracias, vuelva pronto")
        break

    if option == 'i':
        
        contact_diccionario['name'] = input("Insertar nombre: ") 
        phone = int(input("insertar numero de telefono: "))
        pass

        if len(str(phone)) > 0  and len(str(phone)) <= 9:

           contact_diccionario['phone'] = phone
           print(f"Se ha añadido a {contact_diccionario['name']} {contact_diccionario['phone']} a la lista de contactos.")

        else:
            print("Se debe de añadir un numero que no contenga mas de 9 digitos")

        pass
            
    elif option == 'b':
        
        consulta_nombre = input("Inserte nombre de busqueda: ")

        if consulta_nombre in contact_diccionario['name']:
            print(f"{contact_diccionario['name']} {contact_diccionario['phone']} existe en la lista\n")
        
        else:
            print(f"El usuario {consulta_nombre} no existe en la lista, verifique los datos\n")

        pass     

    elif option == 'a':
        consulta_nombre = input("Inserte nombre de busqueda: ")
        if consulta_nombre in contact_diccionario['name']:
            contact_diccionario['phone'] = int(input('Ingrese nuevo numero a actualizar: '))
        print(f"se ha actualizado el numero de {contact_diccionario['name']} por el número {contact_diccionario['phone']}")
        pass 

    elif option == 'e':
        consulta_nombre = input("Inserte nombre de busqueda: ")
        if consulta_nombre in contact_diccionario['name']:
            del contact_diccionario['name']
            del contact_diccionario['phone']
            print(f"se ha eliminado a {consulta_nombre} de la lista")
            pass 
        
    else:
        print("\nDebes seleccionar una de las opciones disponibles.\n")

print(contact_diccionario)