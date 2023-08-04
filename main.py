from views.Login import Login
from models.Internal import Internal
from controllers.db_controller import *

if __name__ == "__main__":
    
    # login = Login()
    # login.mainloop()
    user = Internal(campus='matriz', 
         career='software',
         ci='1725205106',
         email='ttoapanta1@espe.edu.ec',
         id_espe='L00001',
         lastnames='Toapanta',
         names='Toni',
         type_espe='student'
        )
    usuarioB= usuario(user)
    add_user_db(usuarioB)
    
    

