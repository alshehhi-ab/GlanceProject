
# iocontrol.py

# Controls input statements

from event import Event
from task import Task
from sana import Sana
from datacontrol import DataControl
from datetime import datetime, date, time


class IOControl:

    def __init__(self):
        self.years = []       # Default years stored on device.

    def next_date(self, date_in):
        """ Returns next date from current date
        :param date_in: current date
        :return: date object, date after current date
        """

        # Get current ordinal
        curr_ord = date.toordinal(date_in)
        next_ord = curr_ord+1

        # Generate next day as date object
        next_day = date.fromordinal(next_ord)

        return next_day

    def prev_date(self, date_in):
        """ Returns previous date from current date
        :param date_in: current date
        :return date object, date before current date
        """

        # Get current ordinal
        curr_ord = date.toordinal(date_in)
        prev_ord = curr_ord-1

        # Generate previous day as date object
        prev_day = date.fromordinal(prev_ord)

        return prev_day

    def get_youm(self, date_in, sana_in):
        """ Gets a youm (day) object from a given sana (year) object
        :param date_in: input date, date object
        :param sana_in: input sana object
        :return: youm object (representation of date)
        """

        key = str(date_in)

        return sana_in.youms[key]

    def default_menu(self, data_dict):
        """ User Interface for interacting with Glance
        :param data_dict: dictionary relating year numbers to sana objects
        """
        curr_date = date.today()
        curr_year = curr_date.year

        add_menu_str = "\n[Add Menu] \n(E) Add Event \n(T) Add Task \n(Q) Return to previous menu."
        rem_menu_str = "\n[Remove Menu] \n(E) Remove Event \n(T) Remove Task \n(Q) Return to previous menu."

        while True:

            print("-" * 50)
            print("[Menu Options]")
            print("(X) Today")
            print("(<) Yesterday")
            print("(>) Tomorrow")
            print("(?) Show Other Day")
            print("(A) Add Event/Task")
            print("(R) Remove Event/Task")
            print("(T) Terminate Program")

            opt_in = str(input("Please select an option: "))

            # Show today
            if opt_in == "X":
                sana_key = data_dict[curr_year]
                youm_to_show = self.get_youm(curr_date, sana_key)

                while True:

                    print(" {0:^101} ".format("[[Today]]"))
                    print()
                    print("[Date]")
                    print(curr_date.strftime("%A %d, %B %Y"))
                    print()
                    print(youm_to_show)
                    print()

                    in_opt = str(input("Press Q to exit day view at any time. \n"))
                    if in_opt == "Q":
                        break

            # Show Yesterday
            if opt_in == "<":
                sana_key = data_dict[curr_year]
                yesterdate = self.prev_date(curr_date)
                youm_to_show = self.get_youm(yesterdate, sana_key)

                while True:

                    print(" {0:^101} ".format("[[Yesterday]]"))
                    print()
                    print("[Date]")
                    print(yesterdate.strftime("%A %d, %B %Y"))
                    print()
                    print(youm_to_show)
                    print()

                    in_opt = str(input("Press Q to exit day view at any time. \n")).upper()
                    if in_opt == "Q":
                        break

            # Show Next Day
            if opt_in == ">":
                sana_key = data_dict[curr_year]
                nextdate = self.next_date(curr_date)
                youm_to_show = self.get_youm(nextdate, sana_key)

                while True:

                    print(" {0:^101} ".format("[[Tomorrow]]"))
                    print()
                    print("[Date]")
                    print(nextdate.strftime("%A %d, %B %Y"))
                    print()
                    print(youm_to_show)
                    print()

                    in_opt = str(input("Press Q to exit day view at any time. \n")).upper()
                    if in_opt == "Q":
                        break

            # Show Other Day
            if opt_in == "?":
                showdate = date.fromisoformat(str(input("Please enter date in following format yyyy-mm-dd: ")))
                sana_key = data_dict[showdate.year]
                youm_to_show = self.get_youm(showdate, sana_key)

                while True:

                    print(" {0:^101} ".format("[[Day]]"))
                    print()
                    print("[Date]")
                    print(showdate.strftime("%A %d, %B %Y"))
                    print()
                    print(youm_to_show)
                    print()

                    in_opt = str(input("Press Q to exit day view at any time. \n")).upper()

                    if in_opt == "Q":
                        break

            # Add Event/ Task
            if opt_in == "A":

                print(add_menu_str)
                selector = str(input("Please select an option: "))

                if selector == "Q":
                    break

                if selector == "E":

                    event_to_add = Event()

                    event_date_start = date.fromisoformat(str(input("Please enter start date of event yyyy-mm-dd: ")))
                    event_date_end = date.fromisoformat(str(input("Please enter end date of event yyyy-mm-dd: ")))
                    event_time_start = time(int(input("Please enter start hour (HH): ")),
                                            int(input("Please enter start minute (MM): ")))
                    event_time_end = time(int(input("Please enter end hour (HH): ")),
                                          int(input("Please enter end minute (MM): ")))
                    event_name = str(input("Please enter event name: "))
                    event_loc = str(input("Please enter event location: "))
                    event_desc = str(input("Please enter event notes: "))

                    event_to_add.set_date_start(event_date_start)
                    event_to_add.set_date_finish(event_date_end)
                    event_to_add.set_time_start(event_time_start)
                    event_to_add.set_time_finish(event_time_end)
                    event_to_add.set_name(event_name)
                    event_to_add.set_location(event_loc)
                    event_to_add.set_description(event_desc)

                    # Add event to day
                    sana_key = data_dict[event_date_start.year]
                    day_to_modify = self.get_youm(event_date_start, sana_key)
                    day_to_modify.add_event(event_to_add)

                    print("Event Added")

                if selector == "T":

                    task_to_add = Task()

                    task_date_end = date.fromisoformat(str(input("Please enter end date of task yyyy-mm-dd: ")))
                    task_time_end = time(int(input("Please enter end hour (HH): ")),
                                         int(input("Please enter end minute (MM): ")))
                    task_name = str(input("Please enter task name: "))
                    task_priority = str(input("Please enter task priority \"High\" \"Medium\" \"Low\": "))
                    task_desc = str(input("Please enter task notes: "))

                    task_to_add.set_date(task_date_end)
                    task_to_add.set_time(task_time_end)
                    task_to_add.set_name(task_name)
                    task_to_add.set_priority(task_priority)
                    task_to_add.set_description(task_desc)

                    # Add task to day
                    sana_key = data_dict[task_date_end.year]
                    day_to_modify = self.get_youm(task_date_end, sana_key)
                    day_to_modify.add_task(task_to_add)

                    print("Task Added")

            # Remove Event/Task
            if opt_in == "R":

                print(rem_menu_str)
                selector = str(input("Please select an option: "))

                if selector == "Q":
                    break

                # Delete an Event
                if selector == "E":
                    date_event = date.fromisoformat(str(input("Please enter date of event yyyy-mm-dd: ")))
                    sana_key = data_dict[date_event.year]
                    day_events = self.get_youm(date_event, sana_key).events

                    for k, v in day_events.items():
                        print(k, str(v))

                    delete_key = int(input("Please enter an event ID you would like to delete: "))

                    del self.get_youm(date_event, sana_key).events[delete_key]

                # Delete a Task
                if selector == "T":
                    date_task = date.fromisoformat(str(input("Please enter date of task yyyy-mm-dd: ")))
                    sana_key = data_dict[date_task.year]
                    day_tasks = self.get_youm(date_task, sana_key).tasks

                    for k, v in day_tasks.items():
                        print(k, str(v))

                    delete_key = int(input("Please enter an task ID you would like to delete: "))

                    del self.get_youm(date_task, sana_key).tasks[delete_key]

            # Quit
            if opt_in == "T":
                break

            # Any other invalid input
            else:
                print()
