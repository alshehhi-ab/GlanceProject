
# event.py

# Class Definition of an Event object.
# Events are items that occur during the day.

import calendar
from datetime import datetime, date, time

class Event:
    id_counter = 0

    def __init__(self):
        """ Class constructor """
        self.id = Event.id_counter
        self.name = ""
        self.location = ""
        self.description = ""
        self.date_start = ""
        self.time_start = ""
        self.date_finish = ""
        self.time_finish = ""
        Event.id_counter += 1


    def set_name(self, name_in):
        """ Sets name of event
        :param name_in: name input for event
        :return: None
        """
        self.name = name_in

    def set_description(self, desc_in):
        """ Sets description of event
        :param desc_in: description input for event
        :return: None
        """
        self.description = desc_in

    def set_date_start(self, date_start_in):
        """ Sets starting date of event
        :param date_start_in: date object indicating starting date
        :return: None
        """
        self.date_start = date_start_in

    def set_time_start(self, time_start_in):
        """ Sets starting time of event
        :param time_start_in: time object indicating starting time
        :return: None
        """
        self.time_start = time_start_in
        
    def set_date_finish(self, date_finish_in):
        """ Sets finishing date of event
        :param date_finish_in: date object indicating finishing date
        :return: None
        """
        self.date_finish = date_finish_in

    def set_tim_finish(self, time_finish_in):
        """ Sets finishing time of event
        :param time_finish_in: time object indicating finishing time
        :return: None
        """
        self.time_finish = time_finish_in
        
    def __str__(self):
        """ String overload for Event object
        :return: string representation of Event object
        """
        pass
    