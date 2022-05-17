from datetime import date, timedelta

class ShiftReport:

    #--- Constructor ---#
    def __init__(self, startDate:date, startTime:timedelta, endDate:date, endTime:timedelta):
        self.startDate = startDate
        self.startTime = startTime
        self.endDate = endDate
        self.endTime = endTime
        self.totalHours = self.endTime - self.startTime

    #--- GETTERS ---#
    def get_startDate(self):
        return self.startDate

    def get_startTime(self):
        return self.startTime

    def get_endDate(self):
        return self.endDate

    def get_endTime(self):
        return self.endTime
    
    def get_totalHours(self):
        return self.totalHours

    #--- SETTERS --- #
    def set_startDate(self, newSD:date):
        self.startDate = newSD

    def set_startTime(self, newST:timedelta):
        self.startTime = newST

    def set_endDate(self, newED:date):
        self.endDate = newED

    def set_endTime(self, newET:timedelta):
        self.endTime = newET
        