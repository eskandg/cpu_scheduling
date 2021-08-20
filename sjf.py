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

Shortest-job-first scheduling algorithm

"""

import sys
import driver

from fcfs import schedule_fcfs

if __name__ == "__main__":
    driver.main(sys.argv)


# Reference: ideas for SJF scheduling were taken from this book https://www.os-book.com/OS8/os8c/index.html
def schedule_sjf(tasks):
    # order the list by shortest job
    tasks = sorted(tasks, key=lambda task: task.burst)
    schedule_fcfs(tasks)
