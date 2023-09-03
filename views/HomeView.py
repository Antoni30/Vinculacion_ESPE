from typing import Optional, Tuple, Union
import customtkinter
from PIL import Image
import os

"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""
class HomeView(customtkinter.CTk):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    width = 1160
    height = 600
    current_path = os.path.dirname(os.path.realpath(__file__))
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """
    def __init__(self, controller):
        super().__init__()
        self.title("Univerdidad de las Fuerzas Armadas 'ESPE'")
        self.geometry(f"{self.width}x{self.height}+100+70")
        self.overrideredirect(True)
        self.homeController = controller
        self._backgroud()
        self._make_mainFrame()
        self._make_options()
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Creates view's frame.
    """
    def _backgroud(self):
        self.bg_image = customtkinter.CTkImage(Image.open(self.current_path + "/Image/bg.jpg"),
                                               size=(900, 600))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.grid(row=0, column=0)

    def _make_mainFrame(self):
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=1, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="ESPE-Registro\nLogin",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

    def _make_options(self):
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Ingresar", command=self.login_event, width=200)
        self.close_button = customtkinter.CTkButton(self.login_frame, text="Salir", command=self.close, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.close_button.grid(row=4, column=0, padx=30, pady=(5, 5))

    #functions of options

    def login_event(self):
        inputs =[self.username_entry.get(), self.password_entry.get()]
        self.username_entry.delete(0,len(self.username_entry.get()))
        self.password_entry.delete(0,len(self.password_entry.get()))
        self.homeController.btnClicked(inputs)

    """
    @Overrite
    """
    def main(self):
        self.mainloop()
    """
    @Overrite
    """
    def close(self):
        self.destroy()


