class Visit:
    def __init__(self, place, entryTime, exitTime, visitDuration):
        """
        Person Visit

        Parameters
        ------------------------------
        place: The visited place.
        entry_time: The entry time of the visit.
        exit_time: The exit time of the visit.
        visit_duration: The total duration of the visit in minutes.

        """
        self.place = place
        self.entryTime = entryTime
        self.exitTime = exitTime
        self.visitDuration = visitDuration

    def tostring(self):
        """
        Function tostring of the person visit

        Parameters
        ---------------------------------------
        none:none

        Returns:
        --------------------------------------
        Returns a string representation of the visit.
        """
        return f"Place: {self.place}\nEntry Time: {self.entryTime}\nExit Time: {self.exitTime}\nVisit Duration: {self.visitDuration} minutes"
