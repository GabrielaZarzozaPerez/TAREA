Nombres = []
opciones = (1,2,3,4)
i = 0
cont = True


while(cont):
    print("\nSelecciona la opcion que quieres realizar")
    print("1.- Introducir un nombre")
    print("2.- Consultar nombres")
    print("3.- Total de nombres registrados")
    print("4.- Salir\n")
    inicio = int(input())
    
    if inicio in opciones:
        if inicio == 1:
            print("\nIntroduce el nombre")
            Nomb = input()
            Nombres.insert(i,Nomb)
            print("\nNombre guardado")
            i = i+1

        elif inicio == 2:
            print("\nNombres introducidos:")
            j = 0
            f = 1

            while j < i:
                print(f"{f}.- {Nombres[j]}\n")
                j = j + 1
                f = f + 1

        elif inicio == 3:
            print(f"Total de nombres registrados: {i}\n")
        
        elif inicio == 4:
            cont = False
        
    else:
        print("\nEsa no es una opcion valida\n")
        cont = True
