"""
CA216 - Operating Systems

STATEMENT OF NON-PLAGIARISM


I hereby declare that all information in this assignment has been obtained
and presented in accordance with academic rules and ethical conduct
and the work I am submitting in this document, except where I have indicated, is my own work.


Student Number: 19451972
Student Name: George Eskander

"""

from fcfs import schedule_fcfs
from sjf import schedule_sjf
from priority import schedule_priority
from rr import schedule_rr


# put our scheduler functions in a dictionary
SCHEDULERS = {
    "fcfs": schedule_fcfs,
    "sjf": schedule_sjf,
    "priority": schedule_priority,
    "rr": schedule_rr,
}

MIN_PRIORITY = 1
MAX_PRIORITY = 10


# invoke the scheduler
def schedule(scheduler_name, tasks):
    SCHEDULERS[scheduler_name](tasks)  # begin scheduling
