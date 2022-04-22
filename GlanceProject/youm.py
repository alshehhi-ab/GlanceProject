
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
        """ Removes an event from the events Hash
        :param event_in: event to be removed
        :return: None
        """

        # since key is defined as event id
        key = event_in.id

        # deleting the event
        del self.events[key]

    def get_event(self, event_id):
        """ Retrieves an event based on the ID supplied
        :param event_id: ID of event to be found
        :return: event object
        """
        
        # Return the event if found    
        return self.events[event_id]
    
    def show_events(self):
        """ Creates a sorted list of events by start-time
        :return: list of events
        """

        # Create a list of events from events dictionary
        lst_events = [x for x in self.events.values()]

        # Sort list
        lst_events.sort(key=lambda y: y.time_start)     # Python's built-in sort function is fastest implementation.

        return lst_events

    def show_events_str(self):
        """ Generates a string of the events in sorted format.
        :return: string of events
        """

        # Step 1: Get list of events
        lst_events_obj = self.show_events()

        # Step 2: Generate String of list of events
        str_out = "[#]" + "-"*50 + "[#]" + "\n" \
                + " {0:^51} ".format("[EVENTS]") + "\n" + "\n"

        for x in lst_events_obj:
            str_out += str(x) + "\n"

        return str_out

    # Tasks

    def add_task(self, task_in):
        """ Adds task to tasks hash
        :param task_in: input task to be added
        :return: None
        """

        # Setup unique key as tasks id
        key = task_in.id

        # Add event object to Hash
        self.tasks[key] = task_in

    def remove_task(self, task_in):
        """ Removes an task from the tasks Hash
        :param task_in: task to be removed
        :return: None
        """

        # since key is defined as task id
        key = task_in.id

        # deleting the task
        del self.tasks[key]

    def get_task(self, task_id):
        """ Retrieves an task based on the ID supplied
        :param task_id: ID of task to be found
        :return: task object
        """

        # Return the task if found    
        return self.tasks[task_id]

    def show_tasks(self):
        """ Creates a sorted list of tasks by priority
        :return: list of tasks
        """
        
        priority_order = {"High": 0, "Medium": 1, "Low": 2, "": 3}  # Order of priorities, used for lambda in sorting.
        
        # Create a list of tasks from tasks dictionary
        lst_tasks = [x for x in self.tasks.values()]

        # Sort tasks by priority
        lst_tasks.sort(key=lambda y: priority_order[y.priority])

        return lst_tasks

    # Other functions

    def __str__(self):
        """ String overload for Youm
        :return: string representation of Youm
        """

        # Generate strings for tasks and events

        # EVENTS

        # Step 1: Get list of events
        lst_events_obj = self.show_events()

        # Step 2: Generate String of list of events
        str_events = "#" + "-"*75 + "#" + "\n" \
                + " {0:^76} ".format("[Events]") + "\n" + "\n"

        for x in lst_events_obj:
            str_events += str(x) + "\n"

        # TASKS

        # Step 1: Get list of tasks
        lst_tasks_obj = self.show_tasks()

        # Step 2: Generate String of list of tasks
        str_tasks = "#" + "-"*75 + "#" + "\n" \
                + " {0:^76} ".format("[Tasks]") + "\n" + "\n"

        for x in lst_tasks_obj:
            str_tasks += str(x) + "\n"

        str_out = "#" + "-" * 100 + "#" + "\n" \
                  + " {0:^101} ".format("[[Day]]") + "\n" + "\n" \
                  + "[Day]" + "\n" + date.fromisoformat(self.id).strftime("%A %d, %B %Y") + "\n" + "\n" \
                  + str_events+ "\n" + "\n" \
                  + str_tasks + "\n" + "\n" \
                  + "#" + "-"*100 + "#"

        return str_out
