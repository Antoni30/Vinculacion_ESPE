from models.Person import Person 

class External(Person):
    def __init__(self, names, lastnames, ci, email, place, entryTime, exitTime, visitDuration):
        """
        Person Visit

        Parameters
        ------------------------------
        place: The visited place.
        entry_time: The entry time of the visit.
        exit_time: The exit time of the visit.
        visit_duration: The total duration of the visit in minutes.

        """
        super().__init__(names, lastnames, ci, email)
        self.place = place
        self.entryTime = entryTime
        self.exitTime = exitTime
        self.visitDuration = visitDuration

    def gree_external(self):
        """
        Function tostring of the person visit

        Parameters
        ---------------------------------------
        none:none

        Returns:
        --------------------------------------
        Returns a string representation of the visit.
        """
        print("place: {}\nentryTime: {}\nexitTime: {}\nvisitDuraion: {}".format(self.place,self.entryTime,self.exitTime,self.visitDuration))
        
