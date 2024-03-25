#!/usr/bin/python3
"""
Script to gather data from an API and display TODO list progress for a given employee ID.
"""

import json
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

    # Formatting data
    formatted_data = {"USER_ID": []}
    for task in todos_data:
        formatted_data["USER_ID"].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    # Writing data to JSON file
    json_filename = "{}.json".format(user_id)
    with open(json_filename, 'w') as jsonfile:
        json.dump(formatted_data, jsonfile, indent=4)

    print("Data exported to {}".format(json_filename))


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
