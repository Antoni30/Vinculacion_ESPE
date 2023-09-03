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
            #Set the window at the top of all windows.
            hwnd = win32gui.FindWindow(None,"Univerdidad de las Fuerzas Armadas 'ESPE'")
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            app.main()
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    Main.run()