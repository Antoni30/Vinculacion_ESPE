# -*- encoding:utf-8 -*-
from tkinter import messagebox
from core.Controller import Controller
from core.Core import Core

"""
    Main controller. It will be responsible for program's main screen behavior.
"""
class HomeController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.homeView = self.loadView("Home")

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Opens controller according to the option chosen
    """

    def btnClicked(self, inputs):
       user,password= inputs
       if user=="admin" and password=="admin":
            self.homeView.close()
            c = Core.openController("formExternal")
            c.main()
       else:
           messagebox.showerror("Usuario No Encontrado", "Contraseña o Usuario son incorrectos")

           
    """
        @Override
    """

    def main(self):
        self.homeView.main()