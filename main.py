from datetime import date,timedelta
from Shift_Report import ShiftReport 
import Save_Load as SL

class CLI:

    # constructor that holds a state variable and a list of shiftReports
    def __init__(self):

        self.state = True
        self.shiftReports = SL.load()

    # while self.state is true - runs the main menu -- main function --
    def main_menu(self):

        while self.state:
            print("\n\n----- MAIN MENU -----\n")
            try:
                choice:int = int(input("1) Add a new Shift Report\n" + 
                                    "2) Show All Shiftreports\n" + 
                                    "3) Update a Shift Report\n" + 
                                    "4) Delete a Shift Report\n" +
                                    "0) Enter 0 (zero) to Quit\n\n" +
                                    "Enter an option -> "))
            except ValueError:
                print("\n <-- Please indicate a number -->\n")
                
            else:
                self.check_choice(choice)
        
    # checks to see which choice was chosen and calls the approriate function to carry the task
    def check_choice(self, choice:int):
        if choice == 0:
            self.state = False
        elif choice == 1:
            self.add_shiftReport()
        elif choice == 2:
            self.print_all_shiftReports()
        elif choice == 3:
            self.update_shiftReport()
        elif choice == 4:
            self.delete_shiftReport()
        else:
            print("\n<-- Please enter a valid option -->\n")

    # Gets the date info and returns a date object
    def get_date(self):

        while True:
            try:
                month, day, year = [int(num) for num in input(f"\nEnter the shift date (MM DD YYYY) -> ").split()]

                if month > 12 or day > 31:
                    raise ValueError

                date_to_return = date(year, month, day)

            except ValueError:
                print("\n<-- Place date as MM DD YYYY with a space in-between - ex. 01 25 2022 -->")
            else:
                return date_to_return
    
    # Gets the time info and returns a timedelta object - startOrEnd is either "start" or "end" time
    def get_times(self, startOrEnd: str):
        
        while True:
            try:
                hour, minute, second = [int(num) for num in input(f"\nEnter the {startOrEnd} time (24h: HH MM SS) -> ").split()]

                if hour > 24 or minute > 59 or second > 59:
                    raise ValueError
                time_to_return = timedelta(hours=hour, minutes=minute, seconds=second)

            except ValueError:
                print("\n<-- Place time as HH MM SS with a space inbetween - ex. 22 45 00 -->")
            else:
                return time_to_return

    # gathers all shift report information required to make a shift report object
    def get_shiftReport_info(self):

        shiftDate = self.get_date()
        startTime = self.get_times("start")
        endTime = self.get_times("end")
        return shiftDate, startTime, endTime

    # creates a shift report object and appends it to the shiftreports list
    def add_shiftReport(self):
        shiftDate, startTime, endTime = self.get_shiftReport_info()
        sr = ShiftReport(shiftDate, startTime, endTime)
        self.shiftReports.append(sr)
        self.sort_and_save()
        
    def sort_and_save(self):
        self.shiftReports.sort(key=lambda e: e.get_shiftDate(), reverse=True)
        SL.save(self.shiftReports)

    # gets the shift report id to be either deleted or updated based on 'updateOrDel' to carry out the logic
    def get_shiftReport_id(self, updateOrDel: str):
        while True:
            try:
                srID = int(input(f"\nEnter the Shift Report ID you want to {updateOrDel} -> "))
                shiftRep: ShiftReport = self.shiftReports[srID]
            except ValueError:
                print("\n<-- Place a valid number -->")
            except IndexError:
                print("\n<-- Place an ID that is in the list of Shift Reports -->")
            else:
                return srID

    def is_correct_shiftReport(self, srID:int):
        shiftRep: ShiftReport = self.shiftReports[srID]
        print(f"\nID: {srID}\
                \nDate: {shiftRep.get_shiftDate()}\
                \nStart Time: {shiftRep.get_startTime()}\
                \nEnd Time: {shiftRep.get_endTime()}\
                \nTotal Hours: {shiftRep.get_totalHours()}")
        choice = input("\nIs this the correct Shift Report? (y/n) -> ")
        if choice == "y":
            return True
        else:
            return False

    def update_shiftReport(self):
        srID = None
        while (True):
            srID = self.get_shiftReport_id("update")
            if (self.is_correct_shiftReport(srID)):
                break
        shiftRep_toUpdate: ShiftReport = self.shiftReports[srID]
        newDate, newStartTime, newEndTime = self.get_shiftReport_info()
        shiftRep_toUpdate.set_shiftDate(newDate)
        shiftRep_toUpdate.set_startTime(newStartTime)
        shiftRep_toUpdate.set_endTime(newEndTime)
        self.sort_and_save()
        print("\n<-- Updated -->\n")

    def delete_shiftReport(self):
        srID = None
        while(True):
            srID = self.get_shiftReport_id("delete")
            if (self.is_correct_shiftReport(srID)):
                break
        self.shiftReports.remove(self.shiftReports[srID])
        print("\n<-- Deleted -->\n")
    
    

    # prints all shift reports
    def print_all_shiftReports(self):

        print("\n" + "-" * 80)
        print("   ID   |   Shift Date   |   Start Time   |   End Time   |   Total Hours   ")
        print("-" * 80 + "\n")

        for x, sr in enumerate(self.shiftReports):
            print("   " + str(x) +"   |   " + str(sr.get_shiftDate()) + "   |    " + str(sr.get_startTime()) + 
            "     |   " + str(sr.get_endTime()) + 
            "   |    " + str(sr.get_totalHours()))

        print("\n" + "-" * 80 + "\n\n")

CLI().main_menu()
