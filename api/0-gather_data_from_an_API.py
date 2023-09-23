#!/usr/bin/python3
import requests
import sys
""" Getting data from an API """

def get_employee_name(employee_id):
  url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
  response = requests.get(url)
  
  if response.status_code == 200:
    user = response.json()
    return user.get("name")
  else:
    return None


def get_employee_todo_list_progress(employee_id):
  url = "https://jsonplaceholder.typicode.com/todos"
  params = {"userId": employee_id}
  response = requests.get(url, params=params)

  if response.status_code == 200:
    todos = response.json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    return {
      "completed_tasks": completed,
      "total_number_of_tasks": len(todos),
      }
  else:
    return {}


if __name__ == "__main__":
  employee_id = sys.argv[1]
  employee_name = get_employee_name(employee_id)

  if employee_name is not None:
    employee_todo_list_progress = get_employee_todo_list_progress(employee_id)
    completed = employee_todo_list_progress["completed_tasks"]
    total_number_of_tasks = employee_todo_list_progress["total_number_of_tasks"]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed), total_number_of_tasks))
    [print("\t {}".format(c)) for c in completed]
  else:
    print("Employee with ID {} does not exist.".format(employee_id))
