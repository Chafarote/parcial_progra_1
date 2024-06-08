
def menu():
    print("---Eliga una opcion---")
    print("----------------------")
    print("1) Cargar archivo CSV")
    print("2) Imprimir lista")
    print("3) Asignar estadisticas")
    print("4) Filtrar por mejores posts")
    print("5) Filtrar por haters")
    print("6) Informar promedio de followers")
    print("7) Ordenar los datos por nombre de user ascendente")
    print("8) Mostrar más popular")
    print("9) Salir")
    return input("Ingrese una opcion: ")

def get_path_actual(nombre_archivo):
    """Obtiene la ruta en la que se esta trabajando actualmente

    Args:
        nombre_archivo (str): nombre del archivo trabajado

    Returns:
        path: devuelve el path hacia el archivo
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def cargar_archivo_csv(nombre_archivo:str, lista:list)->None:
    """Carga el archivo CSV de los posts

    Args:
        nombre_archivo (str): Nombre del archivo a cargar
        lista (list): Lista en la que se cargan los datos
    """
    with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
        encabezado = archivo.readline().strip("\n").split(",")

        for linea in archivo.readlines():
            post = {}
            linea = linea.strip("\n").split(",")

            id, user, likes, dislikes, followers = linea
            post["id"] = int(id)
            post["user"] = user
            post["likes"] = int(likes)
            post["dislikes"] = int(dislikes)
            post["followers"] = int(followers)
            lista.append(post)
    print("Archivo cargado con exito...")

def mostrar_posts(lista:list)->None:
    """muestra los datos de todos los posts de una lista

    Args:
        lista (list): lista de posts
    """
    print("           *** Lista de posts***")
    print(" id         user        likes  dislikes  followers")
    print("--------------------------------------------------")
    for i in range(len(lista)):
        mostrar_post(lista[i])
    print("")

def mostrar_post(un_post:dict)->None:
    """muestra los datos de un post

    Args:
        un_post (dict): ingresan los datos del post
    """
    print(f"{un_post["id"]:3}    {un_post["user"]:15} {un_post["likes"]:5}    {un_post["dislikes"]:5}      {un_post["followers"]:5}")

def asignar_estadisticas(lista:list):
    """Genera numeros aleatorios para los campos indicados

    Args:
        lista (list): Recibe la lista que modifica
    """
    asignar_valor_random_key(lista, "likes", 500, 3000)
    asignar_valor_random_key(lista, "dislikes", 300, 3500)
    asignar_valor_random_key(lista, "followers", 10000, 20000)

def asignar_valor_random_key(lista:list, key:str, minimo:int, maximo:int):
    """Genera numeros random para reemplazar un valor en especifico de un diccionario

    Args:
        lista (list): lista a modificar
        key (str): valor que se busca reemplazar
        minimo (int): valor minimo
        maximo (int): valor maximo
    """
    from random import randint
    tam = len(lista)
    for i in range(tam):
        lista[i][key] = randint(minimo, maximo)

def filtrar_lista(filtradora, lista:list)->list:
    """filtra los elementos de una lista

    Args:
        filtradora (_type_): funcion para filtrar los datos deseados
        lista (list): lista que se va a filtrar

    Returns:
        list: retorna una lista nueva con los datos ya filtrados
    """
    lista_retorno = []
    for elemento in lista:
        if filtradora(elemento):
            lista_retorno.append(elemento)
    return lista_retorno

def generar_archivo_csv(lista:list, nombre_archivo:str):
    """genera un archivo csv en el directorio actual

    Args:
        lista (list): ingresa una lista con los datos que se desean guardar
        nombre_archivo (str): ingresa el nombre que se desea para el archivo
    """
    with open(get_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for elemento in lista:
            values = list(elemento.values())
            l = []
            for value in values:
                if isinstance(value, int):
                    l.append(str(value))
                elif isinstance(value, float):
                    l.append(str(value))
                else:
                    l.append(value)
            linea = ",".join(l) + "\n"
            archivo.write(linea)

def filtrar_mejores_posts(lista:list):
    """filtra los mejores posts usando la funcion de filtrar y lo guarda en un archivo csv

    Args:
        lista (list): lista con los datos que se deben cargar en el archivo csv
    """
    lista_filtrada = filtrar_lista(lambda post: post["likes"] >= 2000, lista)
    generar_archivo_csv(lista_filtrada, "mejores_posts.csv")

def filtrar_haters_posts(lista:list):
    """filtra los posts con mas haters y los guarda en un archivo csv

    Args:
        lista (list): lista con los datos que se deben cargar en el archivo csv
    """
    lista_filtrada = filtrar_lista(lambda post: post["dislikes"] > post["likes"], lista)
    generar_archivo_csv(lista_filtrada, "haters.csv")

def acumular_elemento_en_lista(key, lista:list)->list:
    """guarda en una lista los numeros enteros de una key

    Args:
        key (str): key de los valores a guardar en la lista nueva
        lista (list): lista de la que se busca extraer los valores

    Returns:
        list: retorna una lista solo con los valores de la misma key
    """
    lista_aux = []
    for elemento in lista:
            lista_aux.append(float(elemento[key]))
    return lista_aux

def promedio_elementos_lista(lista:list)->float:
    """hace el promedio de todos los enteros de una lista

    Args:
        lista (list): lista con enteros

    Returns:
        float: retorna el promedio
    """
    tam = len(lista)
    acumulador = 0
    for elemento in lista:
        acumulador += elemento
    return acumulador / tam

def mostrar_promedio_followers(lista:list)->None:
    """muestra el promedio de los followers

    Args:
        lista (list): recibe la lista de la cual se hace el promedio
    """
    print(f"El promedio de followers es: {promedio_elementos_lista(acumular_elemento_en_lista("followers", lista))}")

def swap_dict(lista:list, i:int, j:int)->None:
    """swapea elementos de una lista

    Args:
        lista (list): lista de diccionarios
        i (int): indice comparado
        j (int): indice con el que se compara
    """
    aux_diccionario = lista[i]
    lista[i] = lista[j]
    lista[j] = aux_diccionario

def ordenar_lista_usuario(lista:list)->None:
    """ordena la lista de posts segun los usuarios de forma ascendente

    Args:
        lista (list): lista a ordenar
    """
    tam = len(lista)
    for i in range(tam -1):
        for j in range(i +1, tam):
            if lista[i]["user"] > lista[j]["user"]:
                swap_dict(lista, i, j)

def generar_archivo_json(lista:list, nombre_archivo:str):
    """genera un archivo json

    Args:
        lista (list): lista con los datos a guardar en el archivo
        nombre_archivo (str): nombre que se le quiere dar al archivo
    """
    import json
    with open(get_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4)

def mostrar_mas_popular(lista:list)->None:
    """muestra el o los usuarios mas populares segun su cantidad de likes

    Args:
        lista (list): lista de la cual se va buscar el maximo
    """
    lista_maximos = maximo_elementos_lista(lista, "likes")
    print("---Usuarios mas populares---")
    for elemento in lista_maximos:
        print(f"{elemento["user"]:15} {elemento["likes"]}")

def maximo_elementos_lista(lista:list, key:str)->list:
    """genera una lista con el o los elementos de una lista que tengan el maximo valor de una key

    Args:
        lista (list): lista de datos
        key (str): key que se busca comparar

    Returns:
        list: retorna una lista con el o los datos que sean el maximo
    """
    lista_retorno = []
    flag = True
    for elemento in lista:
        if flag == True or elemento[key] > maximo:
            maximo = elemento[key]
            lista_retorno = []
            lista_retorno.append(elemento)
            flag = False
        elif elemento[key] == maximo:
            lista_retorno.append(elemento)
    return lista_retorno