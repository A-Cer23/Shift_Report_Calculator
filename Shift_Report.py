from datetime import date, timedelta

class ShiftReport:

    #--- Constructor ---#
    def __init__(self, shiftDate:date, starTime:timedelta, endTime:timedelta):
        self.shiftDate:date = shiftDate
        self.startTime:timedelta = starTime
        self.endTime:timedelta = endTime
        self.totalHours:timedelta = self.endTime - self.startTime

    #--- GETTERS ---#
    def get_shiftDate(self) -> date:
        return self.shiftDate

    def get_startTime(self) -> timedelta:
        return self.startTime

    def get_endTime(self) -> timedelta:
        return self.endTime
    
    def get_totalHours(self) -> timedelta:
        return self.totalHours

    #--- SETTERS --- #
    def set_shiftDate(self, newSD:date):
        self.shiftDate = newSD

    def set_startTime(self, newST:timedelta):
        self.startTime = newST

    def set_endTime(self, newET:timedelta):
        self.endTime = newET
        
    def as_dict(self):
        return {"Date": str(self.shiftDate),
                "Start Time": str(self.startTime),
                "End Time": str(self.endTime)}