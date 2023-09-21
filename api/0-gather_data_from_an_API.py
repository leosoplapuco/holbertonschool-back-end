#!/usr/bin/python3
""" Getting data from an API """
import requests
import sys


def get_employee_todo_list_progress(employee_name):
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_name))

    if response.status_code != 200:
        raise Exception("Failed to get employee TODO list progress: {}".format(response.status_code))

    user = response.json()

    todos = requests.get("https://jsonplaceholder.typicode.com/todos", params={"userId": user.get("id")}).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    return {
        "employee_name": user.get("name"),
        "number_of_done_tasks": len(completed),
        "total_number_of_tasks": len(todos),
    }


if __name__ == "__main__":
    employee_name = input("Enter the employee name: ")

    employee_todo_list_progress = get_employee_todo_list_progress(employee_name)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_todo_list_progress["employee_name"],
        employee_todo_list_progress["number_of_done_tasks"],
        employee_todo_list_progress["total_number_of_tasks"],
    ))
    for c in employee_todo_list_progress["completed_tasks"]:
        print("\t {}".format(c))
