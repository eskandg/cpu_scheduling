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
  driver.py

  Schedule is in the format

  [name] [priority] [CPU burst]

"""

import sys
from os import path
from task import Task
import schedulers


# runs the driver, this also can be run by each of the files containing the schedulers, passing in their own sys.argv
def main(argv):

    if len(argv) > 2:
        print(f"Error: Too many arguments given for \"{argv[0]}\". Only one argument, a text file containing tasks.")
        exit(-1)

    try:
        # read the file
        with open(argv[1], "r") as fd:
            tasks = fd.read().splitlines()  # assuming one task per line, split each into different elements

        re_run = True  # give the option to keep running tests if you run driver.py

        scheduler_choice = None  # for use with pick_scheduler()
        tasks_created = False  # for use with re_run, we don't want to recreate the tasks every loop
        while re_run and scheduler_choice != "q":
            if path.basename(argv[0]) == "driver.py":  # give the option to pick a scheduler
                scheduler_choice = pick_scheduler()  # tuple returning a string scheduler_name and bool re_run
                re_run = scheduler_choice[1]
                scheduler_choice = path.basename(scheduler_choice[0])

            try:  # all or nothing approach (send all tasks or do nothing)
                if not tasks_created:
                    task_names = []
                    for index, task in enumerate(tasks):
                        task_info = task.split(", ")  # split task information into a list

                        if len(task_info) != 3:  # [name] [priority] [CPU burst]
                            print(f"\nError: Tried to create a task but number of fields is invalid.")
                            print(f"Invalid task data caught: {task_info}")
                            raise

                        name = task_info[0]
                        try:
                            priority = int(task_info[1])
                            burst = int(task_info[2])
                        except ValueError:
                            print(f"Error: Invalid integer. Received Priority -> {task_info[1]} and Burst -> {task_info[2]}")
                            raise

                        # do more error-handling
                        if name in task_names:  # checking for duplicate process names
                            print(f"Error: Tried to create a task with an existing name \"{name}\".")
                            raise
                        task_names.append(name)

                        if burst < 1:
                            print(f"Error: Tried to create a task with a CPU burst less than one. Got \"{burst}\", minimum is 1.")
                            raise

                        # check priority is in the correct range
                        if priority < schedulers.MIN_PRIORITY:
                            print(f"\nError: Tried to create a task with priority under the priority limit (limit: {schedulers.MIN_PRIORITY})")
                            print(f"Invalid priority: {priority}")
                            raise
                        elif priority > schedulers.MAX_PRIORITY:
                            print(f"\nError: Tried to create a task with priority over the priority limit (limit: {schedulers.MAX_PRIORITY})")
                            print(f"Invalid priority: {priority}")
                            raise

                        tasks[index] = Task(name, priority, burst)  # replace with Task objects

                    tasks_created = True  # so we don't create them again when running driver.py

                if scheduler_choice != "q":  # if the user doesn't choose to quit
                    if scheduler_choice is None:  # e.g if we run rr.py
                        file_no_py_extension = path.basename(argv[0][:len(argv[0]) - 3])
                        schedulers.schedule(file_no_py_extension, tasks)
                        re_run = False  # since we aren't running driver.py
                    else:  # if we run driver.py pass in what scheduler the user chose
                        schedulers.schedule(scheduler_choice, tasks)  # invoke the scheduler in scheduler.py
                        input("\nPress enter to continue... ")  # just to give the user a chance to read results

            except:
                print(f"Error: Invalid tasks. \"{argv[1]}\" may not have the correct data.")
                break

    except FileNotFoundError:
        print(f"Error: Could not open \"{argv[1]}\". Check if it exists.")
    except IndexError:
        print(f"Error: Not enough arguments (\"{path.basename(argv[0])}\")")

# below are functions used by main()


def print_list_of_schedulers(): # small function to print out our schedulers

    print("\nPick a Scheduler\n----------------")

    for scheduler_name in schedulers.SCHEDULERS.keys():
        print(scheduler_name)

    print("\nEnter \"q\" to quit and stop testing.\n")


def pick_scheduler():

    re_run = True  # since we are running driver.py and want to give the user the option to test everything

    print_list_of_schedulers()

    scheduler_choice = input("Enter the exact name of the scheduler to use as provided above: ")

    if scheduler_choice == "q":
        re_run = False
    else:
        while scheduler_choice not in schedulers.SCHEDULERS.keys():
            print(f"Invalid input, entered \"{scheduler_choice}\"\n")

            print_list_of_schedulers()
            scheduler_choice = input("Enter the exact name of the scheduler to use: ")

            if scheduler_choice == "q":
                re_run = False
                break

    return scheduler_choice, re_run


if __name__ == "__main__":
    main(sys.argv)
