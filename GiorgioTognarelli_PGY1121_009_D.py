# Arreglo
arr = [[99999999, "TXT", "99999999-TXT", "Juan", "12/01/2005", "Soltero","no"]]

# Funciones
def grabar(cod_num, cod_txt, cod_compl, nom, fecha, estado, pertenece):
  new_arr = [cod_num, cod_txt, cod_compl, nom, fecha, estado, pertenece]

  arr.append(new_arr)
  return arr
  
def buscar(cod_compl):
  cod = False
  for i in range(len(arr)):
    if cod_compl == arr[i][2]:
      print(f"NIF: {arr[i][2]}")
      print(f"Nombre: {arr[i][3]}")
      print(f"Fecha de nacimiento: {arr[i][4]}")
      print(f"Estado conyugal: {arr[i][5]}")
      print(f"Pertenece a la Union Europea: {arr[i][6]}")

      cod = True
    else:
      cod = False

  if cod == False:
    print("esta persona no esta registrada")
  
def imprimir():
  for i in range(len(arr)):
    print("")
    print("----------------------------")
    print("")
    print(f"NIF: {arr[i][2]}")
    print(f"Nombre: {arr[i][3]}")
    print(f"Fecha de nacimiento: {arr[i][4]}")
    print(f"Estado conyugal: {arr[i][5]}")
    print(f"Pertenece a la Union Europea: {arr[i][6]}")
    print("")
    print("----------------------------")
    print("")
    
def menu():
    print("Menu")
    print("1.- Grabar")
    print("2.- Buscar")
    print("3.- Imprimir")
    print("0.- Salir")

def verificar(variable):
  try:
    int(variable) 
    return int(variable) 
  except: 
    print("ocurrio un error, intente ingresar el valor correcto")
    return "error" 


i = True 



while i == True:
  menu()

  op = input("Ingresa una opcion: ") 
  op_verificado = verificar(op)

  if op_verificado == "error":
    continue

  if op_verificado == 1:
    cod_num = input("Ingresa la parte numerica de tu NIF: ")
    verif_num = verificar(cod_num)

   
    if verif_num == "error":
      continue 
    if len(str(verif_num)) != 8:
      print("El largo debe ser de 8")
      continue

    
    cod_text = input("Ingrese la segunda parte de su NIF: ")

    
    if len(cod_text) != 3:
      print("El largo debe ser de 3")
      continue

    cod_compl = f"{verif_num}-{cod_text}"
    nom = input("Ingrese su nombre: ")
    fecha = input("Ingrese su fecha de nacimiento: ")
    estado = input("Ingrese su estado: ")
    pertenece = input("Ingrese si pertenece a la Union Europea (si/no)")
    

    arreglo_nuevo = grabar(cod_num, cod_text, cod_compl, nom, fecha, estado, pertenece)
    print(arreglo_nuevo)
  elif op_verificado == 2:
    NIF = input("ingrese sus NIF: ")
    buscar(NIF)
    
  elif op_verificado == 3:
    imprimir()
  elif op_verificado == 0:
    print("Gracias por preferirnos")
    print("Lucciano Tognarelli")
    print("Version 1.0")
    break
  else: 
    print("Ingrese una de las opciones 1/2/3/0")