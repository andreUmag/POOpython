import Object
from datetime import *
listE = []

def menu():
    option = int(input("\t EMPRRESA.SA \n1.Add Trabajador Practicante "
                       "\n2.Add Trabajador de planata \n3.Mostrar Personal "
                       "\n4.Salir \nOpcion: "))
    if option == 1 or option == 2:
        print("INGRESE LOS DATOS:")
        cc = input("CC: ")
        ln = input("Apellido: ")
        day = int(input("Dia: "))
        mouth = int(input("Mes: "))
        year = int(input("Año: "))
        dateIn = date(year, mouth, day)

    if option == 1:
        cliAt = int(input("Cantidad de clientes atendidos: "))
        ob = Object.PersonneReply(cc, ln, dateIn, cliAt)
        listE.insert(0,ob)
        menu()
    elif option == 2:
        salaryBas = float(3500000)
        obb = Object.PersonnelHired(cc, ln, dateIn, salaryBas)
        listE.insert(0, obb)
        menu()
    elif option == 3:
        for i in range(len(listE)):
            print(listE[i])
        menu()
    elif option == 4:
        print("--------------------Saliendo--------------------")
    else:
        print("Opcion no reconocida")
        menu()

menu()