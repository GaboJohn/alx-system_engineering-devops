#!/usr/bin/python3
"""
Script to gather data from an API and display TODO list progress for a given employee ID.
"""

import csv
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
    user_id = user_data.get('id')
    username = user_data.get('username')

    # Getting TODO list
    todos_response = requests.get(url + "/todos?userId={}".format(employee_id))
    todos_data = todos_response.json()

    # Writing data to CSV file
    csv_filename = "{}.csv".format(user_id)
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for task in todos_data:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })

    print("Data exported to {}".format(csv_filename))


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
