import requests
import webbrowser
import os

def obtener_imagenes_gato(api_key, cantidad=10):
    imagenes = []
    url = f"https://api.thecatapi.com/v1/images/search?limit={cantidad}"
    headers = {"x-api-key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    for cat in data:
        imagenes.append(cat["url"])
    return imagenes

def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    with open(nombre_archivo, 'wb') as f:
        f.write(response.content)

def generar_pagina_web(imagenes):
    contenido_html = "<html><head><title>Imágenes de gatos</title></head><body>"
    for imagen in imagenes:
        nombre_archivo = imagen.split("/")[-1]
        descargar_imagen(imagen, nombre_archivo)
        contenido_html += f'<img src="{nombre_archivo}" alt="Gato">'
    contenido_html += "</body></html>"
    with open("gatos.html", "w") as f:
        f.write(contenido_html)
    return os.path.abspath("gatos.html")

def abrir_en_navegador(url):
    webbrowser.open(url)

def main():
    api_key = 'live_duxn2a1r9M9pzboRSn06dO7NIoR4HhyyBlrrVlLXiaibC2OUjsbhAi8LZ8KB2QgS' 
    print("Obteniendo imágenes de gatos...")
    imagenes = obtener_imagenes_gato(api_key)
    print("Descargando imágenes...")
    ruta_pagina_web = generar_pagina_web(imagenes)
    print("Abriendo página web en el navegador...")
    abrir_en_navegador(ruta_pagina_web)

if __name__ == "__main__":
    main()

