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

Priority scheduling algorithm

"""

import sys
import driver

from fcfs import schedule_fcfs

if __name__ == "__main__":
    driver.main(sys.argv)


# Reference: ideas for priority scheduling were taken from this book https://www.os-book.com/OS8/os8c/index.html
def schedule_priority(tasks):
    # order the list by priority, increasing numeric value -> increasing priority
    tasks = sorted(tasks, key=lambda task: task.priority, reverse=True)
    schedule_fcfs(tasks)
