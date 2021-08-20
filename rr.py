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

Round robin scheduling algorithm

"""

import CPU
import sys
import driver

from collections import deque  # to use as a queue
from copy import deepcopy

if __name__ == "__main__":
    driver.main(sys.argv)


# Reference: ideas for RR scheduling were taken from this book https://www.os-book.com/OS8/os8c/index.html
def schedule_rr(tasks):
    # copy the tasks, we will be changing the burst with each time slice, prevents a bug when running again in driver.py
    copy_of_tasks = deepcopy(tasks)
    queue = deque(copy_of_tasks)

    total_burst_time = 0
    turn_around_times = {task.name: 0 for task in copy_of_tasks}  # to print out the turnaround times for each process at the end
    waiting_times = {task.name: task.burst for task in copy_of_tasks}  # to print out the waiting times for each process at the end

    i = 0
    while queue:  # while not empty
        cpu_burst_remaining = CPU.QUANTUM - queue[i].burst

        # run the process and calculate the total burst time
        if cpu_burst_remaining < 0:  # the burst time was larger than the quantum time
            CPU.run(queue[i], CPU.QUANTUM)
            total_burst_time += CPU.QUANTUM
            queue[i].burst = abs(cpu_burst_remaining)  # update burst
            print(f"process ({queue[i].name}) arrived at time (0) and ran for ({CPU.QUANTUM}) MS with ({queue[i].burst}) MS remaining.")

            queue.append(queue[i])
            queue.popleft()
        elif 0 <= cpu_burst_remaining <= CPU.QUANTUM:
            if cpu_burst_remaining == 0:  # if the burst left is the same as quantum
                CPU.run(queue[i], CPU.QUANTUM)
                total_burst_time += CPU.QUANTUM
            else:
                CPU.run(queue[i], queue[i].burst)
                total_burst_time += queue[i].burst

            # calculate turnaround times and waiting times
            turn_around_times[queue[i].name] = total_burst_time
            waiting_times[queue[i].name] = turn_around_times[queue[i].name] - waiting_times[queue[i].name]

            # task complete
            print(f"process ({queue[i].name}) arrived at time (0) and ran for ({queue[i].burst}) MS.")

            queue[i].burst = 0  # we are done with the process
            queue.popleft()

        try:
            i = i % len(queue)  # go round
        except ZeroDivisionError:  # 0 % 0 when index is 0 and size of the queue is 0
            break

    # summary results
    print(f"\nWaiting times:\n{waiting_times}\n")
    print(f"Turnaround times:\n{turn_around_times}\n")
    CPU.print_avg_time(
        CPU.average_time(sum(waiting_times.values()), len(tasks)), "Waiting Time"
    )
    CPU.print_avg_time(
        CPU.average_time(sum(turn_around_times.values()), len(tasks)), "Turnaround Time"
    )
