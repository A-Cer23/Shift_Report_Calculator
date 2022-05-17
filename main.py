from datetime import date,timedelta

class CLI:

    # constructor that holds a state variable and a list of shiftReports
    def __init__(self):
        self.state = True
        self.shiftReports = []

    # while self.state is true - runs the main menu -- main function --
    def main_menu(self):

        while self.state:
            print("----- MAIN MENU -----\n")
            try:
                choice:int = int(input("1) Add a new Shift Report\n" +
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
        else:
            print("\n<-- Please enter a valid option -->\n")


    def get_date(self, dateType:str):

        while True:
            try:
                month, day, year = [int(num) for num in input(f"\nEnter the {dateType} date (MM DD YYYY)\n").split()]
                date_to_return = date(year, month, day)
            except ValueError:
                print("\n<-- Please enter date as MM DD YYYY with a space inbetween - ex. 01 25 2022 -->\n")
            except TypeError:
                print("\n<-- Please use numbers -->\n")
            else:
                return date_to_return
                break

    def get_shiftReport_info(self):

        startDate = self.get_date("start")
        endDate = self.get_date("end")


    def add_shiftReport(self):
        pass


CLI().main_menu()
