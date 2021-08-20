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

Representation of a task in the system.

"""


class Task(object):

    TID = 0

    def __init__(self, name, priority, burst):
        self.tid = Task.TID
        self.name = name
        self.priority = priority
        self.burst = burst

        Task.TID += 1
