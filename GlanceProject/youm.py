
# youm.py
# Youm is a class that represents a day on the calendar.
# Youm is Arabic/Hebrew for day. Used instead of "day" to avoid confusion.

from task import Task
from event import Event
from datetime import datetime, date, time


class Youm:

    def __init__(self, date_in):
        """ Class Constructor """
        self.id = str(date_in)            # string representation of date serves as unique id.
        self.date_d = date_in.day         # Day Value
        self.date_m = date_in.month       # Month Value
        self.date_y = date_in.year        # Year Value
        self.events = {}                  # Default list of events (Hash Table)
        self.tasks = {}                   # Default list of tasks (Hash Table)

    def set_date(self, date_in):
        """ Sets the date values of the youm (if it needs to be changed), updates the id as well.
        :param date_in: datetime date object
        :return: None
        """
        self.date_d = date_in.day
        self.date_m = date_in.month
        self.date_y = date_in.y

        # Since new date is given, the ID must change.
        self.id = str(date_in)

    # Events:

    def add_event(self, event_in):
        """ Adds an event to the events Hash
        :param event_in: event object to be added.
        :return: None
        """

        # Setup unique key as Event's id
        key = event_in.id

        # Add event object to Hash
        self.events[key] = event_in

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

