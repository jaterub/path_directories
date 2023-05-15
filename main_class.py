import os


class Main:
    @staticmethod
    def main():
        ruta_carpeta = r'C:\Users\34680\Desktop\panda IV\prueba'
        directorio = Directorio(ruta_carpeta)
        directorio.categorizar_archivos()


if __name__ == '__main__':
    Main.main()
