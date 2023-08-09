
from models.External import External
from views.FormExternal import Form_External

class Controller:
    """ Controla los modelos
    """
    def __init__(self):
        self.list_users = []
        
        def add_user(self, names, lastnames,place, exitTime):
            ci = ''
            email = ''
            entryTime = ''
            visitDuration = ''
            try:
                self.list_users.append(External(names, lastnames, ci, email, place, entryTime, exitTime, visitDuration))
                #self.list_users.append(External(names, lastnames,place, exitTime))
                print('CREADO', self.list_users)
                return True
            except:
                return False
            