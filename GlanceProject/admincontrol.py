from task import Task
from event import Event
from youm import Youm
from sana import Sana
from datacontrol import DataControl
from iocontrol import IOControl

from datetime import datetime, date, time
import os

class AdminControl():

    def __init__(self, IOControl, DataControl):
        self.DataControl = DataControl
        self.IOControl = IOControl

    def view_sanas(self):
        for x in range(len(self.DataControl.lst_years)):
            print(str(self.DataControl.lst_years[x]) + " : " + self.DataControl.lst_sanas[x])

    def add_sana(self, year_create):
        self.DataControl.write_sdf(Sana(year_create))
        self.DataControl.lst_sanas.append(str(year_create) + ".dat")
        self.DataControl.lst_years.append(year_create)

    def rem_sana(self, year_remove):
        self.DataControl.lst_years.remove(year_remove)
        self.DataControl.lst_sanas.remove(str(year_remove) + ".dat")
        remove_path = os.path.join(self.DataControl.sana_dir, str(year_remove) + ".dat")
        os.remove(remove_path)

    def clear_sana(self, year_clear):
        self.rem_sana(year_clear)
        self.add_sana(year_clear)

    def admin_menu(self):
        print("\n WARNING: ENTERING ADMIN MODE. MAKE SURE YOU KNOW WHAT YOU ARE DOING.")
        print()
        admin_menu_str = "\x1b[1;31m\n[ADMIN MENU] \n<1> VIEW YEARS " \
                         "\n<2> ADD SANA \n<3> REMOVE SANA\n<4> CLEAR SANA\n<Q> QUIT ADMIN MENU"

        while True:
            print(admin_menu_str)
            selector = str(input("Please select an option: "))

            # View Years
            if selector == "1":
                self.view_sanas()

            # Add Sana
            if selector == "2":
                year_create = int(input("Please enter a year to create YYYY: "))
                self.add_sana(year_create)

            # Remove Sana
            if selector == "3":
                year_remove = int(input("Please enter a year to remove YYYY: "))
                self.rem_sana(year_remove)

            # Clear Sana
            if selector == "4":
                year_clear = int(input("Please enter a year to clear YYYY: "))
                self.clear_sana(year_clear)

            # Quit

            if selector == "Q":
                print("\x1b[0;0m")
                break

            # Invalid selection
            else:
                pass

