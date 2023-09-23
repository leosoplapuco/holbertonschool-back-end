#!/usr/bin/python3
""" Getting data from an API """
import requests
import sys


API = 'https://jsonplaceholder.typicode.com'


endpoints = {
        "users": f"{API}/users",
        "todos": f"{API}/todos"
        }


def get_todo_list_progress(employee_id: int) -> str:
    get_employee_endpoint = f"{endpoints['users']}/{employee_id}"
    employee_response = requests.get(get_employee_endpoint)
    employee = employee_response.json()

    get_employee_todos_endpoint = f"{endpoints['todos']}?userId={employee_id}"
    todos_response = requests.get(get_employee_todos_endpoint)
    todos = todos_response.json()

    to_len = len(todos)

    completed_todos = []

    for todo in todos:
        if todo["completed"] is True:
            completed_todos.append(todo)
    com_to_qu = len(completed_todos)

    text = "is done with tasks"
    first_line = f"Employee {employee['name']} {text}({com_to_qu}/{to_len}):\n"

    next_line = ''
    for completed_todo in completed_todos:
        next_line = next_line + "\t " + completed_todo["title"] + "\n"

    return first_line + next_line


if __name__ == '__main__':
    employee_id = sys.argv[1]

    output = get_todo_list_progress(employee_id)

    print(output, end="")
