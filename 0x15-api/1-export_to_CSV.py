#!/usr/bin/python3
"""Extend your Python script to export data in the CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)  # Add this parameter
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            writer.writerow([task['userId'],
                             user_data['username'],
                             task['completed'],
                             task['title']])

    print(
        "Number of tasks written to CSV for employee {} is {}.".format(
            user_data['username'],
            len(todos_data)))
