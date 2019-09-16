menu = True

while(menu):
    print("\nSelecciona una opcion para continuar\n")
    print("1.- Salud")
    print("2.- Dinero")
    print("3.- Autos")
    Inicio = int(input())

    if Inicio == 1:
        print("\nElegiste salud")
        break
        
    elif Inicio == 2:
        print("\nelegiste dinero")       
        break

    elif Inicio == 3:
        print("\nElegiste autos")       
        break
    else:
        print("\nEsa no es una opcion valida\n")
        menu = True
    
