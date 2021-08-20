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

First-come, first-served scheduling algorithm

"""

import CPU
import sys
import driver

from copy import deepcopy

if __name__ == "__main__":
    driver.main(sys.argv)


# Reference: ideas for FCFS scheduling were taken from this book https://www.os-book.com/OS8/os8c/index.html
def schedule_fcfs(tasks):
    total_burst_time = 0
    total_waiting_time = 0
    total_turn_around = 0

    turn_around_times = {task.name: 0 for task in tasks}  # to print out the turnaround times for each process at the end
    waiting_times = deepcopy(turn_around_times)  # to print out the waiting times for each process at the end

    looped_once = False  # for calculating waiting times
    for task in tasks:
        CPU.run(task, task.burst)  # run the task

        if looped_once:
            total_waiting_time += total_burst_time
            waiting_times[task.name] = total_burst_time
        else:
            looped_once = True

        # calculate burst and turnaround times
        total_burst_time += task.burst
        total_turn_around += total_burst_time
        turn_around_times[task.name] = total_burst_time

        # task complete
        print(f"process ({task.name}) arrived at time (0) and ran for ({task.burst}) MS.")

    # summary results
    print(f"\nWaiting times:\n{waiting_times}\n")
    print(f"Turnaround times:\n{turn_around_times}\n")
    CPU.print_avg_time(
        CPU.average_time(total_waiting_time, len(tasks)), "Waiting Time"
    )
    CPU.print_avg_time(
        CPU.average_time(total_turn_around, len(tasks)), "Turnaround Time"
    )
