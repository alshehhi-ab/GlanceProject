
# task.py
# Class Definition of a Task object.
# Tasks are items to be completed in a day. They serve as TO-DOs, or Reminders.

import calendar
from datetime import datetime, date, time


class Task:
    """ Tasks are items to be completed in a day. """
    id_counter = 0  # unique ID attribute

    def __init__(self):
        """ Class constructor """
        self.id = Task.id_counter
        self.name = ""
        self.description = ""
        self.date_finish = ""
        self.time_finish = ""
        self.priority = "Low"       # Default priority is Low
        self.status = False         # Task is incomplete by default
        Task.id_counter += 1

    def set_name(self, name_in):
        """ Sets name of task
        :param name_in: name input for task
        :return: None
        """
        self.name = name_in

    def set_description(self, desc_in):
        """ Sets description of task
        :param desc_in: description input for task
        :return: None
        """
        self.description = desc_in

    def set_date(self, date_finish_in):
        """ Sets finishing date of task
        :param date_finish_in: date object indicating finishing date
        :return: None
        """
        self.date_finish = date_finish_in

    def set_time(self, time_finish_in):
        """ Sets finishing time of task
        :param time_finish_in: time object indicating finishing time
        :return: None
        """
        self.time_finish = time_finish_in

    def set_priority(self, priority_in):
        """ Sets priority level of task
        :param priority_in: Priority level of task, must be "Low", "Medium", "High"
        :return: None
        """

        priorities = ["Low", "Medium", "High"]

        if priority_in not in priorities:
            raise ValueError("Invalid Priority Level")

        self.priority = priority_in

    def mark_complete(self):
        """ Sets status to True
        :return: None
        """
        self.status = True

    def get_status(self):
        """ Gets Status in string form
        :return: "Complete" if true, "Incomplete" if false
        """
        if self.status:
            return "Complete"
        else:
            return "Incomplete"

    def __str__(self):
        """ String overload for Task object
        :return: string representation
        """

        str_out = "#" + "-"*50 + "#" + "\n" \
                  + " {0:^51} ".format("[[Task]]") + "\n" + "\n" \
                  + "[Name]" + "\n" + self.name + "\n" + "\n" \
                  + "[Date]" + "\n" + self.date_finish + "\n" + "\n" \
                  + "[Time]" + "\n" + self.time_finish + "\n" + "\n" \
                  + "[Priority]" + "\n" + self.priority + "\n" + "\n" \
                  + "[Status]" + "\n" + self.get_status() + "\n" + "\n" \
                  + "[Description]" + "\n" + self.description + "\n" \
                  + "#" + "-"*50 + "#"

        return str_out

