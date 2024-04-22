#!/usr/bin/python3
""" Gather data from an API """

#import requests
import urllib
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

    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task['completed'])
    completed_tasks_titles = [task['title']
                              for task in todos_data if task['completed']]

    print("Employee {} is done with task({}/{}):".format(
        user_data['name'], completed_tasks, total_tasks))
    for task_title in completed_tasks_titles:
        print("\t{}".format(task_title))
