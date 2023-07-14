from Person import Person 

class Internal(Person):
    
    def __init__(self, names, lastnames, ci, email, id_espe, type_espe, campus, career):
        """
            Internal Class
            Derived class that extends the Person class

            Parameters
            ------------------------------
            id: Identity institution card
            type: can be student, teacher
            campus: name of institution place, can be sto domingo, latacunga or matriz
            career: name of a related studies
            usernames: names of the users
            lastnames: lastsnames of the users
            ci: Identity card
            email: Person's email

        """    
        super().__init__(names, lastnames, ci, email)
        self.id = id_espe
        self.type = type_espe
        self.campus = campus
        self.career = career
    
    def greet_internal(self):
        """
            Function tostring of the internal class

            Parameters
            ---------------------------------------
            none:none

            Returns: none
            --------------------------------------
            Returns a string representation of the person.
        """
        print("Hola yo soy {}\n y estudio {}\n en la espe {}\n ".format(self.names, self.career, self.campus))