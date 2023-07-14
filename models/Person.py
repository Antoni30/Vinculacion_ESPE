class Person():
    def __init__(self,names,lastnames,ci, email):
        """
        Person Class

        Parameters
        ------------------------------
        usernames: names of the users
        lastnames: lastsnames of the users
        ci: Identity card
        email: Person's email

        """
        self.names=names
        self.lastnames=lastnames
        self.ci=ci
        self.email=email

    def toString(self):
        """
        Function tostring of the person class

        Parameters
        ---------------------------------------
        none:none

        Returns:
        --------------------------------------
        Returns a string representation of the person.
        """
        print("names: {}\nlastnames: {}\nci: {}\nemail: {}".format(self.names,self.lastnames,self.ci,self.email))

    
    def greet(self):
        """
        Function that allows you to greet the person

        Parameters
        ---------------------------------------
        none:none

        Return
        ---------------------------------------
        not return anything
        """

        print('Hello ', self.names)

    