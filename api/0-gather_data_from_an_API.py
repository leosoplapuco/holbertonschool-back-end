#!/usr/bin/python3
""" Getting data form and API """
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'


def get_employee_todo_progress(user_id):
    user_response = requests.get(f"{API_URL}/users/{user_id}")
    tasks_response = requests.get(f"{API_URL}/todos?userId={user_id}")

    if user_response.status_code != 200 or tasks_response.status_code != 200:
        print("Failed to retrieve data from the API.")
        return

    user_data = user_response.json()
    tasks_data = tasks_response.json()

    username = user_data.get('name')
    completed_tasks = [task for task in tasks_data if task.get('completed')]

    total_tasks = len(tasks_data)
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {username} is done with tasks ({num_completed_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
    else:
        user_id = int(sys.argv[1])
        get_employee_todo_progress(user_id)
