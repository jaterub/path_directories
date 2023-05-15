import os


class Fichero:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.extension = os.path.splitext(ruta_archivo)[1]


class Directorio:
    def __init__(self, ruta_carpeta):
        self.ruta_carpeta = ruta_carpeta
        self.categorias = {
            'documentos': ('.pdf', '.docx', '.xlsx'),
            'imagenes': ('.jpg', '.png', '.gif'),
            'videos': ('.mp4', '.avi', '.mkv'),
            'audio': ('.mp3', '.wav', '.aac')
        }

    def categorizar_archivos(self):
        # Crear un diccionario vacío para almacenar las carpetas y los archivos de cada categoría
        carpetas_archivos = {categoria: [] for categoria in self.categorias}

        # Recorrer la carpeta y clasificar los archivos según su extensión
        for archivo in os.listdir(self.ruta_carpeta):
            fichero = Fichero(os.path.join(self.ruta_carpeta, archivo))
            # Buscar la categoría correspondiente para la extensión del archivo
            for categoria, extensiones in self.categorias.items():
                if fichero.extension in extensiones:
                    # Agregar el archivo a la lista de archivos de la categoría correspondiente
                    carpetas_archivos[categoria].append(fichero)
                    break

        # Crear las carpetas correspondientes a las categorías dentro de la carpeta principal
        for categoria in self.categorias:
            ruta_carpeta_nueva = os.path.join(self.ruta_carpeta, categoria)
            os.makedirs(ruta_carpeta_nueva, exist_ok=True)

        # Mover los archivos a las carpetas correspondientes
        for carpeta, archivos in carpetas_archivos.items():
            ruta_carpeta_nueva = os.path.join(self.ruta_carpeta, carpeta)
            for fichero in archivos:
                ruta_archivo_nueva = os.path.join(
                    ruta_carpeta_nueva, os.path.basename(fichero.ruta_archivo))
                os.rename(fichero.ruta_archivo, ruta_archivo_nueva)


if __name__ == '__main__':
    Main.main()
