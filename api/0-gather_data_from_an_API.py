#!/usr/bin/python3
"""
A script that uses a REST API to return information about
an employee's TODO list progress based on a given ID.
"""
import requests
import sys


def gather_data():
    """
    Fetches employee details and TODO progress using the requests module.
    Displays the progress in a specific format.
    """
    if len(sys.argv) < 2:
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        return

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch User information
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_res = requests.get(user_url)
    user_data = user_res.json()

    # Use .get() to access dictionary value as per requirements
    employee_name = user_data.get("name")

    # Fetch TODO list
    todo_url = "{}/todos?userId={}".format(base_url, employee_id)
    todo_res = requests.get(todo_url)
    tasks = todo_res.json()

    # Filter completed tasks and count totals
    completed_tasks = [task for task in tasks if task.get("completed")]
    total_tasks = len(tasks)
    num_done = len(completed_tasks)

    # Print First Line
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_done, total_tasks))

    # Print Task Titles with 1 tabulation and 1 space
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    gather_data()
