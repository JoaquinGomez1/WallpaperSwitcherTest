import ctypes
import os
import time
import tkinter as tk
from tkinter import messagebox


def Start():
    ArchivoConfig = open("config.txt", "w")
    ArchivoConfig.write("Destino de cada imagen: ")
    for i in range(CImagenes):
        ArchivoConfig.write("\nImagen 0{}=".format(i))
    ArchivoConfig.close()


def Check():  # Esta funcion se encarga de conseguir la hora y cambiar el fondo de pantalla
    if vec == None:
        return None

    CurrentTime = time.strftime("%H:%M:%S")
    for i in range(len(ListaDeTiempos)):
        if ListaDeTiempos[i] <= str(CurrentTime) <= ListaDeTiempos[i + 1]:
            # Comando para cambiar el Wallpaper:
            ctypes.windll.user32.SystemParametersInfoW(0x14, 0, str(vec[i + 1]), 0x3)

        elif ListaDeTiempos[0] >= CurrentTime:  # Considero que es de noche
            ctypes.windll.user32.SystemParametersInfoW(0x14, 0, str(vec[-1]), 0x3)

        elif CurrentTime >= ListaDeTiempos[-1]:
            ctypes.windll.user32.SystemParametersInfoW(0x14, 0, str(vec[-1]), 0x3)


def ReadPaths():  # Devuelve una lista con los directorios si todó funciona bien, sino devuelve None
    ArchivoConfig = open("config.txt", "r")
    path = ArchivoConfig.read()
    Lista = path.splitlines()  # path contiene toda la info como string y con esto lo divido en una lista

    for i in range(1, len(Lista)):
        Lista[i] = Lista[i].replace("Imagen 0{}=".format(i - 1), "").lower()
        Lista[i] = os.path.normpath(Lista[i])

        if not os.path.exists(Lista[i]):  # Mostramos errores según que es lo que ha fallado
            root = tk.Tk()
            root.withdraw()
            if Lista[i] == "":
                messagebox.showerror(message='Tenés que completar los seis directorios de imagenes', title='Completar')
            else:
                messagebox.showerror(
                    message='La dirección {} no existe. Verificá que esté escrita correctamente'.format(
                        Lista[i].upper()),
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