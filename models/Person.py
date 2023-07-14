class Person():
    def __init__(self,names,lastnames,idCard):
        """
        Person Class

        Parameters
        ------------------------------
        usernames: names of the users
        lastnames: lastsnames of the users

        """
        self.names=names
        self.lastnames=lastnames
        self.idCard=idCard

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
        print("names: {}\nlastnames: {}\nidCard: {}".format(self.names,self.lastnames,self.idCard))

    
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

    