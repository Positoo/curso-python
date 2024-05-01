#crear una funcion para cargar los datos en el diccionario (BD)
def registrar (dic):
    #comprobar que dic sea del tipo diccionario
    if type(dic) == dict:

        user = input("ingrese nombre de Usuario: ")
        pas = input("ingrese contraseña: ")

        if user in dic: #comprobar que el usuario ya no exista en el diccionario (BD)
            return("\nLo siento, ese Usuario ya existe")
        else:
            dic[user] = pas #cargamos el usuario al diccionario (BD)
            return("\nUsuario cargado con exito")   
    else:#mensaje de error en caso de no ser un diccionario lo que ingreso por parametro
        return("Error: el argumento ingresado no es un diccionario")

#-----------------------------------------------------------------------------------



#crear una funcion login donde comprube que el usuario y su contraseña existan

def login (dic):
    try:
        user = input("ingrese usuario para login: ")
        pas = input("contraseña del usuario: ")

        if user in dic and pas == dic[user]: #comprobar que exista el usuario y su contraseña en el diccionario
            return("\nLogeado")
        else:
            return("\nUsuario o contraseña incorrecto")
    
    except:
        return("Error en algun tipo de argumento")
#---------------------------------------------------------------------------------------    

#funcion para imprimir en pantalla todo el diccionario (db)
def mostrar(dic):
    datos="Los datos de la DB son:\n"
    for user in dic:
        datos += user +" "+ str(dic.get(user))+"\n"
    return datos

#---------------------------------------------------------------------------------------

#funcion para crear un archivo txt del diccionario (db)
def crearTxt(dic):
    nomArchivo = input("ingrese un nombre para el archivo txt: ")
    nomArchivo = nomArchivo+".txt"#asignacion de la extencion del archivo
    with open(nomArchivo, 'w') as archivo:
        archivo.write(str(dic))
    return "Archivo creado"

#----------------------------------------------------------------------------------------


#---PSEUDO MENU--------------------------------------------------------------------------

spWhile = "s" #sp=set point
#db = {"a":1, "b":2, "c":3}
db = {}

while spWhile != "n":
    print("\n 1:Registrar un nuevo usaurio\n 2:Login\n 3:Crear un txt\n 4:Mostrar datos\n 5:Salir")
    try:
        opcion = int(input("\nElija una opción: "))
        if opcion==1:
            #print("entra a REGISTRAR")
            print(registrar(db))
        elif opcion==2:
            #print("entra a LOGIN")
            print(login(db))
        elif opcion==3:
        #print("entra a CREAR TXT")
            print(crearTxt(db))
        elif opcion==4:
            print(mostrar(db))
            # for user in db:
            #     print(user," ",db[user])
        elif opcion==5:
            spWhile = "n"
            print("\n***Fin del Programa***\n")
        else:
            print("\nOpcion no existente")
    except ValueError as exc:
        print(f"Por favor ingrese una opcion numerica. Error: {exc}")


#-----------------------------------------------------------------------------------------