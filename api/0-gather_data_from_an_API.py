#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    # Make requests to get user and task data
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    tasks_response = requests.get(f'{base_url}/todos?userId={employee_id}')

    # Check if the user request was successful
    if user_response.status_code != 200:
        print(f'Failed to retrieve user data. Status code: {user_response.status_code}')
        return

    # Check if the tasks request was successful
    if tasks_response.status_code != 200:
        print(f'Failed to retrieve task data. Status code: {tasks_response.status_code}')
        return

    # Extract user name and task data
    user_data = user_response.json()
    tasks_data = tasks_response.json()

    # Calculate the number of completed tasks and total tasks
    completed_tasks = [task for task in tasks_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(tasks_data)

    # Display the information in the specified format
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
