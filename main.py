from funciones import *

"""
Nombre: Gomez Gabriel Matias
DNI: 38942983

"""

posts = []

while True:
    match menu():
        case "1":
            cargar_archivo_csv("posts.csv", posts)
        case "2":
            mostrar_posts(posts)
        case "3":
            asignar_estadisticas(posts)
        case "4":
            filtrar_mejores_posts(posts)
        case "5":
            filtrar_haters_posts(posts)
        case "6":
            mostrar_promedio_followers(posts)
        case "7":
            ordenar_lista_usuario(posts)
            generar_archivo_json(posts, "usuarios_ordenado_ascendente.json")
        case "8":
            mostrar_mas_popular(posts)
        case "9":
            break

