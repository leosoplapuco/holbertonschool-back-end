#!/usr/bin/python3
""" Getting data from an API """
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    tasks_response = requests.get(f'{base_url}/todos?userId={employee_id}')

    if user_response.status_code != 200:
        print(f'Failed to retrieve user data. Status code: {user_response.status_code}')
        return

    if tasks_response.status_code != 200:
        print(f'Failed to retrieve task data. Status code: {tasks_response.status_code}')
        return

    user_data = user_response.json()
    tasks_data = tasks_response.json()

    completed_tasks = [task for task in tasks_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(tasks_data)

    print(f'Employee {user_data["name"]} is done with tasks({num_completed_tasks}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t{task["title"]}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print('Employee ID must be an integer.')
