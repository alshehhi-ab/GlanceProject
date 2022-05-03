from task import Task
from event import Event
from youm import Youm
from sana import Sana
from datacontrol import DataControl
from iocontrol import IOControl
from admincontrol import AdminControl

from datetime import datetime, date, time


debug = False


# -- STARTUP --

# Set up Data Controller and IO Controller
controller = DataControl()
io = IOControl()
admin = AdminControl(io, controller)

# Read Calendar files (Generate Dictionary of available files)
years_avail = {k: controller.read_sdf(k) for k in controller.lst_years}
io.years = controller.lst_years

# Start Glance System
print("-- STARTING GLANCE --")
selector = str(input("Welcome to Glance, press any key to continue: "))

# ADMIN Control
if selector == "ADMIN":
    admin.admin_menu()


# -- MAIN INTERFACE --


# Interface
io.default_menu(years_avail)

# -- CLOSING UP

# Write Calendar files
for sana_dat in years_avail.values():
    controller.write_sdf(sana_dat)

quit()

# -- DEBUG --

# Test output for Task

if debug:
    print("TASK DEBUG: ")
    task_a = Task()
    task_a.set_name("Pay Water Bill")
    task_a.set_description("Make sure to pay the water bill.")
    task_a.set_date(date(2022, 4, 20))
    task_a.set_time(time(20, 00))
    task_a.set_priority("High")
    print(task_a)

    print()

    task_b = Task()
    task_b.set_name("Tidy up attic")
    task_b.set_description("The attic needs to be cleaned.")
    task_b.set_date(date(2022, 4, 20))
    task_b.set_time(time(12, 00))
    task_b.set_priority("Low")
    task_b.mark_complete()
    print(task_b)

    task_c = Task()
    task_c.set_name("Replace light-bulb in closet")
    task_c.set_description("It's dark. Get 12W bulb.")
    task_c.set_date(date(2022, 4, 20))
    task_c.set_time(time(8, 00))
    task_c.set_priority("Medium")
    print(task_c)

# Test output for Event

if debug:
    print("EVENT DEBUG: ")
    event_a = Event()
    event_a.set_name("Interview With ABC Inc.")
    event_a.set_location("Home")
    event_a.set_time_start(time(14, 30))
    event_a.set_date_start(date(2022, 4, 20))
    event_a.set_time_finish(time(15, 00))
    event_a.set_date_finish(date(2022, 4, 20))
    event_a.set_description("Job interview with ABC. Make sure to dress accordingly.")
    print(event_a)

    event_b = Event()
    event_b.set_name("Smalltown vs Bigville Soccer match.")
    event_b.set_location("Great Sport Stadium")
    event_b.set_time_start(time(17, 00))
    event_b.set_date_start(date(2022, 4, 20))
    event_b.set_time_finish(time(19, 45))
    event_b.set_date_finish(date(2022, 4, 20))
    event_b.set_description("Be there 16:45.")

    print(event_a)
    print(event_b)



# Test output for Youm

if debug:
    print("YOUM DEBUG: ")
    youm_a = Youm(date(2022, 4, 20))

    youm_a.add_task(task_a)
    youm_a.add_task(task_b)
    youm_a.add_task(task_c)

    youm_a.add_event(event_a)
    youm_a.add_event(event_b)

    print(youm_a)
