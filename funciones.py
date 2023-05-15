import os


def categorizar_archivos(ruta_carpeta):
    # Definir las categorías y sus correspondientes extensiones
    categorias = {
        'documentos': ('.pdf', '.docx', '.xlsx'),
        'imagenes': ('.jpg', '.png', '.gif'),
        'videos': ('.mp4', '.avi', '.mkv'),
        'audio': ('.mp3', '.wav', '.aac')
    }

    # Crear un diccionario vacío para almacenar las carpetas y los archivos de cada categoría
    carpetas_archivos = {categoria: [] for categoria in categorias}

    # Recorrer la carpeta y clasificar los archivos según su extensión
    for archivo in os.listdir(ruta_carpeta):
        # Obtener la extensión del archivo
        extension = os.path.splitext(archivo)[1]
        # Buscar la categoría correspondiente para la extensión del archivo
        for categoria, extensiones in categorias.items():
            if extension in extensiones:
                # Agregar el archivo a la lista de archivos de la categoría correspondiente
                carpetas_archivos[categoria].append(archivo)
                break

    # Crear las carpetas correspondientes a las categorías dentro de la carpeta principal
    for categoria in categorias:
        ruta_carpeta_nueva = os.path.join(ruta_carpeta, categoria)
        os.makedirs(ruta_carpeta_nueva, exist_ok=True)

    # Mover los archivos a las carpetas correspondientes
    for carpeta, archivos in carpetas_archivos.items():
        ruta_carpeta_nueva = os.path.join(ruta_carpeta, carpeta)
        for nombre_archivo in archivos:
            ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
            ruta_archivo_nueva = os.path.join(
                ruta_carpeta_nueva, nombre_archivo)
            os.rename(ruta_archivo, ruta_archivo_nueva)


def main():
    ruta_carpeta = r'C:\Users\34680\Desktop\panda IV\prueba'
    categorizar_archivos(ruta_carpeta)


if __name__ == '__main__':
    main()
