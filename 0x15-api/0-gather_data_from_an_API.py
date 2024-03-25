#!/usr/bin/python3
"""
Script to gather data from an API and display TODO
list progress for a given employee ID.
"""

import requests
import sys


def gather_data(employee_id):
    """
    Function to gather TODO list progress for a given employee ID
    """

    # API URL
    url = "https://jsonplaceholder.typicode.com"

    # Getting user information
    user_response = requests.get(url + "/users/{}".format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Getting TODO list
    todos_response = requests.get(url + "/todos?userId={}".format(employee_id))
    todos_data = todos_response.json()

    # Calculating completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task.get('completed'))

    # Displaying progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          completed_tasks, total_tasks))
    for task in todos_data:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    gather_data(employee_id)
