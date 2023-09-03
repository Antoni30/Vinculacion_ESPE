from views.AdviceBox import MessageBox  
import customtkinter
import re
from views.View import View
import win32gui
import win32con

from tkinter import ttk


class FormExternalView(customtkinter.CTk,View):
    width = 1160
    height = 600
    header = 60
    textColor= "#000000"

    def __init__(self,controller):
        super().__init__()
        #controlador
        self.controller = controller

        self.title("ACCESO ESPE")
        self.geometry(f"{self.width}x{self.height}+100+70")

        self.resizable(False, False)
        # Obtener el identificador de la ventana principal de tu aplicación (ajusta esto)
        hwnd = win32gui.FindWindow(None,self.title())  # O usa win32gui.FindWindow(None, "Nombre de tu ventana")
        # Establecer la ventana en la parte superior de todas las ventanas
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        
         # set grid layout 1x2
        self.grid_rowconfigure(7, weight=1)
        self.grid_columnconfigure(2, weight=1)
       
        #create header grid
        
        self.header_form = customtkinter.CTkFrame(self, corner_radius=0,fg_color="#F3F3F3",height=self.header)
        self.header_form.grid(row=0, column=2,sticky="nsew")
    
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0,fg_color="#474646")
        self.navigation_frame.grid(row=1,rowspan=7, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(7, weight=1)

       #create navigation
        self.register_form_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,width=60, border_spacing=10, text="Registrar usuario",
                                                   fg_color="transparent", text_color=("#FFFFFF"), command=self.register_form_button_event,
                                                   anchor="w", hover_color="#1E9A5D")
        self.register_form_button.grid(row=1, column=0, sticky="ew")

        self.show_list_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,width=60, border_spacing=10, text="Listado de usuarios",
                                                      fg_color="transparent", text_color=("#FFFFFF"),command=self.show_list_button_event,
                                                      anchor="w", hover_color="#1E9A5D")
        self.show_list_button.grid(row=2, column=0, sticky="ew")

        #create external visit form
        self.form_frame = customtkinter.CTkFrame(self, corner_radius=0,fg_color="transparent")
        self.form_frame.grid_columnconfigure(1, weight=1)
        #self.form_frame.grid(column=1, sticky="nsew",padx=40)
        self.name_entry = customtkinter.CTkEntry(self.form_frame, width=300, placeholder_text="Nombres",fg_color="#E7FDF2" ,text_color=self.textColor,corner_radius=20)
        self.name_entry.grid(row=2, column=0, padx=40, pady=(15, 15),sticky="ew")
        self.id_entry = customtkinter.CTkEntry(self.form_frame, width=300, show="*", placeholder_text="Cedula",fg_color="#E7FDF2" ,text_color=self.textColor,corner_radius=20)
        self.id_entry.grid(row=3, column=0, padx=40, pady=(15, 15),sticky="ew")
        self.email_entry = customtkinter.CTkEntry(self.form_frame, width=300, placeholder_text="Correo electronico",fg_color="#E7FDF2",text_color=self.textColor,corner_radius=20)
        self.email_entry.grid(row=4, column=0, padx=40, pady=(15, 15),sticky="ew")
        self.place_entry = customtkinter.CTkEntry(self.form_frame, width=300, show="*", placeholder_text="Lugar de destino",fg_color="#E7FDF2",text_color=self.textColor,corner_radius=20)
        self.place_entry.grid(row=5, column=0, padx=40, pady=(15, 15),sticky="ew")
        self.lastname_entry = customtkinter.CTkEntry(self.form_frame, width=300, placeholder_text="Apellidos",fg_color="#E7FDF2",
        text_color=self.textColor,corner_radius=20)
        self.lastname_entry.grid(row=2, column=1, padx=40, pady=(15, 15),sticky="ew")
        self.phone_entry = customtkinter.CTkEntry(self.form_frame, width=300, show="*", placeholder_text="Numero de celular",fg_color="#E7FDF2",text_color=self.textColor,corner_radius=20)
        self.phone_entry.grid(row=3, column=1, padx=40, pady=(15, 15),sticky="ew")
        self.exit_time_entry = customtkinter.CTkEntry(self.form_frame, width=300, placeholder_text="Hora de salida",fg_color="#E7FDF2",text_color=self.textColor,corner_radius=20)
        self.exit_time_entry.grid(row=4, column=1, padx=40, pady=(15, 15),sticky="ew")
        self.person_addressed_entry = customtkinter.CTkEntry(self.form_frame, width=300, show="*", placeholder_text="Persona a la que se dirige",fg_color="#E7FDF2",text_color=self.textColor,corner_radius=20)
        self.person_addressed_entry.grid(row=5, column=1, padx=40, pady=(15, 15),sticky="ew")
        self.obsevation_entry = customtkinter.CTkEntry(self.form_frame,fg_color="#E7FDF2" ,text_color=self.textColor,height=100,width=500,placeholder_text="Observaciones",corner_radius=10)
        self.obsevation_entry.grid(row=6, column=0,columnspan=1,sticky="ew",padx=20 )
        self.register_button = customtkinter.CTkButton(self.form_frame, text="Registrar",  width=200, fg_color="#1E9A5D")
        self.register_button.grid(row=7, column=0,columnspan=1, padx=80, pady=(15, 15),sticky="ew")
       
        #create show person list
        self.header_list = ttk.Treeview(self, columns=['nombres', 'apellidos', 'lugar destino', 'hora salida'], show='headings')
        self.header_list.heading('nombres', text='Nombres')
        self.header_list.heading('apellidos', text='Apellidos')
        self.header_list.heading('lugar destino', text='Lugar destino')
        self.header_list.heading('hora salida', text='Hora salida')
        self.header_list.grid(row = 3,rowspan = 7, column = 1,sticky="nsew")
        
        
        # select default frame
        self.select_frame_by_name("Listado de usuarios")
        #header list user

        
        
    def select_frame_by_name(self, name):
    # set button color for selected button
        self.register_form_button.configure(fg_color="#1E9A5D" if name == "Registrar usuario" else "transparent")
        self.show_list_button.configure(fg_color="#1E9A5D" if name == "Listado de usuarios" else "transparent")
        
        # show selected frame
        if name == "Registrar usuario":
            self.form_frame.grid(row=1, column=2,columnspan=2, sticky="nsew")
        else:
            self.form_frame.grid_forget()
        if name == "Listado de usuarios":
            self.header_list.grid(row=3, column=2,rowspan=7, sticky="nsew")
        else:
            self.header_list.grid_forget()
            

    def register_form_button_event(self):
        self.select_frame_by_name("Registrar usuario")

    def show_list_button_event(self):
        print("mostrar")
        self.select_frame_by_name("Listado de usuarios")


    #verify entry 
    def verify_entry(self):
        entry = [self.name_entry.get(), self.email_entry.get(), self.place_entry.get(), self.lastname_entry.get(),
                self.phone_entry.get(),self.exit_time_entry.get(),self.person_addressed_entry.get()]
        if '' in entry:
            return MessageBox(self, 'Los campos deben ser completados!')
        else:
            try:
                email_expresion = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

                re.match(email_expresion, self.email_entry)
                #print("Correo electrónico válido.")
            except:
                return MessageBox(self, 'Correo electronico invalido!')
        return True
    
    def destroy_win(self):
        #self.main.atualizar_view()
        #self.main.deiconify()
        self.destroy()
    """  
   def create_user(self):
        add_new_user = Controller()
        if self.verify_entry():
            add_new_user.add_user(self.name_entry.get(), self.lastname_entry.get(), self.place_entry.get(), self.exit_time_entry.get())
            self.destroy_win()
    """
    
    """
    @Overrite
    """
    def main(self):
        self.mainloop()
    """
    @Overrite
    """
    def close(self):
        return
