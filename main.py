# -*- encoding:utf-8 -*-
from core.Core import Core
import win32gui
import win32con


"""
    Main class. Responsible for running the application.
"""
class Main:
    @staticmethod
    def run():
        try:
            app = Core.openController("home")
            # Obtener el identificador de la ventana principal de tu aplicación (ajusta esto)
            hwnd = win32gui.FindWindow(None,"Univerdidad de las Fuerzas Armadas 'ESPE'")  # O usa win32gui.FindWindow(None, "Nombre de tu ventana")
            # Establecer la ventana en la parte superior de todas las ventanas
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            app.main()
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    Main.run()