#!/usr/bin/python3
"""
Script to gather data from an API and export TODO list progress for all employees in JSON format.
"""

import json
import requests

def gather_data():
    """
    Function to gather TODO list progress for all employees
    """

    # API URL
    url = "https://jsonplaceholder.typicode.com"

    # Getting all users
    users_response = requests.get(url + "/users")
    users_data = users_response.json()

    # Dictionary to store data for all employees
    all_employees_data = {}

    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')

        # Getting TODO list for each user
        todos_response = requests.get(url + "/todos?userId={}".format(user_id))
        todos_data = todos_response.json()

        # Formatting data for the user
        user_tasks = []
        for task in todos_data:
            user_tasks.append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            })

        # Adding user tasks to the dictionary
        all_employees_data[user_id] = user_tasks

    # Writing data to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as jsonfile:
        json.dump(all_employees_data, jsonfile, indent=4)

    print("Data exported to {}".format(json_filename))


if __name__ == "__main__":
    gather_data()
