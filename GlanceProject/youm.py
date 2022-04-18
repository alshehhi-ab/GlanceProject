
# youm.py
# Youm is a class that represents a day on the calendar.
# Youm is Arabic/Hebrew for day. Used instead of "day" to avoid confusion.

from task import Task
from event import Event
from datetime import datetime, date, time

class Youm:

    def __init__(self, date_in):
        self.date_d = date_in.day         # Day Value
        self.date_m = date_in.month       # Month Value
        self.date_y = date_in.year        # Year Value
        self.lst_events = []              # Default list of events
        self.lst_tasks = []               # Default list of tasks

    def set_date(self, date_in):
        """ Sets the date values of the youm (if it needs to be changed)
        :param date_in: datetime date object
        :return: None
        """
        self.date_d = date_in.day
        self.date_m = date_in.month
        self.date_y = date_in.y

    # Events:

    def add_event(self, event_in):
        pass

    def remove_event(self, event_in):
        pass

    def get_event(self, event_id):
        pass

    def show_events(self):
        pass

    # Tasks

    def add_task(self, task_in):
        pass

    def remove_task(self, task_in):
        pass

    def get_task(self, task_id):
        pass

    def show_tasks(self):
        pass

    # Other functions

    def __str__(self):
        """ String overload for Youm
        :return: string representation of Youm
        """
        pass

