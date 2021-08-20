"""
CA216 - Operating Systems

STATEMENT OF NON-PLAGIARISM


I hereby declare that all information in this assignment has been obtained
and presented in accordance with academic rules and ethical conduct
and the work I am submitting in this document, except where I have indicated, is my own work.


Student Number: 19451972
Student Name: George Eskander

"""

"""

"Virtual" CPU that also maintains track of system time.

"""

from task import Task

QUANTUM = 10


# run this task for the specified time slice
def run(task, time_slice):
    print(f"Running task = [{task.name}] [{task.priority}] [{task.burst}] for {time_slice} units.")


# simply gets the average time of anything for example the average waiting time after processing tasks
def average_time(total_time, num_of_tasks):
    return total_time / num_of_tasks


def print_avg_time(avg_time, time_title):
    print(f"Avg. {time_title}: {avg_time} MS")
