class Person():
    def __init__(self,names,lastnames,idCard):
        self.names=names
        self.lastnames=lastnames
        self.idCard=idCard

    def toString(self):
        print("names: {}\nlastnames: {}\nidCard: {}".format(self.names,self.lastnames,self.idCard))

    def saludar(self):
        """
        Function that allows you to greet the person

        Parameters
        ---------------------------------------
        none:none

        Return
        ---------------------------------------
        not return anything
        """
        print('Hola ', self.names)

    