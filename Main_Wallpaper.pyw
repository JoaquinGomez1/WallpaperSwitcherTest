import ctypes, time, os
import tkinter as tk
from tkinter import messagebox


def Start():
    ArchivoConfig = open("config.txt", "w")
    ArchivoConfig.write("Destino de cada imagen: ")
    for i in range(CImagenes):
        ArchivoConfig.write("\nImagen 0{}=".format(i))
    ArchivoConfig.close()


def Check(): #Esta funcion se encarga de chequear la hora y cambiar el fondo de pantalla
    if vec == None:
        return None

    CurrentTime = time.strftime("%H:%M:%S")
    for i in range(len(ListaDeTiempos)):
        if ListaDeTiempos[i] <= str(CurrentTime) <= ListaDeTiempos[i + 1]:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, str(vec[i + 1]), 3)  # Comando para cambiar el Wallpaper

        elif ListaDeTiempos[0] >= CurrentTime:  # Considero que es de noche
            ctypes.windll.user32.SystemParametersInfoW(20, 0, str(vec[-1]), 3)

        elif CurrentTime >= ListaDeTiempos[-1]:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, str(vec[-1]), 3)


def ReadPaths():
    ArchivoConfig = open("config.txt", "r")
    path = ArchivoConfig.read()
    Lista = path.splitlines()  # path contiene toda la info como string y con esto lo divido en una lista
    for i in range(1, len(Lista)):
        Lista[i] = Lista[i].replace("Imagen 0{}=".format(i - 1), "").lower()
        if not os.path.exists(Lista[i]):
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(message='La direccion {} no existe. Verificá que esté escrita correctamente'.format(Lista[i]),
                             title='Direccion no encontrada')
            return None

    return Lista


if __name__ == "__main__":
    ListaDeTiempos = ["04:00:00", "06:00:00", "12:00:00", "17:00:00", "19:30:00", "21:00:00"]
    creado = False
    CImagenes = 6

    if not os.path.exists("config.txt"):
        Start()
    else:
        creado = True
    vec = ReadPaths()

    while creado:
        Check()
        time.sleep(60)