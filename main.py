from datetime import date,timedelta
from Shift_Report import ShiftReport 

class CLI:

    # constructor that holds a state variable and a list of shiftReports
    def __init__(self):
        self.state = True
        self.shiftReports = []
        
        # Test Data begins
        sr1 = ShiftReport(
                        date(year=2022, month=4, day=23), 
                        timedelta(hours=9, minutes=00, seconds=00),
                        date(year=2022, month=4, day=23),
                        timedelta(hours=17, minutes=00, seconds=00))
        self.shiftReports.append(sr1)
        ## Test Data ends

    # while self.state is true - runs the main menu -- main function --
    def main_menu(self):

        while self.state:
            print("----- MAIN MENU -----\n")
            try:
                choice:int = int(input("1) Add a new Shift Report\n" + 
                                    "2) Show All Shiftreports\n" +
                                    "0) Enter 0 (zero) to Quit\n\n" +
                                    "<Enter an option>\n"))
            except ValueError:
                print("\n <-- Please indicate a number -->\n")
                
            else:
                self.check_choice(choice)
        
    # checks to see which choice was chosen and calls the approriate function to carry the task
    def check_choice(self, choice:int):
        if choice == 0:
            self.state = False
        elif choice == 1:
            self.get_shiftReport_info()
        elif choice == 2:
            self.print_all_shiftReports()
        else:
            print("\n<-- Please enter a valid option -->\n")

    # Gets the date info and returns a date object - startOrEnd is either "start" or "end" date
    def get_date(self, startOrEnd:str):

        while True:
            try:
                month, day, year = [int(num) for num in input(f"\nEnter the {startOrEnd} date (MM DD YYYY)\n").split()]
                date_to_return = date(year, month, day)
                if month > 12 or day > 31:
                    raise ValueError
            except ValueError:
                print("\n<-- Please enter date as MM DD YYYY with a space inbetween - ex. 01 25 2022 -->\n")
            except TypeError:
                print("\n<-- Please use numbers -->\n")
            else:
                return date_to_return
    
    # Gets the time info and returns a timedelta object - startOrEnd is either "start" or "end" time
    def get_times(self, startOrEnd: str):
        
        while True:
            try:
                hour, minute, second = [int(num) for num in input(f"\nEnter the {startOrEnd} time (24h: HH MM SS)\n").split()]
                if hour > 24 or minute > 59 or second > 59:
                    raise ValueError
                time_to_return = timedelta(hours=hour, minutes=minute, seconds=second)
            except ValueError:
                print("\n<-- Please enter time as HH MM SS with a space inbetween - ex. 22 45 00 -->\n")
            except TypeError:
                print("\n<-- Please use numbers -->\n")
            else:
                return time_to_return

    # gathers all shift report information required to make a shift report object
    def get_shiftReport_info(self):

        startDate = self.get_date("start")
        endDate = self.get_date("end")
        startTime = self.get_times("start")
        endTime = self.get_times("end")
        self.add_shiftReport(startDate, endDate, startTime, endTime)

    # creates a shift report object and appends it to the shiftreports list
    def add_shiftReport(self, startDate:date, endDate:date, startTime:timedelta, endTime:timedelta):

        sr = ShiftReport(startDate, startTime, endDate, endTime)
        self.shiftReports.append(sr)
    
    def print_all_shiftReports(self):
        print("\n" + "-" * 80)
        print("   Start Date   |   End Date   |   Start Time   |   End Time   |   Total Hours")
        print("-" * 80 + "\n")
        for sr in self.shiftReports:
            print("   " + str(sr.get_startDate()) + "   |  "  + str(sr.get_endDate()) + 
            "  |    " + str(sr.get_startTime()) + "     |   " + str(sr.get_endTime()) + 
            "   |    " + str(sr.get_totalHours()))
        print("\n" + "-" * 80 + "\n\n")

CLI().main_menu()
