#!/usr/bin/python3
"""extend your Python script to export data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos_res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    user = user_res.json()
    todos = todos_res.json()

    tasks = []
    for todo in todos:
        task = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user.get('username')}
        tasks.append(task)

    with open(f'{employee_id}.json', 'w') as json_file:
        json.dump({employee_id: tasks}, json_file)
