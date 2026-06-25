coleccion_productos = []

def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    else:
        return True
    
def validacion_de_stock(stock):
    if stock >= 0:
        return True
    else:
        return False
def validacion_de_precio(precio):
    if  precio > 0:
        return True
    else:
        return False
    
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto ")
    print("2. Buscar producto")
    print("3. Eliminar producto ")
    print("4. Actualizar disponibilidad ")
    print("5. Mostrar productos ")
    print("6. Salir ")
    print("===================================== ")
    
def obtener_opcion():
    opcion = int(input("Seleccione una opcion (1 - 6): "))
    while opcion < 1 or opcion > 6:
        print("Opcion invalida")
        opcion = int(input("Seleccione una opcion (1 - 6): "))
    return opcion


def agregar_producto(lista):
    nombre = input("Ingrese el nombre del producto: ")
    stock = int(input("Ingrese la cantidad de unidades que hay en bodega: "))
    precio = float(input("Ingrese el precio del producto es -CLP- : "))
    
    validar_nombre()
    validacion_de_stock()
    validacion_de_precio()
    
    if validar_nombre == False:
        print("ERROR ,el nombre no puede estar vacio ni ser solo espacios en blanco")
    elif validacion_de_stock == False:
        print("ERROR, el stock tiene que ser un numero entero mayor o igual a cero")
    elif validacion_de_precio == False:
        print("ERROR, el precio debe de ser un numero decimal mayor que cero")
    else:
        
        producto = {
            "nombre": nombre,
            "stock": stock,
            "precio": precio,
            "disponibilidad": False
        }
        lista.append(producto)
        print("Producto agregado correctamente")
        


def buscar_producto(lista, nombre_buscado):
    posicion =- 1
    i = 0
    while i < len(lista):
        if lista[i]["nombre"] == nombre_buscado:
            posicion = i
        i = + i
    return posicion




def actualizar_producto(lista):
    i = 0
    while i < len(lista):
        if lista[i]["stock"] > 0:
            lista[i]["disponibilidad"] = True
        else:
            lista[i]["disponibilidad"] = False
            
        i = i + 1
        
        
def eliminar_producto(lista):
    nombre_eliminar = input("Ingrese el nombre del producto que desea eliminar")
    
    posicion = buscar_producto(lista, nombre_eliminar)
    
    if posicion != -1:
        
        lista.pop(posicion)
        print("Producto eliminado con exito")
    else:
        print(f"El procuto -{nombre_eliminar}- no se encuentra registrado")
        
def mostrar_productos(lista):
    actualizar_producto(lista)
    
    print("Lista de productos")
    i = 0
    while i < len(lista):
        print("Nombre:", lista[i]["nombre"])
        print("Stock:", lista[i]["stock"])
        print("Precio", lista[i]["precio"])
        
        if lista[i]["disponible"] == True:
            print("Estado: Disponible")
        else:
            print("Estado: Sin Stock")
            
        i = i + 1
        







opcion_elegida = 0

while opcion_elegida != 6:
    mostrar_menu()
    opcion_elegida() = obtener_opcion()

    
    if opcion_elegida == 1:
        agregar_producto(coleccion_productos)
        
    elif opcion_elegida == 2:
        print("Buscar producto")
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
        posicion = buscar_producto(coleccion_productos, nombre_buscar)
        
        if posicion != -1:
            print("Posicion en la lista:", posicion)
            print("Nombre:", coleccion_productos[posicion]["nombre"])
            print("Stock:", coleccion_productos[posicion]["stock"])
            print("Precio:", coleccion_productos[posicion]["precio"])
            
            
        
                 
            
        
    